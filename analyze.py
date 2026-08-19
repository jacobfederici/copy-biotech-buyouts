#!/usr/bin/env python3
"""Build the comprehensive cross-deal analysis from reports + dataset + LLM.

Per company it assembles deterministic fields (premium, deal size, trailing
price moves) from the parsed dataset, plus qualitative fields extracted once
per report by an LLM (cached): development stage, value-inflection events,
offer low/high, number of interested parties, inbound vs. outbound, early
leak, and first-contact date (for engagement->deal timing).

    .venv/bin/python buyouts/analyze.py            # extract (cached) + build
    .venv/bin/python buyouts/analyze.py --no-llm   # assemble from cache only
    .venv/bin/python buyouts/analyze.py LOXO ICGN  # only these (test)

Reads:  buyouts/reports/*.md + buyouts/data/{deals.json, prices.csv}
Writes: buyouts/data/{analysis_rows.json, analysis.csv, analysis.md}
"""
import csv
import json
import sys
import datetime as dt
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

from common import (DATA, REPORTS, DEALS_JSON, ROWS_JSON, ANALYSIS_CSV, ANALYSIS_MD,
                    LLM_MODEL, load_prices, trailing_move, first_date,
                    section, llm_json_cached, fmt_pct, fmt_num, fmt_size)

MAX_WORKERS = 6

SCHEMA_HINT = """Return ONLY a JSON object with EXACTLY these keys:
{
 "company_stage": "<short: lead asset stage + commercial status, e.g. 'Phase 3 lead + 1 approved drug' or 'Pre-revenue, Phase 2'>",
 "value_inflection_events": ["<= 4 short strings: the major events that materially moved the company's value (pivotal data, FDA action, partnership). [] if none stated>"],
 "offer_low": <number or null: LOWEST per-share offer made by any bidder during the process>,
 "offer_high": <number or null: HIGHEST per-share offer = the final deal price>,
 "offer_currency": "<USD/EUR/etc>",
 "num_parties_interested": <integer: count of distinct parties that made offers or were engaged in the sale process; 1 if only the buyer>,
 "interest_direction": "<'inbound' if the buyer approached the company; 'outbound' if the company initiated/ran a sale process or shopped itself; 'both'; or 'unclear'>",
 "first_contact_date": "<YYYY-MM-DD of first contact with the eventual buyer, or null>",
 "leaked_1m_plus_early": <true/false: was the acquisition reported/rumored in the press 1+ MONTH before the official announcement? Use the Buyout Rumors section>,
 "leak_detail": "<short: outlet + how early, or '' if none>"
}
No prose, no markdown fences."""

SYSTEM = ("You are extracting structured M&A facts from an SC 14D-9 buyout report. "
          "Base every field ONLY on the text provided.")


def report_excerpt(text):
    keep = ["Summary", "Timeline", "Interaction History", "Pipeline",
            "Value Inflection Points", "Buyout Rumors"]
    parts = []
    for h in keep:
        body = section(text, h).strip()
        if body:
            parts.append(f"## {h}\n{body[:4500]}")
    return "\n\n".join(parts)[:16000]


def extract_one(fp, use_llm):
    """(stem, llm_dict) — cached per report stem."""
    prompt = SCHEMA_HINT + "\n\n=== REPORT ===\n" + report_excerpt(
        fp.read_text(errors="replace"))
    return fp.stem, llm_json_cached(prompt, fp.stem, system=SYSTEM, use_llm=use_llm)


def build_rows(files, deals, prices, extracts):
    rows = []
    for fp in files:
        d = deals.get(fp.name)
        if not d:
            continue
        llm = extracts.get(fp.stem, {})
        ann = first_date(d.get("announcement_date") or "")
        ser = prices.get(fp.name, [])
        end_anchor = (ann - dt.timedelta(days=28)) if ann else None  # unaffected endpoint
        fc = first_date(llm.get("first_contact_date") or "")
        rows.append({
            "ticker": d.get("ticker"),
            "company": d.get("company"),
            "acquirer": d.get("acquirer"),
            "ann_date": d.get("announcement_date"),
            "close_date": d.get("close_date"),
            "deal_size_m": d.get("implied_equity_value_m"),
            "per_share": d.get("per_share_upfront"),
            "max_cvr": d.get("max_per_share_cvr"),
            "has_cvr": d.get("has_cvr"),
            "payment": d.get("payment_type"),
            "premium": d.get("premium_to_unaffected"),
            "ann_to_close_days": d.get("ann_to_close_days"),
            "data_quality": d.get("data_quality"),
            "ret_3m": trailing_move(ser, end_anchor, 3),
            "ret_6m": trailing_move(ser, end_anchor, 6),
            "ret_12m": trailing_move(ser, end_anchor, 12),
            "ret_24m": trailing_move(ser, end_anchor, 24),
            "stage": llm.get("company_stage"),
            "inflections": llm.get("value_inflection_events"),
            "offer_low": llm.get("offer_low"),
            "offer_high": llm.get("offer_high"),
            "offer_ccy": llm.get("offer_currency"),
            "n_parties": llm.get("num_parties_interested"),
            "direction": llm.get("interest_direction"),
            "first_contact": llm.get("first_contact_date"),
            "eng_to_deal_days": (ann - fc).days if (ann and fc) else None,
            "leaked_early": llm.get("leaked_1m_plus_early"),
            "leak_detail": llm.get("leak_detail"),
            "llm_error": llm.get("_error"),
        })
    rows.sort(key=lambda r: (r["ann_date"] in (None, ""), r["ann_date"] or ""))
    return rows


def write_outputs(rows):
    ROWS_JSON.write_text(json.dumps(rows, default=str))
    with open(ANALYSIS_CSV, "w", newline="") as f:
        w = csv.writer(f)
        cols = [k for k in rows[0] if k != "inflections"]
        w.writerow(cols + ["inflections"])
        for r in rows:
            infl = r["inflections"]
            w.writerow([r[c] for c in cols] +
                       [" | ".join(infl) if isinstance(infl, list) else ""])
    write_markdown(rows)


def write_markdown(rows):
    n = len(rows)

    def med(key):
        v = sorted(r[key] for r in rows if isinstance(r[key], (int, float)))
        return v[len(v) // 2] if v else None

    prem = [r["premium"] for r in rows if isinstance(r["premium"], (int, float))]
    stage_n, dir_n, leak_n = defaultdict(int), defaultdict(int), defaultdict(int)
    for r in rows:
        if r["stage"]:
            stage_n[r["stage"]] += 1
        if r["direction"]:
            dir_n[r["direction"]] += 1
        leak_n["leaked 1m+" if r["leaked_early"] is True else
               ("no leak" if r["leaked_early"] is False else "unknown")] += 1
    cvr = sum(1 for r in rows if r["has_cvr"] in (True, "True"))

    L = ["# Biotech Buyout Analysis — Comprehensive Cross-Deal Page\n",
         f"_Generated from {n} SC 14D-9 acquisition reports in `buyouts/reports/`._\n",
         "Deterministic fields (premium, size, trailing price moves) come from "
         "`deals.json` / `prices.csv`. Qualitative fields (stage, value-inflection events, "
         f"offer range, parties, timing, direction, early leak) are extracted by `{LLM_MODEL}`.\n",
         "## Portfolio Summary\n", f"- **Deals analyzed:** {n}"]
    if prem:
        ps = sorted(prem)
        L.append(f"- **Premium (vs unaffected):** median **{fmt_pct(ps[len(ps)//2])}**, "
                 f"range {fmt_pct(min(prem))}–{fmt_pct(max(prem))} (n={len(prem)})")
    a2c = med("ann_to_close_days")
    if a2c:
        L.append(f"- **Announcement → close:** median **{a2c:.0f} days**")
    L.append(f"- **Deals with a CVR:** {cvr} of {n}")
    L.append("- **Trailing return to unaffected (median):** "
             f"3mo {fmt_pct(med('ret_3m'), signed=True)}, 6mo {fmt_pct(med('ret_6m'), signed=True)}, "
             f"12mo {fmt_pct(med('ret_12m'), signed=True)}, 24mo {fmt_pct(med('ret_24m'), signed=True)}")
    if stage_n:
        L.append("- **Company stage mix:** " + ", ".join(
            f"{k} ({v})" for k, v in sorted(stage_n.items(), key=lambda x: -x[1])[:8]))
    if dir_n:
        L.append("- **Interest direction:** " + ", ".join(
            f"{k} ({v})" for k, v in sorted(dir_n.items(), key=lambda x: -x[1])))
    L.append("- **Early leak (1+ month before deal):** " + ", ".join(
        f"{k} ({v})" for k, v in sorted(leak_n.items(), key=lambda x: -x[1])))
    L.append("")

    hdr = ["Company", "Ticker", "Buyer", "Ann.", "Size", "Premium", "Stage",
           "Bid low→high", "# Parties", "Eng→Deal", "Direction", "Leak?",
           "3mo", "6mo", "12mo", "2yr"]
    L.append("## Master Table\n")
    L.append("| " + " | ".join(hdr) + " |")
    L.append("|" + "|".join(["---"] * len(hdr)) + "|")
    for r in rows:
        offer = "—"
        if r["offer_low"] is not None or r["offer_high"] is not None:
            offer = f"{fmt_num(r['offer_low'])}→{fmt_num(r['offer_high'])}"
        eng = f"{r['eng_to_deal_days']/30.4:.1f} mo" if r["eng_to_deal_days"] else "—"
        cells = [str(r["company"] or "")[:34], r["ticker"] or "—", str(r["acquirer"] or "")[:26],
                 r["ann_date"] or "—", fmt_size(r["deal_size_m"]), fmt_pct(r["premium"]),
                 r["stage"] or "—", offer,
                 str(r["n_parties"]) if r["n_parties"] is not None else "—", eng,
                 r["direction"] or "—",
                 "yes" if r["leaked_early"] is True else ("no" if r["leaked_early"] is False else "—"),
                 fmt_pct(r["ret_3m"], signed=True), fmt_pct(r["ret_6m"], signed=True),
                 fmt_pct(r["ret_12m"], signed=True), fmt_pct(r["ret_24m"], signed=True)]
        L.append("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in cells) + " |")
    L.append("")

    L.append("## Per-Deal Detail\n")
    for r in rows:
        L.append(f"### {r['company']} ({r['ticker'] or '—'})")
        L.append(f"- **Acquirer:** {r['acquirer'] or '—'}")
        L.append(f"- **Announced / Closed:** {r['ann_date'] or '—'} / {r['close_date'] or '—'}")
        L.append(f"- **Deal size:** {fmt_size(r['deal_size_m'])}"
                 + (f"  ·  {fmt_num(r['per_share'])}/sh" if r["per_share"] is not None else "")
                 + ("  + CVR" if r["has_cvr"] in (True, "True") else ""))
        L.append(f"- **Premium (vs unaffected):** {fmt_pct(r['premium'])}")
        L.append(f"- **Stage:** {r['stage'] or '—'}")
        L.append(f"- **Value-inflecting events:** "
                 + ("; ".join(r["inflections"]) if isinstance(r["inflections"], list) and r["inflections"] else "—"))
        offer = "—"
        if r["offer_low"] is not None or r["offer_high"] is not None:
            offer = f"{fmt_num(r['offer_low'])} → {fmt_num(r['offer_high'])}"
        L.append(f"- **Offer range (low→high):** {offer}")
        L.append(f"- **Interested parties:** {r['n_parties'] if r['n_parties'] is not None else '—'}")
        L.append(f"- **Interest direction:** {r['direction'] or '—'}")
        eng = f"{r['eng_to_deal_days']/30.4:.1f} months" if r["eng_to_deal_days"] else "—"
        L.append(f"- **Engagement → deal:** {eng}")
        L.append(f"- **Reported early (1mo+):** "
                 + ("yes" if r["leaked_early"] is True else ("no" if r["leaked_early"] is False else "—"))
                 + (f" — {r['leak_detail']}" if r["leak_detail"] else ""))
        L.append(f"- **Trailing return to unaffected:** 3mo {fmt_pct(r['ret_3m'], signed=True)} · "
                 f"6mo {fmt_pct(r['ret_6m'], signed=True)} · 12mo {fmt_pct(r['ret_12m'], signed=True)} · "
                 f"2yr {fmt_pct(r['ret_24m'], signed=True)}")
        L.append("")
    ANALYSIS_MD.write_text("\n".join(L), encoding="utf-8")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    use_llm = "--no-llm" not in sys.argv
    DATA.mkdir(parents=True, exist_ok=True)

    deals = {x["file"]: x for x in json.loads(DEALS_JSON.read_text())}
    prices = load_prices()
    files = [fp for fp in sorted(REPORTS.glob("*.md"))
             if fp.name != "README.md" and fp.name in deals]
    if args:
        want = {a.upper() for a in args}
        files = [fp for fp in files if fp.stem.split("_")[-1].upper() in want or fp.name in args]

    extracts = {}
    if use_llm:
        print(f"Running LLM extraction over {len(files)} reports ({LLM_MODEL})...")
    done = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {ex.submit(extract_one, fp, use_llm): fp for fp in files}
        for fut in as_completed(futs):
            stem, data = fut.result()
            extracts[stem] = data
            done += 1
            if done % 25 == 0 or done == len(files):
                print(f"  {done}/{len(files)}")

    rows = build_rows(files, deals, prices, extracts)
    if not rows:
        print("No rows built.")
        return
    write_outputs(rows)
    n_llm = sum(1 for r in rows if r["stage"])
    errs = sum(1 for r in rows if r["llm_error"])
    print(f"\nRows: {len(rows)} | with LLM fields: {n_llm} | errors: {errs}")
    print(f"Wrote {ROWS_JSON.name}, {ANALYSIS_CSV.name}, {ANALYSIS_MD.name}")


if __name__ == "__main__":
    main()
