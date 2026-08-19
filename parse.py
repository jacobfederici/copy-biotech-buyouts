#!/usr/bin/env python3
"""Parse all SC 14D9 buyout reports into the structured cross-deal dataset.

    .venv/bin/python buyouts/parse.py

Reads:  buyouts/reports/*.md
Writes: buyouts/data/{deals.csv, deals.json, prices.csv, inflections.csv}
"""
import csv
import json
import re
import datetime as dt
import statistics as st
from pathlib import Path

from common import (DATA, REPORTS, DEALS_CSV, DEALS_JSON, PRICES_CSV, INFLECTIONS_CSV,
                    first_date, first_money, get_field, section, parse_table_rows, num)

# Web-verified per-ticker corrections for deals whose price-feed-derived premium
# is wrong (foreign-ADR currency mismatch, or a bad feed print). See overrides.json.
OVERRIDES_PATH = Path(__file__).resolve().parent / "overrides.json"
OVERRIDES = {k: v for k, v in json.loads(OVERRIDES_PATH.read_text()).items()
             if not k.startswith("_")} if OVERRIDES_PATH.exists() else {}
# fields an override is allowed to replace on the computed deal row
OVERRIDE_FIELDS = ("currency", "unaffected_close", "last_pre_close",
                   "premium_to_unaffected", "premium_to_last",
                   "runup_4wk_pct", "pct_premium_pre_captured")

# merger-sub / shell-entity name patterns (so we resolve to the real parent)
SUB_RE = re.compile(r"\b(merger sub|acquisition (corp|corporation|company|sub)|"
                    r"bidco|holdco|purchaser|merger co|sub,?\s*inc|parent,?\s*inc|"
                    r"parent)\b", re.I)


def parse_prices(text):
    block = section(text, "Stock Price Over Time")
    out = []
    for cells in parse_table_rows(block):
        # Week ended | Open | High | Low | Close | Volume | Shares out | ... | Market cap | src
        if len(cells) < 6:
            continue
        wk = first_date(cells[0])
        if not wk:
            continue
        out.append({
            "week_ended": wk,
            "open": num(cells[1]), "high": num(cells[2]),
            "low": num(cells[3]), "close": num(cells[4]),
            "volume": num(cells[5]),
            "shares_out": num(cells[6]) if len(cells) > 6 else None,
            "market_cap": num(cells[8]) if len(cells) > 8 else None,
        })
    out.sort(key=lambda r: r["week_ended"])
    return out


def parse_economics(text):
    block = section(text, "Offer Economics")
    upfront = maxval = shares = None
    for cells in parse_table_rows(block):
        if len(cells) < 2:
            continue
        metric, val = cells[0].lower(), cells[1]
        if "upfront cash per" in metric or ("per common share" in metric and upfront is None):
            upfront = first_money(val)
        elif "maximum per-share" in metric:
            maxval = first_money(val)
        elif "shares outstanding" in metric:
            shares = num(val)
    return upfront, maxval, shares


def parse_inflections(text, fname):
    block = section(text, "Value Inflection Points")
    out = []
    for cells in parse_table_rows(block):
        if len(cells) < 6:
            continue
        wk = first_date(cells[0])
        trigger = cells[1]
        out.append({
            "file": fname,
            "week_ended": wk.isoformat() if wk else "",
            "trigger": trigger,
            "source": cells[2],
            "pre_close": num(cells[3]),
            "post_close": num(cells[4]),
            "change_pct": num(cells[5].replace("%", "")),
            "identified": "not identified" not in trigger.lower(),
        })
    return out


def clean_prices(prices, deal_price=None):
    """Use contemporaneous closes (adj_close = raw close) and flag broken feeds.

    Weekly closes are split-correct on their own date — the basis the premium
    needs. We do NOT synthesize reverse-split adjustments from noisy SEC
    shares_out. A feed is 'suspect' only when intrinsically impossible: a close
    above $1500/share, or a sub-cent print on a stock with a real (>$1) deal
    price.
    """
    adj = [dict(p, adj_close=p["close"]) for p in prices]
    suspect = False
    closes = [p["adj_close"] for p in adj if p["adj_close"] is not None]
    if closes:
        if max(closes) > 1500:
            suspect = True
        elif min(closes) < 0.02 and (deal_price or 0) > 1:
            suspect = True
    return adj, suspect


def nearest_close_on_or_before(prices, target):
    cand = [p for p in prices if p["week_ended"] <= target and p["adj_close"]]
    return cand[-1] if cand else None


def leak_signal(prices, ann_date, deal_price):
    """Run-up / volume / premium-capture around the announcement (on adj_close)."""
    res = {k: None for k in (
        "unaffected_close", "last_pre_close", "premium_to_unaffected",
        "premium_to_last", "runup_4wk_pct", "pct_premium_pre_captured",
        "vol_ratio_4wk", "n_price_weeks")}
    res["n_price_weeks"] = len(prices)
    if not ann_date or not prices:
        return res
    pre = [p for p in prices if p["week_ended"] < ann_date and p["adj_close"]]
    if not pre:
        return res
    last_pre = pre[-1]
    res["last_pre_close"] = round(last_pre["adj_close"], 4)
    unaff = nearest_close_on_or_before(prices, ann_date - dt.timedelta(days=28))
    if unaff:
        uc = unaff["adj_close"]
        res["unaffected_close"] = round(uc, 4)
        if deal_price and uc:
            res["premium_to_unaffected"] = round(deal_price / uc - 1, 4)
        if last_pre["adj_close"] and uc:
            res["runup_4wk_pct"] = round(last_pre["adj_close"] / uc - 1, 4)
        if deal_price and uc and (deal_price - uc):
            res["pct_premium_pre_captured"] = round(
                (last_pre["adj_close"] - uc) / (deal_price - uc), 4)
    if deal_price and last_pre["adj_close"]:
        res["premium_to_last"] = round(deal_price / last_pre["adj_close"] - 1, 4)
    win = [p for p in pre if p["week_ended"] >= ann_date - dt.timedelta(days=28) and p["volume"]]
    base = [p for p in pre if ann_date - dt.timedelta(days=84) <= p["week_ended"]
            < ann_date - dt.timedelta(days=28) and p["volume"]]
    if win and base:
        bw = sum(p["volume"] for p in base) / len(base)
        ww = sum(p["volume"] for p in win) / len(win)
        if bw:
            res["vol_ratio_4wk"] = round(ww / bw, 2)
    return res


def days_between(a, b):
    return (b - a).days if a and b else None


def main():
    DATA.mkdir(parents=True, exist_ok=True)
    deals, all_prices, all_infl = [], [], []
    for fp in sorted(p for p in REPORTS.glob("*.md") if p.name != "README.md"):
        text = fp.read_text(encoding="utf-8", errors="replace")
        if not text.lstrip().startswith("#") or "## Stock Price Over Time" not in text:
            continue
        fname = fp.name
        ann = first_date(get_field(text, "Announcement date"))
        close_d = first_date(get_field(text, "Close date"))
        tender_d = first_date(get_field(text, "Tender expiration date"))
        board_d = first_date(get_field(text, "Board recommendation date"))
        upfront, maxval, shares_econ = parse_economics(text)
        deal_price = upfront or first_money(get_field(text, "Per-share consideration"))
        adj, suspect = clean_prices(parse_prices(text), deal_price)
        leak = leak_signal(adj, ann, deal_price)
        data_quality = "suspect_feed" if suspect else "ok"
        if suspect:  # price-derived metrics unreliable; drop them
            for k in ("unaffected_close", "last_pre_close", "premium_to_unaffected",
                      "premium_to_last", "runup_4wk_pct", "pct_premium_pre_captured",
                      "vol_ratio_4wk"):
                leak[k] = None
        has_cvr = bool(re.search(r"\bCVR\b|contingent value", text)) and (
            (maxval or 0) > (upfront or 0) or "cvr" in (get_field(text, "Payment type") or "").lower())
        # resolve true acquirer: whichever of Parent/Buyer is NOT a shell entity
        buyer = get_field(text, "Buyer")
        parent = get_field(text, "Parent")
        cands = [c for c in (parent, buyer) if c]
        clean = [c for c in cands if not SUB_RE.search(c)]
        acquirer = clean[0] if clean else (cands[0] if cands else None)

        row = {
            "file": fname,
            "company": text.splitlines()[0].lstrip("# ").strip(),
            "ticker": get_field(text, "Ticker"),
            "cik": get_field(text, "CIK"),
            "status": get_field(text, "Status"),
            "buyer": buyer,
            "acquirer": acquirer,
            "data_quality": data_quality,
            "deal_type": get_field(text, "Deal type"),
            "payment_type": get_field(text, "Payment type"),
            "announcement_date": ann.isoformat() if ann else "",
            "board_rec_date": board_d.isoformat() if board_d else "",
            "tender_exp_date": tender_d.isoformat() if tender_d else "",
            "close_date": close_d.isoformat() if close_d else "",
            "ann_year": ann.year if ann else "",
            "per_share_upfront": deal_price,
            "max_per_share_cvr": maxval,
            "has_cvr": has_cvr,
            "shares_out": shares_econ,
            "implied_equity_value_m": round(deal_price * shares_econ / 1e6, 1)
                if deal_price and shares_econ else None,
            "ann_to_close_days": days_between(ann, close_d),
            "ann_to_tender_days": days_between(ann, tender_d),
            "currency": "USD",
            "premium_override": False,
            "override_source": "",
            **leak,
        }
        ov = OVERRIDES.get(row["ticker"])
        if ov:
            for k in OVERRIDE_FIELDS:
                if k in ov:
                    row[k] = ov[k]
            row["premium_override"] = True
            row["override_source"] = ov.get("source", "")
        deals.append(row)
        for p in adj:
            all_prices.append({"file": fname, "ticker": row["ticker"],
                               "week_ended": p["week_ended"].isoformat(),
                               **{k: p[k] for k in ("open", "high", "low", "close", "volume",
                                                    "shares_out", "market_cap")},
                               "adj_close": round(p["adj_close"], 4) if p["adj_close"] else None})
        all_infl.extend(parse_inflections(text, fname))

    with open(DEALS_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(deals[0].keys()))
        w.writeheader()
        w.writerows(deals)
    DEALS_JSON.write_text(json.dumps(deals, indent=0, default=str))
    with open(PRICES_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_prices[0].keys()))
        w.writeheader()
        w.writerows(all_prices)
    with open(INFLECTIONS_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_infl[0].keys()))
        w.writeheader()
        w.writerows(all_infl)

    n = len(deals)
    print(f"Parsed {n} deals, {len(all_prices)} weekly price rows, {len(all_infl)} inflection events")
    dq = {}
    for d in deals:
        dq[d["data_quality"]] = dq.get(d["data_quality"], 0) + 1
    print(f"  data quality: {dq}")

    def med(key):
        v = [d[key] for d in deals if isinstance(d[key], (int, float))]
        return (round(st.median(v), 3), len(v)) if v else (None, 0)
    for label, key in (("premium-to-unaffected (4wk pre)", "premium_to_unaffected"),
                       ("premium-to-last-close", "premium_to_last"),
                       ("4-week pre-ann run-up", "runup_4wk_pct"),
                       ("% of premium captured pre-ann", "pct_premium_pre_captured")):
        m, c = med(key)
        print(f"  median {label}: {m}  (n={c})")


if __name__ == "__main__":
    main()
