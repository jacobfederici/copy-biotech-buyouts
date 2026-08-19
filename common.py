#!/usr/bin/env python3
"""Shared utilities for the buyouts post-processing pipeline.

One source of truth for paths, env, LLM calls (cached), markdown-report
parsing, price-series math, and number formatting. Imported by
parse.py / analyze.py / dashboard.py / deck.py.
"""
import csv
import json
import os
import re
import time
import datetime as dt
from pathlib import Path

import requests
from dotenv import find_dotenv, load_dotenv

# --------------------------------------------------------------------------- #
# Paths & constants
# --------------------------------------------------------------------------- #
ROOT = Path(__file__).resolve().parent          # .../buyouts
REPORTS = ROOT / "reports"
DATA = ROOT / "data"                            # generated datasets + outputs
DEALS_JSON = DATA / "deals.json"
DEALS_CSV = DATA / "deals.csv"
PRICES_CSV = DATA / "prices.csv"
INFLECTIONS_CSV = DATA / "inflections.csv"
ROWS_JSON = DATA / "analysis_rows.json"
ANALYSIS_CSV = DATA / "analysis.csv"
ANALYSIS_MD = DATA / "analysis.md"
DASHBOARD_HTML = DATA / "dashboard.html"
ANALYSIS_HTML = DATA / "analysis.html"
DECKS = DATA / "decks"
LLM_CACHE = DATA / "llm_cache"

LLM_MODEL = "google/gemini-3-flash-preview"
_ENV_LOADED = False


def load_env():
    """Load .env once (repo root, with find_dotenv fallback)."""
    global _ENV_LOADED
    if not _ENV_LOADED:
        load_dotenv(ROOT.parent / ".env")
        load_dotenv(find_dotenv(), override=False)
        _ENV_LOADED = True


# --------------------------------------------------------------------------- #
# LLM (OpenRouter) — single wrapper + per-report JSON cache
# --------------------------------------------------------------------------- #
def call_llm(prompt, system=None, retries=4):
    """Call OpenRouter and return the parsed JSON object.

    Returns {"_error": ...} on failure rather than raising, so a single bad
    report never aborts a batch run.
    """
    load_env()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return {"_error": "OPENROUTER_API_KEY not set"}
    messages = ([{"role": "system", "content": system}] if system else []) + \
               [{"role": "user", "content": prompt}]
    payload = {"model": LLM_MODEL, "messages": messages,
               "temperature": 0.0, "response_format": {"type": "json_object"}}
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    for attempt in range(retries):
        try:
            r = requests.post("https://openrouter.ai/api/v1/chat/completions",
                              headers=headers, json=payload, timeout=120)
            if r.status_code == 200:
                content = r.json()["choices"][0]["message"]["content"]
                content = re.sub(r"^```(?:json)?|```$", "", content.strip(), flags=re.M).strip()
                return json.loads(content)
            if r.status_code == 429:
                time.sleep(12)
                continue
            if attempt == retries - 1:
                return {"_error": f"HTTP {r.status_code}"}
            time.sleep(5)
        except json.JSONDecodeError as e:
            if attempt == retries - 1:
                return {"_error": f"bad json: {e}"}
            time.sleep(2)
        except Exception as e:  # noqa: BLE001
            if attempt == retries - 1:
                return {"_error": str(e)}
            time.sleep(4)
    return {"_error": "failed"}


def llm_json_cached(prompt, cache_key, system=None, use_llm=True):
    """Cached LLM JSON extraction. Cache is one file per key in DATA/llm_cache/."""
    fp = LLM_CACHE / f"{cache_key}.json"
    if fp.exists():
        try:
            return json.loads(fp.read_text())
        except Exception:
            pass
    if not use_llm:
        return {}
    data = call_llm(prompt, system=system)
    if "_error" not in data:
        LLM_CACHE.mkdir(parents=True, exist_ok=True)
        fp.write_text(json.dumps(data))
    return data


# --------------------------------------------------------------------------- #
# Markdown-report parsing
# --------------------------------------------------------------------------- #
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
MONEY_RE = re.compile(r"[\$€£]?\s*([0-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]+)?)")


def first_date(s):
    """First date in a string, accepting ISO or 'October 10, 2021' forms."""
    if not s:
        return None
    m = DATE_RE.search(s)
    if m:
        try:
            return dt.date.fromisoformat(m.group(1))
        except ValueError:
            return None
    m = re.search(r"([A-Z][a-z]+ \d{1,2}, \d{4})", s)
    if m:
        for fmt in ("%B %d, %Y", "%b %d, %Y"):
            try:
                return dt.datetime.strptime(m.group(1), fmt).date()
            except ValueError:
                pass
    return None


def first_money(s):
    if not s:
        return None
    m = MONEY_RE.search(s)
    if not m:
        return None
    try:
        return float(m.group(1).replace(",", ""))
    except ValueError:
        return None


def num(s):
    """Loose numeric parse of a cell ('$1,234.5' -> 1234.5)."""
    if s is None:
        return None
    s = s.replace(",", "").replace("$", "").strip()
    m = re.search(r"-?\d+(?:\.\d+)?", s)
    return float(m.group(0)) if m else None


def get_field(text, name):
    """Value of a '- <name>: <value>' metadata line."""
    m = re.search(rf"^- {re.escape(name)}:\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else None


def section(text, header):
    """Body of a '## <header>' section, up to the next '## ' or EOF."""
    m = re.search(rf"^## {re.escape(header)}\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def parse_table_rows(block):
    """Cell lists for each pipe-table data row (skips header/separator rows)."""
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells:
            continue
        if set("".join(cells).replace(" ", "")) <= set("-:"):  # separator
            continue
        rows.append(cells)
    return rows


# --------------------------------------------------------------------------- #
# Price-series math (operates on the parsed prices.csv dataset)
# --------------------------------------------------------------------------- #
def load_prices():
    """file -> list of (date, close) ascending, using adj_close when present."""
    series = {}
    if not PRICES_CSV.exists():
        return series
    with open(PRICES_CSV) as f:
        for r in csv.DictReader(f):
            wk = first_date(r["week_ended"])
            c = r.get("adj_close") or r.get("close")
            if wk and c:
                try:
                    series.setdefault(r["file"], []).append((wk, float(c)))
                except ValueError:
                    pass
    for k in series:
        series[k].sort()
    return series


def close_on_or_before(series, target):
    """Latest close at or before target date, or None."""
    cand = [c for d, c in series if d <= target]
    return cand[-1] if cand else None


def trailing_move(series, end_date, months):
    """Return over the `months` window ending at end_date.

    If the window start predates the ~2yr series, fall back to the earliest
    close when it still covers >=80% of the window.
    """
    if not series or not end_date:
        return None
    end = close_on_or_before(series, end_date)
    if not end:
        return None
    start = close_on_or_before(series, end_date - dt.timedelta(days=round(30.44 * months)))
    if start is None:
        first_d, first_c = series[0]
        if first_d <= end_date - dt.timedelta(days=round(30.44 * months * 0.8)):
            start = first_c
    if end and start and start > 0:
        return round(end / start - 1, 4)
    return None


# --------------------------------------------------------------------------- #
# Formatting
# --------------------------------------------------------------------------- #
def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def fmt_pct(v, signed=False):
    """Fraction -> percent string (0.44 -> '44%' / '+44%'). '—' if not numeric."""
    v = fnum(v)
    if v is None:
        return "—"
    return f"{v * 100:+.0f}%" if signed else f"{v * 100:.0f}%"


def fmt_num(v, prefix="$"):
    v = fnum(v)
    return f"{prefix}{v:,.2f}" if v is not None else "—"


def fmt_size(v):
    """Equity value in $M -> '$1.2B' / '$340M'."""
    v = fnum(v)
    if not v:
        return "—"
    return f"${v / 1000:.1f}B" if v >= 1000 else f"${v:,.0f}M"
