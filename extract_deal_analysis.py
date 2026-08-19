"""Loop every SC 14D9 buyout report through Gemini 3.5 Flash and extract a
structured set of deal-analysis fields, then assemble one comprehensive
analysis page.

Usage:
    .venv/bin/python buyouts/extract_deal_analysis.py            # extract + build
    .venv/bin/python buyouts/extract_deal_analysis.py --build    # rebuild page from cache only
"""

import os
import sys
import json
import time
import hashlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parent          # .../buyouts
REPORTS_DIR = ROOT / "reports"
DATA_DIR = ROOT / "data"
DEALS_JSON = DATA_DIR / "deals.json"
CACHE_DIR = DATA_DIR / "llm_cache" / "deal_analysis"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
OUT_PAGE = ROOT / "COMPREHENSIVE_DEAL_ANALYSIS.md"

MODEL = "deepseek/deepseek-v4-pro"
API_KEY = os.environ.get("OPENROUTER_API_KEY")  # only needed for live extraction, not --build
URL = "https://openrouter.ai/api/v1/chat/completions"

MAX_CHARS = 220_000  # plenty for metadata + timeline + interaction + inflection + price table
WORKERS = 12

# Files that are not standard single-deal reports
SKIP_FILES = {"README.md", "king_pharmaceuticals_acquisition_report.md"}

SYSTEM = """You are a biotech M&A analyst extracting structured data from a single SC 14D9 / merger deal dossier.
The dossier is a Markdown report about ONE target company being acquired. It contains sections:
metadata header, Summary, Timeline, Interaction History, Pipeline, Offer Economics, a weekly Stock Price
table (spanning ~2 years before announcement through close), Value Inflection Points, and Company News.

Extract ONLY what the document supports. If a value is not determinable from the document, use null
(for numbers) or "unknown" (for strings). Do not invent. Compute prior price moves from the weekly
Stock Price table relative to the announcement date when the table is present.

Return a single JSON object, no prose, exactly matching this schema:

{
  "company": string,                      // target company name
  "ticker": string,
  "buyer": string,
  "announcement_date": string,            // YYYY-MM-DD or "unknown"
  "close_date": string,                   // YYYY-MM-DD or "unknown" (or status if terminated/pending)
  "deal_status": string,                  // completed | pending | terminated | unknown
  "deal_size_usd_m": number|null,         // total equity/deal value in USD millions
  "final_offer_per_share": number|null,
  "payment_type": string,                 // cash | stock | mixed | cash+CVR | unknown
  "has_cvr": boolean,

  "premium": {
     "pct": number|null,                  // headline premium % vs unaffected price if stated or computable
     "basis": string                      // brief note: what price the premium is vs, or how derived
  },

  "company_stage": string,                // overall company maturity: e.g. "commercial", "Phase 3 / pre-approval", "Phase 2", "Phase 1", "approved+marketed", "diversified pharma". Base on lead asset / pipeline.
  "lead_asset": string,                   // name of the single most value-driving asset/product
  "lead_asset_stage": string,             // stage of that lead asset

  "value_inflection_events": [            // major events that moved value (from Value Inflection Points + Timeline/News). Empty list if none identifiable.
     {"date": string, "event": string, "approx_change_pct": number|null}
  ],

  "offer_low_per_share": number|null,     // first / lowest disclosed offer in the negotiation
  "offer_high_per_share": number|null,    // final / highest disclosed offer (usually == final_offer_per_share)
  "num_offers_or_rounds": number|null,    // count of distinct price proposals disclosed in interaction history

  "num_parties_interested": number|null,  // distinct bidders/strategic parties who engaged or signed CDAs
  "process_type": string,                 // "broad auction" | "limited / targeted" | "single bidder / bilateral" | "unknown"

  "engagement_to_deal_days": number|null, // days from first substantive contact/engagement to signing of merger agreement
  "first_engagement_date": string,        // YYYY-MM-DD or "unknown"
  "signing_date": string,                 // YYYY-MM-DD or "unknown"

  "interest_direction": string,           // "inbound (buyer approached target)" | "outbound (target ran process / sought buyer)" | "mixed" | "unknown"

  "leaked_early": {                        // was the deal/interest publicly reported 1+ month before the official announcement?
     "leaked": boolean,                    // true only if there is evidence of a press report/rumor >= ~1 month prior
     "details": string                     // brief note or "unknown"
  },

  "price_move_3m_pct": number|null,        // % change in close from ~3 months before announcement to the last pre-announcement close
  "price_move_6m_pct": number|null,
  "price_move_12m_pct": number|null,
  "price_move_24m_pct": number|null,

  "notes": string                          // one-sentence analyst note on anything notable
}
"""

USER_TMPL = "Extract the deal-analysis JSON for this dossier.\n\n=== DOSSIER START ===\n{body}\n=== DOSSIER END ==="


def call_llm(body: str) -> dict:
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": USER_TMPL.format(body=body)},
        ],
        "temperature": 0.0,
        "response_format": {"type": "json_object"},
    }
    last_err = None
    for attempt in range(5):
        try:
            r = requests.post(URL, headers=headers, json=payload, timeout=240)
            if r.status_code == 200:
                txt = r.json()["choices"][0]["message"]["content"]
                return json.loads(txt)
            if r.status_code in (429, 500, 502, 503):
                last_err = f"{r.status_code}: {r.text[:200]}"
                time.sleep(5 * (attempt + 1))
                continue
            raise RuntimeError(f"OpenRouter {r.status_code}: {r.text[:300]}")
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            last_err = str(e)
            time.sleep(4 * (attempt + 1))
    raise RuntimeError(f"OpenRouter failed after retries: {last_err}")


def cache_path(fname: str) -> Path:
    return CACHE_DIR / (fname.replace(".md", "") + ".json")


def process_one(path: Path) -> dict:
    cp = cache_path(path.name)
    if cp.exists():
        try:
            return json.loads(cp.read_text())
        except Exception:
            pass
    body = path.read_text(encoding="utf-8", errors="ignore")[:MAX_CHARS]
    data = call_llm(body)
    data["_source_file"] = path.name
    cp.write_text(json.dumps(data, indent=2))
    return data


def extract_all() -> list[dict]:
    files = sorted(p for p in REPORTS_DIR.glob("*.md") if p.name not in SKIP_FILES)
    print(f"Processing {len(files)} reports with {MODEL} ({WORKERS} workers)...")
    results = []
    done = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(process_one, p): p for p in files}
        for fut in as_completed(futs):
            p = futs[fut]
            done += 1
            try:
                results.append(fut.result())
                print(f"  [{done}/{len(files)}] OK  {p.name}")
            except Exception as e:
                print(f"  [{done}/{len(files)}] FAIL {p.name}: {e}")
    return results


# ---------------- page assembly ----------------

def load_cached() -> list[dict]:
    out = []
    for cp in sorted(CACHE_DIR.glob("*.json")):
        try:
            out.append(json.loads(cp.read_text()))
        except Exception:
            pass
    return out


def num(v):
    return v if isinstance(v, (int, float)) else None


def fmt(v, suffix="", pct=False):
    if v is None or v == "" or v == "unknown":
        return "—"
    if isinstance(v, float):
        if pct:
            return f"{v:+.0f}%"
        return f"{v:,.1f}{suffix}"
    if isinstance(v, int):
        if pct:
            return f"{v:+d}%"
        return f"{v:,}{suffix}"
    return str(v)


def median(xs):
    xs = sorted(x for x in xs if isinstance(x, (int, float)))
    if not xs:
        return None
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def load_pipeline_premiums() -> dict:
    """Map source-report filename -> deterministic premium_to_unaffected (%),
    from the parse.py/analyze.py pipeline (data/deals.json). Used to backfill the
    premium where the LLM left it null but the weekly price feed supports one."""
    if not DEALS_JSON.exists():
        return {}
    out = {}
    for d in json.loads(DEALS_JSON.read_text()):
        p = d.get("premium_to_unaffected")
        if isinstance(p, (int, float)):
            out[d["file"]] = round(p * 100, 1)   # fraction -> percent
    return out


def merge_premium(rows: list[dict]):
    """Set r['_prem_pct'] / r['_prem_src'] on each row. Prefer the filing-stated
    LLM premium; fall back to the pipeline's price-feed premium when the LLM left
    it null. r['_prem_src'] is 'filing', 'price feed', or None."""
    pipe = load_pipeline_premiums()
    for r in rows:
        llm_p = num((r.get("premium") or {}).get("pct"))
        if llm_p is not None:
            r["_prem_pct"], r["_prem_src"] = llm_p, "filing"
            continue
        fb = pipe.get(r.get("_source_file"))
        if fb is not None:
            r["_prem_pct"], r["_prem_src"] = fb, "price feed"
            basis = (r.get("premium") or {}).get("basis") or ""
            note = "computed from weekly price feed vs. ~4-week-pre-announcement (unaffected) close"
            r.setdefault("premium", {})
            r["premium"]["basis"] = f"{note}" + (f"; filing note: {basis}" if basis and basis != "unknown" else "")
        else:
            r["_prem_pct"], r["_prem_src"] = None, None


def build_page(rows: list[dict]):
    rows = [r for r in rows if r.get("company")]
    rows.sort(key=lambda r: (r.get("announcement_date") or "9999"))
    merge_premium(rows)

    n = len(rows)
    premiums = [r["_prem_pct"] for r in rows if r.get("_prem_pct") is not None]
    n_filing = sum(1 for r in rows if r.get("_prem_src") == "filing")
    n_feed = sum(1 for r in rows if r.get("_prem_src") == "price feed")
    parties = [num(r.get("num_parties_interested")) for r in rows]
    parties = [p for p in parties if p is not None]
    eng_days = [num(r.get("engagement_to_deal_days")) for r in rows]
    eng_days = [d for d in eng_days if d is not None]
    inbound = sum(1 for r in rows if str(r.get("interest_direction", "")).startswith("inbound"))
    outbound = sum(1 for r in rows if str(r.get("interest_direction", "")).startswith("outbound"))
    leaked = sum(1 for r in rows if (r.get("leaked_early") or {}).get("leaked") is True)
    cvr = sum(1 for r in rows if r.get("has_cvr") is True)

    L = []
    L.append("# Comprehensive Buyout Deal Analysis")
    L.append("")
    L.append(f"*One row per SC 14D9 / merger dossier in `buyouts/reports/`. "
             f"Extracted by looping every report through **{MODEL}** (via OpenRouter).*")
    L.append("")
    L.append(f"**Deals analyzed:** {n}")
    L.append("")

    # ---- Aggregate summary ----
    L.append("## Portfolio-Level Summary")
    L.append("")
    L.append("| Metric | Value |")
    L.append("| --- | --- |")
    L.append(f"| Deals with a computable premium | {len(premiums)} |")
    L.append(f"| — stated in filing / computed from price feed | {n_filing} / {n_feed} |")
    if premiums:
        L.append(f"| Median premium | {median(premiums):+.0f}% |")
        L.append(f"| Premium range | {min(premiums):+.0f}% to {max(premiums):+.0f}% |")
    if parties:
        L.append(f"| Median # parties interested | {median(parties):.0f} |")
    if eng_days:
        L.append(f"| Median engagement→signing | {median(eng_days):.0f} days (~{median(eng_days)/30:.1f} mo) |")
    L.append(f"| Inbound (buyer approached) | {inbound} |")
    L.append(f"| Outbound (target ran process) | {outbound} |")
    L.append(f"| Deals leaked/reported ≥1 month early | {leaked} |")
    L.append(f"| Deals with a CVR | {cvr} |")
    L.append("")

    # ---- Master table ----
    L.append("## Master Deal Table")
    L.append("")
    hdr = [
        "Company", "Ticker", "Buyer", "Announced", "Size ($M)", "Stage",
        "Premium", "Offer Low→High", "#Rounds", "#Parties", "Eng→Deal",
        "Direction", "Leaked Early", "Pmt", "3mo", "6mo", "12mo", "2yr prior",
    ]
    L.append("| " + " | ".join(hdr) + " |")
    L.append("| " + " | ".join("---" for _ in hdr) + " |")
    for r in rows:
        prem_cell = fmt(num(r.get("_prem_pct")), pct=True)
        if r.get("_prem_src") == "price feed" and prem_cell != "—":
            prem_cell += " †"
        low = r.get("offer_low_per_share")
        high = r.get("offer_high_per_share")
        offer_rng = "—"
        if low is not None or high is not None:
            offer_rng = f"${fmt(low)}→${fmt(high)}"
        leak = (r.get("leaked_early") or {}).get("leaked")
        leak_s = "Yes" if leak is True else ("No" if leak is False else "—")
        eng = r.get("engagement_to_deal_days")
        eng_s = f"{eng:.0f}d" if isinstance(eng, (int, float)) else "—"
        cells = [
            (r.get("company") or "")[:38],
            r.get("ticker", "—"),
            (r.get("buyer") or "—")[:28],
            r.get("announcement_date", "—"),
            fmt(num(r.get("deal_size_usd_m"))),
            (r.get("company_stage") or "—")[:24],
            prem_cell,
            offer_rng,
            fmt(num(r.get("num_offers_or_rounds"))),
            fmt(num(r.get("num_parties_interested"))),
            eng_s,
            (r.get("interest_direction") or "—").split(" ")[0],
            leak_s,
            (r.get("payment_type") or "—")[:10],
            fmt(num(r.get("price_move_3m_pct")), pct=True),
            fmt(num(r.get("price_move_6m_pct")), pct=True),
            fmt(num(r.get("price_move_12m_pct")), pct=True),
            fmt(num(r.get("price_move_24m_pct")), pct=True),
        ]
        L.append("| " + " | ".join(str(c).replace("|", "/") for c in cells) + " |")
    L.append("")
    L.append("† Premium computed from the weekly price feed (offer vs. the ~4-week-pre-announcement "
             "unaffected close) where the filing did not state a headline premium. All other premiums "
             "are as stated in the dossier.")
    L.append("")

    # ---- Per-deal detail ----
    L.append("## Per-Deal Detail")
    L.append("")
    for r in rows:
        L.append(f"### {r.get('company')} ({r.get('ticker','—')}) — {r.get('buyer','—')}")
        L.append("")
        prem = r.get("premium") or {}
        L.append(f"- **Announced / Closed:** {r.get('announcement_date','—')} / {r.get('close_date','—')} "
                 f"({r.get('deal_status','—')})")
        L.append(f"- **Deal size:** {fmt(num(r.get('deal_size_usd_m')))} $M | "
                 f"**Final offer:** ${fmt(num(r.get('final_offer_per_share')))}/sh | "
                 f"**Payment:** {r.get('payment_type','—')}{' + CVR' if r.get('has_cvr') else ''}")
        src_tag = " *(computed from price feed)*" if r.get("_prem_src") == "price feed" else ""
        L.append(f"- **Premium:** {fmt(num(r.get('_prem_pct')), pct=True)}{src_tag} — {prem.get('basis','—')}")
        L.append(f"- **Company stage:** {r.get('company_stage','—')} | "
                 f"**Lead asset:** {r.get('lead_asset','—')} ({r.get('lead_asset_stage','—')})")
        L.append(f"- **Offers:** low ${fmt(num(r.get('offer_low_per_share')))} → high "
                 f"${fmt(num(r.get('offer_high_per_share')))} over {fmt(num(r.get('num_offers_or_rounds')))} round(s)")
        L.append(f"- **Parties interested:** {fmt(num(r.get('num_parties_interested')))} | "
                 f"**Process:** {r.get('process_type','—')} | **Direction:** {r.get('interest_direction','—')}")
        L.append(f"- **Engagement→signing:** {fmt(num(r.get('engagement_to_deal_days')))} days "
                 f"({r.get('first_engagement_date','—')} → {r.get('signing_date','—')})")
        leak = r.get("leaked_early") or {}
        L.append(f"- **Leaked ≥1mo early:** {'Yes' if leak.get('leaked') else 'No'} — {leak.get('details','—')}")
        L.append(f"- **Prior price moves:** 3mo {fmt(num(r.get('price_move_3m_pct')), pct=True)} | "
                 f"6mo {fmt(num(r.get('price_move_6m_pct')), pct=True)} | "
                 f"12mo {fmt(num(r.get('price_move_12m_pct')), pct=True)} | "
                 f"2yr {fmt(num(r.get('price_move_24m_pct')), pct=True)}")
        vies = r.get("value_inflection_events") or []
        if vies:
            L.append("- **Value-inflection events:**")
            for e in vies[:6]:
                ch = e.get("approx_change_pct")
                ch_s = f" ({ch:+.0f}%)" if isinstance(ch, (int, float)) else ""
                L.append(f"    - {e.get('date','—')}: {e.get('event','')}{ch_s}")
        if r.get("notes"):
            L.append(f"- **Note:** {r.get('notes')}")
        L.append("")

    OUT_PAGE.write_text("\n".join(L), encoding="utf-8")
    print(f"\nWrote {OUT_PAGE} ({n} deals)")


if __name__ == "__main__":
    if "--build" in sys.argv:
        build_page(load_cached())
    else:
        extract_all()
        build_page(load_cached())
