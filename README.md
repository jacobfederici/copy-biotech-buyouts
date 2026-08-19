# Buyouts — Acquisition Analysis Pipeline

Turns the finished SC 14D-9 buyout reports in `reports/` into a structured
cross-deal dataset, two interactive HTML views, and per-company PowerPoint decks.

The extraction phase is complete: `reports/*.md` are the fixed inputs. Everything
under `data/` is regenerated from them by the four scripts below.

## Layout

```
buyouts/
├── common.py      # shared lib: paths, env, LLM+cache, report parsing, prices, formatting
├── parse.py       # reports/*.md          → data/{deals,prices,inflections}
├── analyze.py     # dataset + reports+LLM → data/{analysis_rows.json, analysis.csv, analysis.md}
├── dashboard.py   # dataset / rows        → data/{dashboard.html, analysis.html}
├── deck.py        # dataset               → data/decks/<TICKER>.pptx
├── reports/       # FINAL report per company (inputs)
└── data/          # generated datasets, HTML, decks/, llm_cache/
```

## Run (from the repo root)

```bash
.venv/bin/python buyouts/parse.py        # 1. reports → datasets
.venv/bin/python buyouts/analyze.py      # 2. + LLM extraction (cached) → rows/csv/md
.venv/bin/python buyouts/dashboard.py    # 3. → dashboard.html + analysis.html
.venv/bin/python buyouts/deck.py --all   # 4. → decks/*.pptx  (or pass tickers: deck.py LOXO ICGN)
```

`analyze.py` calls an LLM (OpenRouter, `google/gemini-3-flash-preview`) once per
report and caches each result in `data/llm_cache/`, so reruns are free. Requires
`OPENROUTER_API_KEY` in the repo-root `.env`. Flags: `--no-llm` (cache only),
or pass tickers to limit (`analyze.py LOXO`).

## Datasets (`data/`)

| File | Grain | Notes |
|---|---|---|
| `deals.csv` / `deals.json` | one row per deal | acquirer (merger-sub shells resolved to parent), premium, run-up, % premium pre-captured, timing, `data_quality` |
| `prices.csv` | one row per deal-week | OHLCV + `adj_close` (contemporaneous weekly close) |
| `inflections.csv` | one flagged price move | `week_ended`, `trigger`, `change_pct`, `identified` |
| `analysis_rows.json` / `analysis.csv` / `analysis.md` | one row per deal | deterministic metrics + LLM fields (stage, value-inflection events, bid range, parties, direction, early leak) |

`data_quality` is `ok`, or `suspect_feed` when the price feed is intrinsically
impossible (close > $1500/sh, or sub-cent print on a >$1 deal) — those deals are
dropped from premium/run-up math and skipped by `deck.py`.

## Deck anatomy (5 slides per company)

1. **Deal snapshot** — acquirer, deal price, premium, 4-wk run-up, % premium captured pre-announcement, dates, status.
2. **Stock price, events & rumors** — native editable line chart of the weekly close with the most material inflections marked: **red = rumor/leak**, **teal = event**, **gold = deal announcement**. Rumor/event markers sit one week before the reported move week (weekly data can lag the true move); the deal marker stays on the announcement week.
3. **Interaction timeline** — native shape diagram (dot per milestone, teal before / gold after announcement) + the complete dated list, paginated. Dates render at the precision the filing states (`Mar 05, 2019` / `Aug 2021` / `2018`).
4. **The rumors** — unexplained pre-announcement inflection weeks (the announcement-week reaction is classified as the deal, not a rumor).
5. **The events** — disclosed catalysts from Company News, tagged Deal / Regulatory / Clinical / Partnership / Financing.

Inflection classification (`deck.py` → `classify_inflections`): **deal** = within
−3…+10 days of announcement; **rumor** = trigger "not identified" and no
catalyst-keyword news within ±12 days; **event** = otherwise.

## Refresh after reports change

Re-run `parse.py`, then `analyze.py`, `dashboard.py`, `deck.py --all`. Everything
regenerates deterministically from the Markdown reports (LLM fields served from
cache unless a report's text changed).
