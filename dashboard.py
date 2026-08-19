#!/usr/bin/env python3
"""Render the two interactive HTML pages from the parsed dataset.

    .venv/bin/python buyouts/dashboard.py

Reads:  buyouts/data/{deals.json, prices.csv, analysis_rows.json}
Writes: buyouts/data/dashboard.html  (leak signal & premiums, from deals+prices)
        buyouts/data/analysis.html   (sortable deal table, from analysis_rows)
"""
import csv
import json
import statistics as st
import datetime as dt

from common import (DEALS_JSON, PRICES_CSV, ROWS_JSON, DASHBOARD_HTML, ANALYSIS_HTML)


def _date(s):
    try:
        return dt.date.fromisoformat(s)
    except Exception:
        return None


def _pct(xs, p):
    if not xs:
        return None
    xs = sorted(xs)
    k = (len(xs) - 1) * p
    lo = int(k)
    return xs[lo] if lo == k else xs[lo] + (xs[lo + 1] - xs[lo]) * (k - lo)


# --------------------------------------------------------------------------- #
# dashboard.html — leak signal & premiums
# --------------------------------------------------------------------------- #
def build_dashboard():
    deals = json.loads(DEALS_JSON.read_text())
    prices = {}
    with open(PRICES_CSV) as f:
        for r in csv.DictReader(f):
            prices.setdefault(r["file"], []).append(r)

    # aligned run-up panel: normalize each deal's close to unaffected(-4wk)=100
    WEEKS = list(range(-12, 2))
    buckets = {w: [] for w in WEEKS}
    for d in deals:
        if d.get("data_quality") == "suspect_feed":
            continue
        ann, unaff = _date(d["announcement_date"]), d.get("unaffected_close")
        if not ann or not unaff:
            continue
        rows = sorted((r for r in prices.get(d["file"], []) if r.get("adj_close")),
                      key=lambda r: r["week_ended"])
        for r in rows:
            wk = _date(r["week_ended"])
            if not wk:
                continue
            offset = round((wk - ann).days / 7)
            if offset in buckets:
                try:
                    buckets[offset].append(float(r["adj_close"]) / unaff * 100)
                except Exception:
                    pass
    runup_panel = [{
        "week": w,
        "median": round(st.median(buckets[w]), 1) if buckets[w] else None,
        "p25": round(_pct(buckets[w], .25), 1) if buckets[w] else None,
        "p75": round(_pct(buckets[w], .75), 1) if buckets[w] else None,
        "n": len(buckets[w]),
    } for w in WEEKS]

    by_year = {}
    for d in deals:
        y, p = d.get("ann_year"), d.get("premium_to_unaffected")
        if isinstance(y, int) and isinstance(p, (int, float)):
            by_year.setdefault(y, []).append(p)
    year_panel = [{"year": y, "median": round(st.median(v), 3), "n": len(v)}
                  for y, v in sorted(by_year.items())]

    DATA = json.dumps({"deals": deals, "runup_panel": runup_panel,
                       "year_panel": year_panel}, default=str)
    nsuspect = sum(1 for d in deals if d.get("data_quality") == "suspect_feed")
    html = (DASHBOARD_TMPL.replace("__DATA__", DATA)
            .replace("__NDEALS__", str(len(deals)))
            .replace("__NSUSPECT__", str(nsuspect)))
    DASHBOARD_HTML.write_text(html)
    print(f"Wrote dashboard.html ({len(html)//1024} KB) covering {len(deals)} deals")


# --------------------------------------------------------------------------- #
# analysis.html — sortable comprehensive deal table
# --------------------------------------------------------------------------- #
def build_analysis_page():
    rows = json.loads(ROWS_JSON.read_text())
    ANALYSIS_HTML.write_text(ANALYSIS_TMPL.replace("__DATA__", json.dumps(rows)))
    print(f"Wrote analysis.html with {len(rows)} deals")


DASHBOARD_TMPL = """<!doctype html><html lang=en><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>Biotech Buyout Atlas — Leak Signal & Premiums</title>
<style>
:root{--bg:#0c1015;--panel:#151b24;--panel2:#1b2430;--ink:#e8eef5;--mut:#8aa0b8;
--line:#26303d;--accent:#46b3ff;--hot:#ff5d6c;--warm:#ffb454;--good:#37d79a;}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:28px 20px 80px}
h1{font-size:26px;margin:0 0 4px}h2{font-size:16px;margin:0 0 14px;font-weight:600}
.sub{color:var(--mut);margin:0 0 24px;font-size:13px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin-bottom:26px}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px}
.kpi .v{font-size:27px;font-weight:700;letter-spacing:-.5px}
.kpi .l{color:var(--mut);font-size:12px;margin-top:3px}
.kpi .v.hot{color:var(--hot)}.kpi .v.good{color:var(--good)}.kpi .v.warm{color:var(--warm)}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin-bottom:20px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media(max-width:820px){.grid2{grid-template-columns:1fr}}
.note{color:var(--mut);font-size:12px;margin-top:10px}
svg{width:100%;height:auto;display:block;overflow:visible}
.axis{stroke:var(--line)}.axt{fill:var(--mut);font-size:11px}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{padding:7px 9px;text-align:right;border-bottom:1px solid var(--line);white-space:nowrap}
th:first-child,td:first-child{text-align:left}
th{color:var(--mut);font-weight:600;cursor:pointer;user-select:none}
th:hover{color:var(--ink)}tbody tr:hover{background:var(--panel2)}
.scroll{overflow-x:auto}
.tag{display:inline-block;padding:1px 7px;border-radius:20px;font-size:11px;background:var(--panel2);color:var(--mut)}
.pill{font-size:11px;color:var(--mut)}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:12px;color:var(--mut);margin-top:8px}
.dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px;vertical-align:middle}
a{color:var(--accent);text-decoration:none}
input[type=search]{background:var(--panel2);border:1px solid var(--line);color:var(--ink);
border-radius:8px;padding:7px 10px;width:240px;font-size:13px}
</style></head><body><div class=wrap>
<h1>Biotech Buyout Atlas</h1>
<p class=sub id=sub>Pre-announcement leak signal &amp; takeout premiums across SC&nbsp;14D-9 deals</p>
<div class=kpis id=kpis></div>

<div class=card>
<h2>The "blinded data" drift — price run-up before the deal is public</h2>
<div id=runup></div>
<div class=legend>
<span><span class=dot style=background:var(--accent)></span>Median close (deals normalized to unaffected price = 100, 4 wks before announcement)</span>
<span><span class=dot style=background:var(--line)></span>25th–75th percentile band</span></div>
<p class=note>Each deal's weekly close is rebased to 100 at 4 weeks before its announcement, then aligned by weeks-to-announcement and pooled. A rising median in the weeks <em>before</em> week 0 is the systematic leak/rumor footprint. The vertical line marks the announcement.</p>
</div>

<div class=grid2>
<div class=card>
<h2>Leak scatter — run-up vs. total premium</h2>
<div id=scatter></div>
<div class=legend>
<span><span class=dot style=background:var(--hot)></span>incl. CVR</span>
<span><span class=dot style=background:var(--accent)></span>cash-only</span>
<span class=pill>x: 4-wk pre-announcement run-up &nbsp;·&nbsp; y: premium to unaffected &nbsp;·&nbsp; size: deal value</span></div>
<p class=note>Deals far to the right gave away a large slice of the premium before the announcement. The diagonal-ish band = the part the market "front-ran."</p>
</div>
<div class=card>
<h2>How much premium was captured before announcement?</h2>
<div id=hist></div>
<p class=note>Share of each deal's total premium already in the price the week before it went public. Mass to the right = the market increasingly "knew."</p>
</div>
</div>

<div class=grid2>
<div class=card><h2>Median premium by announcement year</h2><div id=byyear></div>
<p class=note>Median premium-to-unaffected price; label shows deal count.</p></div>
<div class=card><h2>Time from announcement to close</h2><div id=timing></div>
<p class=note>Calendar days, announcement → merger close (tender-offer deals close fast).</p></div>
</div>

<div class=card>
<h2>Leakiest deals — largest pre-announcement run-up &amp; volume</h2>
<input type=search id=q placeholder="filter by company / ticker / buyer…">
<div class=scroll style=margin-top:12px><table id=tbl><thead><tr>
<th data-k=company>Company</th><th data-k=ticker>Tkr</th><th data-k=announcement_date>Announced</th>
<th data-k=acquirer>Acquirer</th><th data-k=runup_4wk_pct>Run-up 4wk</th>
<th data-k=vol_ratio_4wk>Vol ×</th><th data-k=pct_premium_pre_captured>% prem pre</th>
<th data-k=premium_to_unaffected>Premium</th><th data-k=per_share_upfront>$/sh</th>
</tr></thead><tbody></tbody></table></div>
<p class=note>Sortable. "% prem pre" = fraction of the takeout premium already captured before announcement. "Vol ×" = avg volume in the 4 weeks pre-announcement vs. the prior 4-week baseline.</p>
</div>

<p class=note>Source: __NDEALS__ parsed SC 14D-9 buyout reports. Unaffected price = split-adjusted weekly close ~4 weeks before announcement. Acquirer resolved from the filing's parent/buyer (merger-sub shells mapped to the real parent). <strong>__NSUSPECT__ deals with corrupted price feeds are excluded</strong> from all run-up/premium calculations. Generated by dashboard.py.</p>
</div>
<script>
const D=__DATA__;const $=s=>document.querySelector(s);
const fmtpct=x=>x==null?"—":(x*100).toFixed(0)+"%";
const med=a=>{a=a.filter(x=>typeof x==="number").sort((x,y)=>x-y);if(!a.length)return null;
const m=Math.floor(a.length/2);return a.length%2?a[m]:(a[m-1]+a[m])/2;};
const deals=D.deals;
// KPIs
const ru=deals.map(d=>d.runup_4wk_pct), pu=deals.map(d=>d.premium_to_unaffected),
  cap=deals.map(d=>d.pct_premium_pre_captured);
const leaky=deals.filter(d=>typeof d.runup_4wk_pct==="number"&&d.runup_4wk_pct>0.15).length;
const cvr=deals.filter(d=>d.has_cvr===true||d.has_cvr==="True").length;
const kpis=[
 ["Deals analyzed",deals.length,""],
 ["Median premium",fmtpct(med(pu)),"good"],
 ["Median premium captured pre-ann.",fmtpct(med(cap)),"warm"],
 ["Deals w/ >15% pre-ann run-up",leaky+" ("+Math.round(leaky/deals.length*100)+"%)","hot"],
 ["Median 4-wk run-up",fmtpct(med(ru)),"warm"],
 ["Deals incl. CVR",cvr,""],
];
$("#kpis").innerHTML=kpis.map(k=>`<div class=kpi><div class="v ${k[2]}">${k[1]}</div><div class=l>${k[0]}</div></div>`).join("");
$("#sub").textContent="Pre-announcement leak signal & takeout premiums across "+deals.length+" SC 14D-9 deals";

function svg(w,h){const s=document.createElementNS("http://www.w3.org/2000/svg","svg");
 s.setAttribute("viewBox",`0 0 ${w} ${h}`);return s;}
function el(p,n,a){const e=document.createElementNS("http://www.w3.org/2000/svg",n);
 for(const k in a)e.setAttribute(k,a[k]);p.appendChild(e);return e;}

// ---- run-up panel ----
(function(){const P=D.runup_panel.filter(d=>d.median!=null);
 const W=720,H=300,L=46,R=16,T=14,B=34;const xs=P.map(d=>d.week);
 const xmin=Math.min(...xs),xmax=Math.max(...xs);
 const ys=P.flatMap(d=>[d.p25,d.p75,d.median]);const ymin=Math.min(...ys)-2,ymax=Math.max(...ys)+2;
 const X=w=>L+(w-xmin)/(xmax-xmin)*(W-L-R);const Y=v=>T+(1-(v-ymin)/(ymax-ymin))*(H-T-B);
 const s=svg(W,H);$("#runup").appendChild(s);
 const step=Math.ceil((ymax-ymin)/5/5)*5||5;
 for(let v=Math.ceil(ymin/step)*step;v<=ymax;v+=step){el(s,"line",{x1:L,x2:W-R,y1:Y(v),y2:Y(v),class:"axis"});
  el(s,"text",{x:L-6,y:Y(v)+3,class:"axt","text-anchor":"end"}).textContent=v;}
 el(s,"line",{x1:X(0),x2:X(0),y1:T,y2:H-B,stroke:"var(--hot)","stroke-dasharray":"4 3","stroke-width":1.3});
 el(s,"text",{x:X(0)+4,y:T+10,class:"axt",fill:"var(--hot)"}).textContent="announcement";
 let up=P.map(d=>`${X(d.week)},${Y(d.p75)}`).join(" ");
 let dn=P.slice().reverse().map(d=>`${X(d.week)},${Y(d.p25)}`).join(" ");
 el(s,"polygon",{points:up+" "+dn,fill:"var(--accent)","fill-opacity":.12,stroke:"none"});
 el(s,"polyline",{points:P.map(d=>`${X(d.week)},${Y(d.median)}`).join(" "),fill:"none",
  stroke:"var(--accent)","stroke-width":2.2});
 P.forEach(d=>el(s,"circle",{cx:X(d.week),cy:Y(d.median),r:2.6,fill:"var(--accent)"}));
 xs.forEach(w=>{if(w%2===0)el(s,"text",{x:X(w),y:H-B+16,class:"axt","text-anchor":"middle"}).textContent=w;});
 el(s,"text",{x:(L+W-R)/2,y:H-2,class:"axt","text-anchor":"middle"}).textContent="weeks relative to announcement";
})();

// ---- scatter ----
(function(){const pts=deals.filter(d=>typeof d.runup_4wk_pct==="number"&&typeof d.premium_to_unaffected==="number"
  &&d.premium_to_unaffected<4&&d.runup_4wk_pct>-.3&&d.runup_4wk_pct<1.2);
 const W=520,H=320,L=48,R=14,T=12,B=40;
 const X=v=>L+(v+.3)/(1.2+.3)*(W-L-R);const Y=v=>T+(1-v/3)*(H-T-B);
 const s=svg(W,H);$("#scatter").appendChild(s);
 [0,.25,.5,.75,1].forEach(v=>{el(s,"line",{x1:X(v),x2:X(v),y1:T,y2:H-B,class:"axis"});
  el(s,"text",{x:X(v),y:H-B+16,class:"axt","text-anchor":"middle"}).textContent=(v*100)+"%";});
 [0,1,2,3].forEach(v=>{el(s,"line",{x1:L,x2:W-R,y1:Y(v),y2:Y(v),class:"axis"});
  el(s,"text",{x:L-6,y:Y(v)+3,class:"axt","text-anchor":"end"}).textContent=(v*100)+"%";});
 const sz=v=>{const m=Math.sqrt((v||200)/1000);return Math.max(2.5,Math.min(11,m));};
 pts.forEach(d=>{const isc=d.has_cvr===true||d.has_cvr==="True";
  const c=el(s,"circle",{cx:X(d.runup_4wk_pct),cy:Y(Math.min(d.premium_to_unaffected,3)),
   r:sz(d.implied_equity_value_m),fill:isc?"var(--hot)":"var(--accent)","fill-opacity":.42,
   stroke:isc?"var(--hot)":"var(--accent)","stroke-opacity":.7});
  el(c,"title").textContent=`${d.company} (${d.ticker})\\n4wk run-up ${fmtpct(d.runup_4wk_pct)} · premium ${fmtpct(d.premium_to_unaffected)}`;});
 el(s,"text",{x:(L+W-R)/2,y:H-3,class:"axt","text-anchor":"middle"}).textContent="4-wk pre-announcement run-up";
})();

// ---- histogram of % premium captured pre ----
(function(){const xs=deals.map(d=>d.pct_premium_pre_captured).filter(x=>typeof x==="number"&&x>=-.2&&x<=1.2);
 const bins=14,lo=-.1,hi=1.0,bw=(hi-lo)/bins;const h=new Array(bins).fill(0);
 xs.forEach(v=>{let i=Math.floor((v-lo)/bw);i=Math.max(0,Math.min(bins-1,i));h[i]++;});
 const W=520,H=320,L=40,R=14,T=12,B=40;const mx=Math.max(...h);
 const s=svg(W,H);$("#hist").appendChild(s);
 [0,.25,.5,.75,1].forEach(v=>el(s,"text",{x:L+(v-lo)/(hi-lo)*(W-L-R),y:H-B+16,class:"axt","text-anchor":"middle"}).textContent=(v*100)+"%");
 const bwid=(W-L-R)/bins;
 h.forEach((c,i)=>{const ph=c/mx*(H-T-B);
  el(s,"rect",{x:L+i*bwid+1,y:H-B-ph,width:bwid-2,height:ph,rx:2,
   fill:i>=Math.floor((0.3-lo)/bw)?"var(--warm)":"var(--accent)","fill-opacity":.8});});
 el(s,"line",{x1:L,x2:W-R,y1:H-B,y2:H-B,class:"axis"});
 el(s,"text",{x:(L+W-R)/2,y:H-3,class:"axt","text-anchor":"middle"}).textContent="% of premium captured before announcement";
})();

// ---- premium by year ----
(function(){const P=D.year_panel;const W=520,H=300,L=42,R=14,T=12,B=34;
 const yrs=P.map(d=>d.year);const xmin=Math.min(...yrs),xmax=Math.max(...yrs);
 const mx=Math.max(...P.map(d=>d.median));
 const X=y=>L+(y-xmin)/(xmax-xmin||1)*(W-L-R);const Y=v=>T+(1-v/(mx*1.1))*(H-T-B);
 const s=svg(W,H);$("#byyear").appendChild(s);
 [0,.5,1,1.5].filter(v=>v<=mx*1.1).forEach(v=>{el(s,"line",{x1:L,x2:W-R,y1:Y(v),y2:Y(v),class:"axis"});
  el(s,"text",{x:L-6,y:Y(v)+3,class:"axt","text-anchor":"end"}).textContent=(v*100)+"%";});
 el(s,"polyline",{points:P.map(d=>`${X(d.year)},${Y(d.median)}`).join(" "),fill:"none",stroke:"var(--good)","stroke-width":2});
 P.forEach(d=>{const c=el(s,"circle",{cx:X(d.year),cy:Y(d.median),r:3,fill:"var(--good)"});
  el(c,"title").textContent=`${d.year}: ${fmtpct(d.median)} (n=${d.n})`;});
 yrs.forEach(y=>{if(y%3===0)el(s,"text",{x:X(y),y:H-B+16,class:"axt","text-anchor":"middle"}).textContent=y;});
})();

// ---- timing hist ----
(function(){const xs=deals.map(d=>d.ann_to_close_days).filter(x=>typeof x==="number"&&x>0&&x<400);
 const bins=16,lo=0,hi=320,bw=(hi-lo)/bins;const h=new Array(bins).fill(0);
 xs.forEach(v=>{let i=Math.floor((v-lo)/bw);i=Math.max(0,Math.min(bins-1,i));h[i]++;});
 const W=520,H=300,L=36,R=14,T=12,B=34;const mx=Math.max(...h);const bwid=(W-L-R)/bins;
 const s=svg(W,H);$("#timing").appendChild(s);
 h.forEach((c,i)=>{const ph=c/mx*(H-T-B);el(s,"rect",{x:L+i*bwid+1,y:H-B-ph,width:bwid-2,height:ph,rx:2,fill:"var(--accent)","fill-opacity":.8});});
 [0,90,180,270].forEach(v=>el(s,"text",{x:L+(v-lo)/(hi-lo)*(W-L-R),y:H-B+16,class:"axt","text-anchor":"middle"}).textContent=v+"d");
 el(s,"line",{x1:L,x2:W-R,y1:H-B,y2:H-B,class:"axis"});
 el(s,"text",{x:(L+W-R)/2,y:H-3,class:"axt","text-anchor":"middle"}).textContent="days, announcement → close";
})();

// ---- table ----
let sortK="runup_4wk_pct",sortDir=-1;
function render(){const q=$("#q").value.toLowerCase();
 let rows=deals.filter(d=>d.data_quality!=="suspect_feed").filter(d=>!q||[d.company,d.ticker,d.acquirer].join(" ").toLowerCase().includes(q));
 rows.sort((a,b)=>{let x=a[sortK],y=b[sortK];
  if(typeof x==="number"&&typeof y==="number")return (x-y)*sortDir;
  return String(x||"").localeCompare(String(y||""))*sortDir;});
 const tb=$("#tbl tbody");tb.innerHTML=rows.slice(0,80).map(d=>`<tr>
  <td>${d.company.replace(/, Inc\\.?| Corp\\.?| Ltd\\.?| Co\\.?/g,"")}</td>
  <td><span class=tag>${d.ticker||""}</span></td>
  <td>${d.announcement_date||""}</td><td style="text-align:left;max-width:170px;overflow:hidden;text-overflow:ellipsis">${(d.acquirer||"").slice(0,30)}</td>
  <td style="color:${d.runup_4wk_pct>0.15?'var(--hot)':'inherit'}">${fmtpct(d.runup_4wk_pct)}</td>
  <td>${d.vol_ratio_4wk?d.vol_ratio_4wk.toFixed(1)+"×":"—"}</td>
  <td>${fmtpct(d.pct_premium_pre_captured)}</td>
  <td>${fmtpct(d.premium_to_unaffected)}</td>
  <td>${d.per_share_upfront!=null?"$"+d.per_share_upfront:"—"}</td></tr>`).join("");}
document.querySelectorAll("#tbl th").forEach(th=>th.onclick=()=>{
 const k=th.dataset.k;if(k===sortK)sortDir*=-1;else{sortK=k;sortDir=-1;}render();});
$("#q").oninput=render;render();
</script></body></html>"""


ANALYSIS_TMPL = """<!doctype html><html lang=en><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>Biotech Buyouts — Comprehensive Deal Analysis</title>
<style>
:root{--bg:#0c1015;--panel:#151b24;--p2:#1b2430;--ink:#e8eef5;--mut:#8aa0b8;
--line:#26303d;--accent:#46b3ff;--hot:#ff5d6c;--good:#37d79a;--warm:#ffb454;--violet:#b58cff;}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font:13px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:1700px;margin:0 auto;padding:22px 18px 80px}
h1{font-size:23px;margin:0 0 3px}.sub{color:var(--mut);margin:0 0 18px;font-size:13px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-bottom:18px}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 14px}
.kpi .v{font-size:22px;font-weight:700}.kpi .l{color:var(--mut);font-size:11px;margin-top:2px}
.bar{display:flex;gap:10px;align-items:center;margin-bottom:12px;flex-wrap:wrap}
input[type=search]{background:var(--p2);border:1px solid var(--line);color:var(--ink);
border-radius:8px;padding:8px 11px;width:280px;font-size:13px}
.chip{background:var(--p2);border:1px solid var(--line);color:var(--mut);border-radius:20px;
padding:5px 11px;font-size:12px;cursor:pointer;user-select:none}
.chip.on{background:var(--accent);color:#04121f;border-color:var(--accent);font-weight:600}
.scroll{overflow-x:auto;border:1px solid var(--line);border-radius:12px}
table{border-collapse:collapse;font-size:12px;width:100%;white-space:nowrap}
th,td{padding:7px 9px;border-bottom:1px solid var(--line);text-align:right}
th:nth-child(-n+2),td:nth-child(-n+2){text-align:left}
th{position:sticky;top:0;background:var(--panel);color:var(--mut);font-weight:600;
cursor:pointer;user-select:none;z-index:2}
th:hover{color:var(--ink)}
td:first-child,th:first-child{position:sticky;left:0;background:var(--panel);z-index:1}
tbody td:first-child{background:var(--bg)}
tbody tr:hover td{background:var(--p2)}
tbody tr:hover td:first-child{background:var(--p2)}
.tk{font-weight:700;color:var(--accent)}
.pos{color:var(--good)}.neg{color:var(--hot)}.muted{color:var(--mut)}
.tag{padding:1px 7px;border-radius:20px;font-size:11px;font-weight:600}
.in{background:rgba(70,179,255,.16);color:var(--accent)}
.out{background:rgba(255,180,84,.16);color:var(--warm)}
.both{background:rgba(181,140,255,.16);color:var(--violet)}
.leak{color:var(--hot);font-weight:700}
.det{font-size:11px;color:var(--mut);white-space:normal;max-width:340px;text-align:left}
.note{color:var(--mut);font-size:11px;margin-top:12px}
.x{cursor:pointer;color:var(--accent)}
tr.detail td{background:var(--p2);white-space:normal;text-align:left;font-size:12px;color:var(--ink)}
</style></head><body><div class=wrap>
<h1>Biotech Buyouts — Comprehensive Deal Analysis</h1>
<p class=sub id=sub></p>
<div class=kpis id=kpis></div>
<div class=bar>
<input type=search id=q placeholder="filter company / ticker / acquirer / stage…">
<span class=chip data-f=all id=cAll>All</span>
<span class=chip data-f=inbound>Inbound</span>
<span class=chip data-f=outbound>Outbound/process</span>
<span class=chip data-f=leak>Leaked 1m+ early</span>
<span class=chip data-f=cvr>Has CVR</span>
<span class=chip data-f=multi>Multiple bidders</span>
</div>
<div class=scroll><table id=t><thead><tr></tr></thead><tbody></tbody></table></div>
<p class=note id=foot></p>
</div>
<script>
const D=__DATA__;const $=s=>document.querySelector(s);
const pct=x=>x==null?"":(x*100).toFixed(0)+"%";
const sg=x=>x==null?"":(x>0?"+":"")+(x*100).toFixed(0)+"%";
const money=x=>x==null?"":"$"+(+x).toLocaleString();
const m$=x=>x==null?"":"$"+(+x>=1000?(+x/1000).toFixed(1)+"B":(+x).toFixed(0)+"M");
const med=a=>{a=a.filter(x=>typeof x==="number").sort((x,y)=>x-y);return a.length?a[a.length>>1]:null;};

// KPIs
const prem=D.map(r=>r.premium), leaks=D.filter(r=>r.leaked_early===true).length;
const inb=D.filter(r=>r.direction==="inbound").length, outb=D.filter(r=>r.direction==="outbound"||r.direction==="both").length;
const multi=D.filter(r=>+r.n_parties>1).length, eng=D.map(r=>r.eng_to_deal_days);
const kpi=[["Deals",D.length,""],["Median premium",pct(med(prem)),"good"],
 ["Leaked 1m+ early",leaks+" ("+Math.round(leaks/D.length*100)+"%)","hot"],
 ["Inbound (buyer-led)",inb,"accent"],["Ran a process",outb,"warm"],
 ["Multiple bidders",multi,""],["Median engage→deal",med(eng)?Math.round(med(eng)/30.4)+" mo":"—",""]];
$("#kpis").innerHTML=kpi.map(k=>`<div class=kpi><div class=v style="color:var(--${k[2]||'ink'})">${k[1]}</div><div class=l>${k[0]}</div></div>`).join("");
$("#sub").textContent=`${D.length} buyouts · premium, stage, bid range, parties, timing, leak signal & trailing returns · deterministic metrics + Gemini-extracted narrative fields`;

const COLS=[
 ["ticker","Ticker",r=>`<span class=tk>${r.ticker||""}</span>`],
 ["company","Company",r=>(r.company||"").replace(/,? (Inc|Corp|Ltd|Co|Holdings|plc|N\\.V|S\\.A|AG)\\.?.*$/,"").slice(0,26)],
 ["acquirer","Acquirer",r=>(r.acquirer||"").slice(0,24)],
 ["ann_date","Announced",r=>r.ann_date||""],
 ["deal_size_m","Size",r=>m$(r.deal_size_m)],
 ["per_share","$/sh",r=>r.per_share!=null?"$"+r.per_share:""],
 ["premium","Premium",r=>`<b class=${r.premium>0?'pos':'neg'}>${pct(r.premium)}</b>`],
 ["stage","Stage",r=>`<span class=det>${r.stage||""}</span>`],
 ["offer_low","Bid low",r=>r.offer_low!=null?"$"+r.offer_low:""],
 ["offer_high","Bid high",r=>r.offer_high!=null?"$"+r.offer_high:""],
 ["n_parties","Parties",r=>r.n_parties??""],
 ["direction","Interest",r=>{const d=r.direction||"";const c=d==="inbound"?"in":d==="outbound"?"out":d==="both"?"both":"";return c?`<span class="tag ${c}">${d}</span>`:"";}],
 ["eng_to_deal_days","Engage→deal",r=>r.eng_to_deal_days!=null?(r.eng_to_deal_days/30.4).toFixed(1)+" mo":""],
 ["leaked_early","Leak 1m+",r=>r.leaked_early===true?`<span class=leak>YES</span>`:(r.leaked_early===false?"<span class=muted>no</span>":"")],
 ["ret_3m","3m",r=>`<span class=${r.ret_3m>0?'pos':'neg'}>${sg(r.ret_3m)}</span>`],
 ["ret_6m","6m",r=>`<span class=${r.ret_6m>0?'pos':'neg'}>${sg(r.ret_6m)}</span>`],
 ["ret_12m","12m",r=>`<span class=${r.ret_12m>0?'pos':'neg'}>${sg(r.ret_12m)}</span>`],
 ["ret_24m","24m",r=>`<span class=${r.ret_24m>0?'pos':'neg'}>${sg(r.ret_24m)}</span>`],
 ["inflections","Value-inflecting events",r=>`<span class=det>${(r.inflections||[]).join(" · ")||"<span class=muted>none</span>"}</span>`],
];
$("#t thead tr").innerHTML=COLS.map(c=>`<th data-k="${c[0]}">${c[1]}</th>`).join("");

let sortK="premium",dir=-1,filt="all",q="";
function pass(r){
 if(q){const s=[r.ticker,r.company,r.acquirer,r.stage].join(" ").toLowerCase();if(!s.includes(q))return false;}
 if(filt==="inbound")return r.direction==="inbound";
 if(filt==="outbound")return r.direction==="outbound"||r.direction==="both";
 if(filt==="leak")return r.leaked_early===true;
 if(filt==="cvr")return r.max_cvr!=null&&r.per_share!=null&&+r.max_cvr>+r.per_share;
 if(filt==="multi")return +r.n_parties>1;
 return true;
}
function render(){
 let rs=D.filter(pass);
 rs.sort((a,b)=>{let x=a[sortK],y=b[sortK];
  if(typeof x==="number"&&typeof y==="number")return (x-y)*dir;
  return String(x==null?"":x).localeCompare(String(y==null?"":y))*dir;});
 $("#t tbody").innerHTML=rs.map(r=>"<tr>"+COLS.map(c=>`<td>${c[2](r)}</td>`).join("")+"</tr>").join("");
 $("#foot").textContent=`${rs.length} of ${D.length} shown · trailing returns measured to the unaffected price (~4 weeks before announcement) · click a column header to sort.`;
}
document.querySelectorAll("#t th").forEach(th=>th.onclick=()=>{const k=th.dataset.k;if(k===sortK)dir*=-1;else{sortK=k;dir=(k==="ticker"||k==="company"||k==="acquirer")?1:-1;}render();});
$("#q").oninput=e=>{q=e.target.value.toLowerCase();render();};
document.querySelectorAll(".chip").forEach(c=>c.onclick=()=>{
 document.querySelectorAll(".chip").forEach(x=>x.classList.remove("on"));c.classList.add("on");
 filt=c.dataset.f;render();});
$("#cAll").classList.add("on");render();
</script></body></html>"""


def main():
    build_dashboard()
    build_analysis_page()


if __name__ == "__main__":
    main()
