# Biotech Buyout Analysis — Comprehensive Cross-Deal Page

_Generated from 238 SC 14D-9 acquisition reports in `buyouts/reports/`._

Deterministic fields (premium, size, trailing price moves) come from `deals.json` / `prices.csv`. Qualitative fields (stage, value-inflection events, offer range, parties, timing, direction, early leak) are extracted by `google/gemini-3-flash-preview`.

## Portfolio Summary

- **Deals analyzed:** 238
- **Premium (vs unaffected):** median **59%**, range -98%–482% (n=230)
- **Announcement → close:** median **44 days**
- **Deals with a CVR:** 59 of 238
- **Trailing return to unaffected (median):** 3mo +6%, 6mo +7%, 12mo -5%, 24mo -12%
- **Company stage mix:** Phase 3 lead asset (8), Phase 3 lead + 1 approved drug (6), Phase 3 lead, pre-revenue (4), Phase 1/2 lead asset (4), Marketed products + Phase 3 lead (3), Phase 3 lead (3), Phase 2 lead asset (3), Marketed products + Phase 3 pipeline (2)
- **Interest direction:** both (114), inbound (80), outbound (43), unclear (1)
- **Early leak (1+ month before deal):** no leak (179), leaked 1m+ (59)

## Master Table

| Company | Ticker | Buyer | Ann. | Size | Premium | Stage | Bid low→high | # Parties | Eng→Deal | Direction | Leak? | 3mo | 6mo | 12mo | 2yr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SCHERING AKTIENGESELLSCHAFT | no_ticker | Bayer Aktiengesellschaft | 2006-03-23 | $17.3B | — | Marketed products + Pipeline | $77.00→$89.36 | 3 | 0.3 mo | inbound | yes | — | — | — | — |
| VIRBAC CORPORATION | VBAC | Virbac S.A. | 2006-08-08 | $130M | 37% | Commercial + R&D pipeline | $4.15→$5.75 | 1 | 7.9 mo | inbound | no | -4% | -5% | +61% | +64% |
| AnorMED Inc. | ANOR | Genzyme Corporation | 2006-08-30 | $567M | 111% | Phase 3 lead + Phase 1/2 clinical | $8.55→$12.00 | 3 | 11.0 mo | both | yes | -6% | +12% | — | — |
| Myogen, Inc. | MYOG | Gilead Sciences, Inc. | 2006-10-02 | $2.3B | 50% | Phase 3 lead + Phase 2b | $44.00→$52.50 | 3 | 6.1 mo | both | no | +10% | -15% | +71% | +322% |
| KOS PHARMACEUTICALS INC | KOSP | Abbott Laboratories | 2006-11-06 | $3.7B | 60% | Marketed products + Phase 3 pipeline | $60.00→$78.00 | 10 | 1.3 mo | both | no | +26% | +9% | -24% | +11% |
| COTHERIX INC | CTRX | Actelion Ltd. | 2006-11-19 | $389M | 249% | Marketed lead asset + Phase 2 | $10.00→$13.50 | 3 | 3.3 mo | inbound | no | +33% | — | — | — |
| PRAECIS PHARMACEUTICALS INCORPORAT | PRCS | GlaxoSmithKline plc | 2006-12-21 | $54M | 140% | Phase 1 lead + 1 marketed drug (EU) | $4.29→$5.00 | 100 | 14.1 mo | both | no | +4% | -61% | -48% | -77% |
| NEW RIVER PHARMACEUTICALS INC | NRPH | Shire plc | 2007-02-20 | $2.4B | 15% | Approved lead asset (VYVANSE) | $61.50→$64.00 | 15 | 24.7 mo | both | yes | +17% | +120% | +67% | +364% |
| MedImmune, Inc. | MEDI | AstraZeneca PLC | 2007-04-23 | $13.8B | 70% | Marketed products + Phase 3 lead | $50.00→$58.00 | 20 | 1.0 mo | outbound | yes | +7% | +19% | -6% | +34% |
| BIOENVISION, INC. | BIVN | Genzyme Corporation | 2007-05-29 | $308M | 51% | Marketed lead asset + Phase 3 | $5.25→$5.60 | 21 | 35.9 mo | both | no | -23% | -31% | -43% | -40% |
| DIGENE CORPORATION | DIGE | QIAGEN N.V. | 2007-06-03 | $1.5B | 33% | Marketed diagnostic franchise | $58.00→$61.25 | 12 | 4.8 mo | both | no | -8% | -3% | +7% | +84% |
| Coley Pharmaceutical Group, Inc. | COLY | Pfizer Inc. | 2007-11-16 | $214M | 169% | Phase 2/3 lead + clinical adjuvant platform | $6.25→$8.00 | 3 | 4.0 mo | outbound | no | -11% | -70% | -77% | -81% |
| NATROL, INC. | NTOL | Plethico Pharmaceuticals L | 2007-11-18 | $63M | 40% | Commercial, multiple marketed nutraceutical brands | $3.50→$4.40 | 1 | 7.1 mo | inbound | no | -21% | +1% | +57% | +34% |
| Adams Respiratory Therapeutics, In | ARXT | Reckitt Benckiser Group pl | 2007-12-10 | $2.2B | 39% | Commercial consumer healthcare portfolio | $48.00→$60.00 | 10 | 2.1 mo | both | no | +4% | +11% | +2% | +1% |
| MGI PHARMA INC | MOGN | Eisai Co., Ltd. | 2007-12-10 | $3.3B | 37% | 2 marketed drugs + NDA filing | $33.00→$41.00 | 19 | 14.5 mo | inbound | no | +33% | +40% | +58% | +79% |
| ENCYSIVE PHARMACEUTICALS INC | ENCY | Pfizer Inc. | 2008-02-20 | $190M | 246% | Marketed (EU/AU/CA), Phase 3 (US) | $1.25→$2.35 | 70 | 4.4 mo | outbound | yes | -53% | -67% | -82% | -93% |
| COLLAGENEX PHARMACEUTICALS INC | CGPI | Galderma Pharma S.A. | 2008-02-26 | $358M | 41% | Marketed lead asset (Oracea) | $12.50→$16.60 | 14 | 31.9 mo | both | no | +14% | -4% | -19% | -12% |
| Millennium Pharmaceuticals, Inc. | MLNM | Takeda Pharmaceutical Comp | 2008-04-10 | $8.2B | 91% | Marketed lead asset + Phase 2 and IND pipeline | $23.00→$25.00 | 1 | 9.0 mo | inbound | yes | -13% | +31% | +23% | +39% |
| Sirtris Pharmaceuticals, Inc. | SIRT | GlaxoSmithKline plc | 2008-04-22 | $658M | 109% | Clinical/Pre-clinical SIRT1 activation platform | $18.50→$22.50 | 2 | 26.5 mo | both | no | -23% | -35% | -14% | — |
| USANA HEALTH SCIENCES, INC. | USNA | Gull-Unity Holding Corp. | 2008-05-13 | $426M | 23% | Marketed nutritional supplements | $26.00→$26.00 | 1 | 11.4 mo | inbound | no | -57% | -52% | -49% | -43% |
| Third Wave Technologies, Inc. | TWTI | Hologic, Inc. | 2008-06-09 | $510M | 33% | PMA Submission (HPV tests) + FDA Cleared (Cystic Fibrosis) | $4.75→$11.25 | 11 | 2.4 mo | both | no | +6% | -5% | +65% | +206% |
| TARO PHARMACEUTICAL INDUSTRIES LTD | TARO | Sun Pharmaceutical Industr | 2008-06-25 | $306M | -7% | Commercial, generic product pipeline | $7.75→$7.75 | 4 | 29.8 mo | inbound | no | -1% | +15% | +11% | -22% |
| GENENTECH INC | DNA | Roche Holding Ltd | 2008-07-21 | $100.1B | 27% | Marketed products + Phase 3 pipeline | $86.50→$95.00 | 1 | 7.7 mo | inbound | yes | -6% | +10% | -0% | -7% |
| SCIELE PHARMA, INC. | SCRX | Shionogi & Co., Ltd. | 2008-09-01 | $1.0B | 63% | Marketed lead asset (Sular) | $28.50→$31.00 | 6 | 4.1 mo | inbound | no | -11% | -22% | -19% | +7% |
| GENELABS TECHNOLOGIES, INC. | GNLB | GlaxoSmithKline plc | 2008-10-29 | $57M | 177% | Late-stage (Prestara) + Discovery/Preclinical (HCV) | $1.03→$1.30 | 23 | 1.3 mo | both | no | -31% | -45% | -75% | -70% |
| ALPHARMA INC | ALO | King Pharmaceuticals, Inc. | 2008-11-24 | $1.5B | 26% | NDA / Priority Review lead + 1 marketed drug | $33.00→$37.00 | 3 | 4.5 mo | inbound | yes | +18% | +15% | +42% | +33% |
| Omrix Biopharmaceuticals, Inc. | OMRI | Johnson & Johnson | 2008-11-24 | $428M | 69% | Phase 3 lead + 2 marketed products | $21.00→$25.00 | 4 | 3.8 mo | both | yes | -22% | -5% | -56% | -48% |
| MEMORY PHARMACEUTICALS CORP | MEMY | Hoffmann-La Roche Inc. | 2008-11-25 | $50M | 319% | Phase 2 lead + Phase 1 and 2 assets | $0.55→$0.61 | 2 | 1.2 mo | inbound | no | -77% | -81% | -93% | -97% |
| Indevus Pharmaceuticals, Inc. | ENDP | Endo Pharmaceuticals Holdi | 2009-01-05 | $352M | 87% | 1 approved drug + Phase 3/NDA lead assets | $6.50→$7.50 | 1 | 3.6 mo | inbound | no | +28% | +75% | -68% | -65% |
| Targanta Therapeutics Corporation | TARG | The Medicines Company | 2009-01-12 | $42M | 92% | Phase 3 (Complete Response Letter received) | $1.80→$6.55 | 26 | 4.3 mo | outbound | no | -85% | -86% | -89% | — |
| IDM PHARMA, INC. | IDMI | Takeda Pharmaceutical Comp | 2009-05-18 | $67M | 43% | Approved (Europe) / Phase 3 (US) | $1.94→$2.64 | 50 | 29.3 mo | outbound | no | +1% | +11% | -19% | -42% |
| Cougar Biotechnology, Inc. | CGRB | Johnson & Johnson | 2009-05-21 | $894M | 27% | Phase 3 lead, pre-revenue | $28.00→$43.00 | 20 | 6.2 mo | outbound | yes | +15% | +26% | +72% | +37% |
| Monogram Biosciences, Inc. | MGRM | Laboratory Corporation of  | 2009-06-23 | $105M | 82% | Commercial (HIV and Oncology diagnostics) | $3.00→$4.55 | 1 | 7.7 mo | inbound | no | -12% | +11% | -62% | -75% |
| NOVEN PHARMACEUTICALS INC | NOVN | Hisamitsu Pharmaceutical C | 2009-07-14 | $414M | 38% | Marketed product + Phase 2 lead asset | $14.00→$16.50 | 1 | 3.7 mo | inbound | no | +24% | +4% | +5% | -40% |
| Avigen, Inc. | AVGN | MediciNova, Inc. | 2009-08-21 | $32M | -9% | Phase 2 lead + 1 failed Phase 2 asset | $1.00→$1.24 | 3 | 8.4 mo | both | yes | +8% | +41% | -59% | -77% |
| Sepracor Inc. | SEPR | Dainippon Sumitomo Pharma  | 2009-09-03 | $2.6B | 31% | Marketed products + Phase 3 lead | $15.00→$23.00 | 7 | 3.3 mo | both | yes | +32% | +15% | -0% | -37% |
| CHATTEM INC | CHTT | sanofi-aventis | 2009-12-21 | $1.8B | 41% | Marketed OTC portfolio + Rx-to-OTC switch platform | $85.00→$93.50 | 1 | 3.8 mo | inbound | no | +8% | +18% | -4% | -12% |
| OSI PHARMACEUTICALS INC | OSIP | Astellas US Holding, Inc. | 2010-03-01 | $3.4B | 68% | Marketed lead + Phase 3 pipeline | $52.00→$57.50 | 2 | 13.5 mo | inbound | yes | +6% | +1% | -4% | -7% |
| PENWEST PHARMACEUTICALS CO | PPCO | Endo Pharmaceuticals Holdi | 2010-08-09 | $160M | 53% | Marketed product + Phase 2 lead asset | $4.00→$5.00 | 1 | 0.6 mo | inbound | yes | -9% | +29% | +26% | -19% |
| ZYMOGENETICS, INC. | ZGEN | Bristol-Myers Squibb Compa | 2010-09-07 | $844M | 139% | Phase 2 lead + 1 marketed product | $8.00→$9.75 | 1 | 25.5 mo | inbound | no | -16% | -21% | -21% | -44% |
| GENZYME CORP | GENZ | sanofi-aventis | 2010-10-04 | $19.2B | 5% | Phase 3 lead + 2 approved drugs | $69.00→$74.00 | 3 | 2.2 mo | inbound | yes | +48% | +23% | +23% | +9% |
| KING PHARMACEUTICALS INC | KG | Pfizer Inc. | 2010-10-11 | $3.6B | 52% | Commercial with marketed products (Altace) + pipeline | $11.00→$14.25 | 5 | 4.3 mo | both | yes | +17% | -24% | -12% | +14% |
| EURAND N.V. | EURX | Axcan Holdings Inc. | 2010-12-01 | $576M | 9% | Marketed lead asset + Phase 3/Pending FDA | $11.00→$12.00 | 26 | 4.6 mo | both | no | +38% | +6% | -17% | +48% |
| CYPRESS BIOSCIENCE INC | CYPB | Ramius Value and Opportuni | 2010-12-14 | $251M | 63% | Phase 2b lead + 1 marketed drug (royalty interest) | $4.00→$6.50 | 3 | 6.6 mo | inbound | yes | +4% | -6% | -33% | -33% |
| MATRIXX INITIATIVES, INC. | MTXX | H.I.G. Capital, LLC | 2010-12-14 | $82M | 65% | Marketed OTC products + product recall status | $6.50→$8.75 | 1 | 10.8 mo | inbound | no | +15% | +13% | +40% | -66% |
| MARTEK BIOSCIENCES CORPORATION | MATK | Koninklijke DSM N.V. | 2010-12-21 | $1.1B | 43% | Marketed products (ARA + Amerifit) | $27.00→$31.50 | 5 | 12.4 mo | both | no | +7% | +16% | +22% | -23% |
| CLINICAL DATA INC | CLDA | Forest Laboratories, Inc. | 2011-02-22 | $933M | 100% | Approved lead asset + Phase 3 pipeline | $24.00→$30.00 | 24 | 22.3 mo | outbound | no | -20% | +9% | -6% | +80% |
| Inspire Pharmaceuticals, Inc. | ISPH | Merck & Co., Inc. | 2011-04-05 | $416M | 25% | Phase 3 (failed) lead + 2 marketed drugs | $4.40→$5.00 | 4 | 1.3 mo | outbound | no | -43% | -19% | -36% | -11% |
| ICAGEN INC | ICGN | Pfizer Inc. | 2011-07-20 | $53M | 180% | Phase 2 lead + Pre-clinical | $4.00→$6.00 | 43 | 3.2 mo | both | no | -20% | +48% | -36% | -33% |
| Anadys Pharmaceuticals, Inc. | ANDS | Roche Holding Ltd | 2011-10-17 | $212M | 289% | Phase 2 lead + clinical secondary asset | $3.00→$3.70 | 15 | 13.8 mo | outbound | yes | +2% | -16% | -47% | -57% |
| ADOLOR CORPORATION | ADLR | Cubist Pharmaceuticals, In | 2011-10-24 | $198M | 146% | Phase 2 lead + 1 approved drug | $4.00→$4.25 | 11 | 6.8 mo | both | no | -3% | +20% | +57% | +19% |
| Pharmasset Inc | VRUS | Gilead Sciences, Inc. | 2011-11-21 | $10.4B | — | Phase 3 lead + Phase 2b assets | $100.00→$137.00 | 5 | 5.1 mo | both | no | — | — | — | — |
| MICROMET, INC. | MITI | Amgen Inc. | 2012-01-26 | $1.0B | — | Phase 2 lead + BiTE platform | $9.00→$11.00 | 28 | 12.5 mo | both | yes | — | — | — | — |
| AMYLIN PHARMACEUTICALS INC | AMLN | Bristol-Myers Squibb Compa | 2012-06-29 | $5.1B | 16% | Commercial, 2 approved drugs + Phase 2/3 pipeline | $22.00→$31.00 | 12 | 4.4 mo | both | yes | +56% | +169% | +99% | +44% |
| DUSA PHARMACEUTICALS, INC. | DUSA | Sun Pharmaceutical Industr | 2012-11-08 | $200M | 17% | Marketed products (Levulan Kerastick, BLU-U) + Phase 2 label expansion | $6.98→$8.00 | 30 | 6.0 mo | outbound | no | +28% | +15% | +84% | +159% |
| MAP Pharmaceuticals, Inc. | MAPP | Allergan, Inc. | 2013-01-22 | $889M | — | NDA Resubmission (PDUFA April 2013) | $19.00→$25.00 | 2 | 2.8 mo | inbound | no | — | — | — | — |
| Obagi Medical Products, Inc. | OMPI | Valeant Pharmaceuticals In | 2013-03-20 | $418M | 68% | Commercial, marketed core product line | $16.50→$24.00 | 12 | 1.2 mo | both | yes | +11% | +7% | +19% | +14% |
| ELAN CORPORATION, PLC | ELN | Royalty Pharma | 2013-05-15 | — | — | Commercial (Tysabri royalty interest) | $11.00→$15.50 | 7 | 2.7 mo | both | yes | +16% | +10% | -10% | +42% |
| Trius Therapeutics Inc | TSRX | Cubist Pharmaceuticals, In | 2013-07-30 | $652M | 67% | Phase 3 / NDA preparation | $12.25→$13.50 | 13 | 12.2 mo | inbound | yes | +18% | +69% | +41% | +9% |
| Onyx Pharmaceuticals, Inc. | ONXX | Amgen Inc. | 2013-08-25 | $9.2B | -5% | 3 approved drugs + Phase 3 lead asset | $120.00→$125.00 | 13 | 2.6 mo | inbound | yes | +39% | +68% | +69% | +312% |
| SANTARUS INC | SNTS | Salix Pharmaceuticals, Ltd | 2013-11-07 | $2.2B | 43% | Marketed (Uceris) + Phase 3 (Ruconest) | $4.50→$32.00 | 16 | 41.3 mo | both | no | +2% | +33% | +135% | +688% |
| Cadence Pharmaceuticals Inc | CADX | Mallinckrodt plc | 2014-02-10 | $1.2B | 36% | 1 approved drug | $11.25→$14.00 | 8 | 3.0 mo | both | no | +74% | +37% | +91% | +155% |
| Chelsea Therapeutics International | CHTP | H. Lundbeck A/S | 2014-05-08 | $508M | 21% | 1 approved drug (accelerated approval) | $6.44→$6.44 | 13 | 12.9 mo | outbound | yes | +52% | +82% | +177% | +142% |
| Idenix Pharmaceuticals, Inc. | IDIX | Merck & Co., Inc. | 2014-06-09 | $3.7B | 379% | Phase 1/2 lead asset | $7.18→$24.50 | 4 | 6.2 mo | both | yes | -25% | +18% | +41% | -46% |
| Cadista Holdings Inc. | CADI | Jubilant Life Sciences Ltd | 2014-08-01 | $188M | — | Commercial + Marketed generic products | $1.20→$1.60 | 2 | 10.9 mo | inbound | no | — | — | — | — |
| INTERMUNE, INC. | ITMN | Roche Holding Ltd | 2014-08-24 | $8.0B | 63% | Phase 3 / NDA Resubmission | $57.00→$74.00 | 5 | 1.0 mo | inbound | yes | +53% | +170% | +207% | +472% |
| AMBIT BIOSCIENCES CORP | AMBI | Daiichi Sankyo Company, Li | 2014-09-28 | $270M | 98% | Phase 3 lead asset | $12.00→$15.00 | 2 | 9.4 mo | both | no | +10% | -31% | -44% | — |
| Durata Therapeutics, Inc. | DRTX | Actavis plc | 2014-10-06 | $616M | 54% | Approved lead asset + Phase 3 expansion | $18.00→$23.00 | 7 | 0.5 mo | both | no | -7% | +6% | +68% | +58% |
| ALLERGAN INC | AGN | Actavis plc | 2014-11-16 | $38.4B | -27% | Phase 3 lead + 1 approved drug | $153.00→$219.00 | 4 | 6.9 mo | both | yes | +6% | +33% | +96% | +100% |
| AVANIR PHARMACEUTICALS, INC. | AVNR | Otsuka Pharmaceutical Co., | 2014-12-02 | $3.3B | 31% | 1 marketed drug + Phase 2/3 pipeline | $15.00→$17.00 | 5 | 18.7 mo | inbound | yes | +146% | +179% | +202% | +404% |
| Cubist Pharmaceuticals Inc. | CBST | Merck & Co., Inc. | 2014-12-08 | $7.8B | 25% | Phase 3 lead + 4 approved drugs | $85.00→$102.00 | 5 | 7.1 mo | both | no | +2% | +6% | +35% | +92% |
| NPS Pharmaceuticals, Inc. | NPSP | Shire plc | 2015-01-11 | $5.0B | 47% | 1 commercial drug + 1 pending FDA approval | $41.00→$46.00 | 12 | 1.9 mo | both | yes | -4% | -10% | +27% | +250% |
| SALIX PHARMACEUTICALS LTD | SLXP | Valeant Pharmaceuticals In | 2015-02-22 | $11.1B | 37% | Marketed products + Phase 3 lead | $150.00→$173.00 | 9 | 1.1 mo | both | yes | -10% | -5% | +28% | +155% |
| Auspex Pharmaceuticals, Inc. | ASPX | Teva Pharmaceutical Indust | 2015-03-30 | $3.2B | 50% | Phase 3 lead, pre-revenue | $85.00→$101.00 | 6 | 21.9 mo | both | no | +178% | +192% | +172% | — |
| CELLULAR DYNAMICS INTERNATIONAL, I | ICEL | FUJIFILM Holdings Corporat | 2015-03-30 | $261M | 204% | Commercial (iCell Hepatocytes) + Development (Pharma Cellular Therapeutic) | $13.00→$16.50 | 9 | 9.7 mo | outbound | no | -18% | -53% | -64% | -46% |
| HYPERION THERAPEUTICS INC | HPTX | Horizon Pharma plc | 2015-03-30 | $960M | 56% | 2 approved drugs + Phase 2/3 lead expansion | $30.00→$46.00 | 5 | 1.5 mo | both | no | +44% | +14% | -5% | +20% |
| Perrigo Company plc | PRGO | Mylan N.V. | 2015-04-08 | $11.0B | -52% | Marketed portfolio + Phase 3 | $205.00→$205.00 | 1 | 10.2 mo | inbound | no | -0% | +7% | -5% | +31% |
| Depomed, Inc. | ASRT | Horizon Pharma plc | 2015-07-07 | $57M | -96% | Commercial with multiple approved drugs (NUCYNTA, Gralise) | $29.25→$33.00 | 4 | 1.3 mo | both | no | -7% | +36% | +75% | +257% |
| Receptos, Inc. | RCPT (NASDAQ Global Market) | Celgene Corporation | 2015-07-14 | $7.3B | 30% | Phase 3 lead, pre-revenue | $175.00→$232.00 | 14 | 22.5 mo | both | yes | +19% | +48% | +345% | +868% |
| INSITE VISION INCORPORATED | INSV | Sun Pharmaceutical Industr | 2015-09-15 | $46M | 59% | NDA Filed lead + 1 marketed drug | $0.25→$0.35 | 36 | 19.5 mo | both | no | +57% | +22% | -12% | +10% |
| ZS Pharma, Inc. | ZSPH | AstraZeneca PLC | 2015-11-06 | $2.3B | 35% | NDA (Under FDA Review), lead asset ZS-9 | $83.00→$90.00 | 8 | 1.8 mo | inbound | yes | +14% | +61% | +74% | — |
| Ocata Therapeutics, Inc. | OCAT | Astellas Pharma Inc. | 2015-11-10 | $360M | 81% | Phase 1/2 lead asset | $8.00→$8.50 | 11 | 15.6 mo | both | no | -10% | -29% | -32% | -22% |
| Biotie Therapies Oyj | BITI | Acorda Therapeutics, Inc. | 2016-01-19 | $289M | -98% | Phase 3 lead + 1 marketed drug | $25.50→$25.60 | 7 | 3.3 mo | both | no | -17% | -42% | — | — |
| ALERE INC. | ALR | Abbott Laboratories | 2016-01-30 | $4.5B | 30% | Commercial diagnostic platforms | $46.00→$51.00 | 5 | — | both | yes | -23% | -28% | +4% | +3% |
| Alexza Pharmaceuticals Inc. | ALXA | Grupo Ferrer Internacional | 2016-05-10 | $20M | 80% | Approved/Commercial lead asset | $0.60→$0.90 | 83 | 7.4 mo | outbound | yes | -7% | -60% | -75% | -88% |
| Anacor Pharmaceuticals, Inc. | ANAC | Pfizer Inc. | 2016-05-16 | $4.5B | 53% | Phase 3 / NDA submitted lead + 1 marketed drug | $82.00→$99.25 | 3 | 1.0 mo | both | no | -31% | — | — | — |
| XENOPORT, INC. | XNPT | Arbor Pharmaceuticals, Inc | 2016-05-23 | $449M | 43% | Commercial with 1 approved drug + Phase 3 ready asset | $5.65→$7.03 | 33 | 1.8 mo | outbound | yes | -3% | -5% | -33% | +21% |
| Celator Pharmaceuticals Inc | CPXX | Jazz Pharmaceuticals plc | 2016-05-27 | $1.3B | 104% | Pre-commercial, Phase 3 lead | $3.00→$30.25 | 41 | 17.7 mo | both | no | +9% | +21% | +36% | +452% |
| Sagent Pharmaceuticals, Inc. | SGNT | Nichi-Iko Pharmaceutical C | 2016-07-11 | $716M | 55% | Commercial generic injectable portfolio + 20 pipeline ANDAs | $20.32→$21.75 | 7 | 5.3 mo | both | yes | +4% | -4% | -40% | -48% |
| Relypsa, Inc. | RLYP | Galenica AG | 2016-07-21 | $1.4B | 79% | Approved / Commercial | $29.00→$32.00 | 4 | 26.5 mo | both | yes | +33% | -36% | -47% | -24% |
| MEDIVATION, INC. | MDVN | Pfizer Inc. | 2016-08-22 | $13.5B | 30% | Marketed lead asset + Phase 3 pipeline | $52.50→$81.50 | 15 | 4.1 mo | inbound | yes | +19% | +66% | -39% | -31% |
| Raptor Pharmaceutical Corp | RPTP | Horizon Pharma plc | 2016-09-12 | $772M | 33% | 1 approved drug + 1 drug approved in EU/Canada under FDA review | $9.00→$9.00 | 3 | — | outbound | yes | +60% | +70% | -49% | -39% |
| Vitae Pharmaceuticals, Inc. | VTAE | Allergan plc | 2016-09-14 | $606M | 143% | Phase 2 lead | $20.50→$21.00 | 38 | 8.5 mo | both | no | +35% | +1% | +4% | +9% |
| Tobira Therapeutics, Inc. | TBRA | Allergan plc | 2016-09-20 | $534M | 482% | Phase 2b lead asset | $28.35→$28.35 | 11 | 3.0 mo | inbound | no | -41% | -30% | -63% | -53% |
| ARIAD PHARMACEUTICALS INC | ARIA | Takeda Pharmaceutical Comp | 2017-01-09 | $4.7B | 89% | 1 marketed drug + 1 NDA review asset | $20.00→$24.00 | 5 | 20.4 mo | both | yes | +25% | +53% | +110% | +103% |
| CoLucid Pharmaceuticals, Inc. | CLCD | Eli Lilly and Company | 2017-01-18 | $897M | 29% | Phase 3 lead | $42.70→$46.50 | 50 | 4.4 mo | both | no | +29% | +421% | +434% | +352% |
| Nabriva Therapeutics AG | NBRV | Nabriva Therapeutics plc | 2017-04-18 | $2M | — | Phase 3 lead | — | 1 | 0.2 mo | outbound | no | +124% | +53% | +30% | — |
| Patheon N.V. | PTHN | Thermo Fisher Scientific I | 2017-05-15 | $5.1B | 36% | Commercial CDMO services | $33.00→$35.00 | 2 | 2.5 mo | inbound | no | -9% | -6% | — | — |
| Kite Pharma, Inc. | KITE | Gilead Sciences, Inc. | 2017-08-28 | $10.3B | 62% | Registration/Pre-approval lead asset | $127.00→$180.00 | 1 | 7.9 mo | inbound | yes | +36% | +130% | +97% | +106% |
| Dimension Therapeutics, Inc. | DMTX | Ultragenyx Pharmaceutical  | 2017-10-03 | $151M | 72% | Phase 1/2 lead + multiple pre-clinical | $1.40→$6.00 | 21 | 0.5 mo | both | no | +203% | +88% | -41% | -72% |
| Advanced Accelerator Applications  | AAAP | Novartis AG | 2017-10-30 | $3.6B | -39% | Approved (EU) / NDA Resubmitted (US), lead asset Lutathera | $62.50→$82.00 | 2 | 3.1 mo | inbound | yes | +73% | +70% | +78% | +142% |
| Ocera Therapeutics, Inc. | OCRX | Mallinckrodt plc | 2017-11-02 | $40M | 33% | Phase 2b, pre-revenue | $1.52→$1.52 | 34 | 9.8 mo | both | no | -2% | -13% | -57% | -67% |
| REPROS THERAPEUTICS INC. | RPRX | Allergan plc | 2017-12-12 | $26M | 63% | Phase 3 (Enclomiphene) and Phase 2 (Proellex) | $0.45→$0.67 | 6 | 8.4 mo | inbound | no | +17% | -51% | -77% | -68% |
| Ignyta, Inc. | RXDX | Roche Holdings, Inc. | 2017-12-22 | $1.8B | 62% | Phase 2 lead asset | $23.00→$27.00 | 26 | 19.2 mo | both | no | +79% | +142% | +145% | +22% |
| Sucampo Pharmaceuticals, Inc. | SCMP | Mallinckrodt plc (Irish pu | 2017-12-26 | $851M | 71% | Commercial with 1 approved drug + Phase 3 pipeline | $17.00→$18.00 | 5 | 3.0 mo | inbound | no | -7% | +3% | -33% | -41% |
| TiGenix NV | TIG | Takeda Pharmaceutical Comp | 2018-01-05 | $527M | 82% | Approved (EU) / Phase 3 (US) | $1.25→$1.78 | 1 | 6.4 mo | inbound | no | -3% | +28% | +61% | — |
| Bioverativ Inc. | BIVV | Sanofi | 2018-01-22 | $11.4B | 94% | Commercial + 2 marketed drugs | $98.50→$105.00 | 1 | 8.4 mo | inbound | yes | -5% | -14% | +22% | — |
| Ablynx NV | ABLX | Sanofi | 2018-01-29 | $3.4B | 21% | Pre-marketing lead asset + Phase 2 pipeline | $26.75→$45.00 | 10 | 0.7 mo | both | yes | — | — | — | — |
| AveXis, Inc. | AVXS | Novartis AG | 2018-04-09 | $8.0B | 59% | Phase 3 / BLA Preparation | $112.00→$218.00 | 4 | 1.7 mo | inbound | yes | +37% | +47% | +90% | +482% |
| ARMO BioSciences, Inc. | ARMO | Eli Lilly and Company | 2018-05-10 | $1.5B | 39% | Phase 3 lead asset, pre-revenue | $48.00→$50.00 | 4 | 1.7 mo | both | no | +21% | — | — | — |
| JUNIPER PHARMACEUTICALS INC | JNP | Catalent, Inc. | 2018-07-03 | $128M | 29% | Phase 2b failure; commercial CDMO and progesterone gel business | $8.00→$11.50 | 38 | 4.5 mo | both | no | +1% | +77% | +98% | +13% |
| TESARO, Inc. | TSRO | GlaxoSmithKline plc | 2018-12-03 | $4.1B | 148% | Marketed lead + Phase 3 pipeline | $66.00→$75.00 | 10 | 5.8 mo | both | yes | +12% | -39% | -73% | -77% |
| Loxo Oncology, Inc. | LOXO | Eli Lilly and Company | 2019-01-07 | $7.2B | 74% | 1 approved drug + Phase 1/2 lead asset | $230.00→$235.00 | 1 | 8.8 mo | inbound | no | -16% | -25% | +62% | +254% |
| Immune Design Corp. | IMDZ | Merck & Co., Inc. | 2019-02-21 | $283M | 312% | Phase 2 lead + Phase 3 discontinued | $5.18→$5.85 | 5 | 5.7 mo | both | no | -14% | -67% | -62% | -74% |
| Spark Therapeutics, Inc. | ONCE | Roche Holding Ltd | 2019-02-25 | $4.4B | 164% | Phase 3 lead + 1 approved drug | $70.00→$114.50 | 3 | 4.6 mo | both | no | -6% | -41% | -25% | -31% |
| Osiris Therapeutics, Inc. | OSIR | Smith & Nephew plc (Englis | 2019-03-12 | $656M | 24% | Commercial (multiple products) + royalty interest | $17.50→$19.00 | 5 | 8.1 mo | both | no | +46% | +72% | +296% | +165% |
| ARRAY BIOPHARMA INC | ARRY | Pfizer Inc. | 2019-06-17 | $10.7B | 120% | Approved drugs + Phase 3 lead asset | $44.00→$48.00 | 4 | 2.9 mo | both | yes | -5% | +33% | +39% | +141% |
| Alder BioPharmaceuticals, Inc. | ALDR | H. Lundbeck A/S | 2019-09-16 | $1.5B | 88% | BLA submitted / Phase 3 lead | $14.00→$18.00 | 11 | 8.2 mo | both | no | -11% | -33% | -48% | -12% |
| Dova Pharmaceuticals, Inc. | DOVA | Swedish Orphan Biovitrum A | 2019-09-30 | $793M | 83% | Approved lead asset + Phase 3 pipeline | $23.00→$29.00 | 28 | 20.5 mo | both | no | +70% | +85% | -41% | -46% |
| The Medicines Company | MDCO | Novartis AG | 2019-11-24 | $6.8B | 49% | Phase 3 lead asset | $74.03→$85.00 | 12 | 5.9 mo | both | no | +54% | +80% | +135% | +84% |
| Audentes Therapeutics, Inc. | BOLD | Astellas Pharma Inc. | 2019-12-02 | $2.8B | 106% | Phase 1/2 lead asset | $49.00→$60.00 | 4 | 6.4 mo | inbound | no | -23% | -23% | -1% | -0% |
| Synthorx, Inc. | THOR | Sanofi | 2019-12-08 | $2.2B | 324% | Clinical-stage lead asset + pre-clinical pipeline | $36.00→$68.00 | 4 | 13.7 mo | both | no | +7% | -4% | +27% | — |
| ArQule, Inc. | ARQL | Merck Sharp & Dohme Corp. | 2019-12-09 | $2.4B | 177% | Phase 1 lead + multiple clinical assets | $18.00→$20.00 | 10 | 5.4 mo | inbound | no | +35% | +51% | +128% | +29% |
| Dermira, Inc. | DERM | Eli Lilly and Company | 2020-01-10 | $1.0B | 48% | Phase 3 lead + 1 approved drug | $13.00→$18.75 | 13 | 4.4 mo | outbound | no | +42% | +26% | +17% | -54% |
| Forty Seven, Inc. | FTSV | Gilead Sciences, Inc. | 2020-03-02 | $4.6B | 159% | Phase 2 lead | $57.50→$95.50 | 4 | 1.8 mo | inbound | no | +388% | +340% | +146% | +130% |
| QIAGEN N.V. | QGEN | Thermo Fisher Scientific I | 2020-03-03 | — | 25% | Marketed diagnostics and sample technologies | $39.00→$39.00 | 2 | 3.7 mo | inbound | yes | +10% | -9% | -8% | -2% |
| STEMLINE THERAPEUTICS INC | STML | A. Menarini - Industrie Fa | 2020-05-04 | $604M | 158% | Marketed (US) / Pending (EU) | $10.00→$11.50 | 2 | 11.0 mo | inbound | no | -59% | -52% | -69% | -76% |
| Portola Pharmaceuticals, Inc. | PTLA | Alexion Pharmaceuticals, I | 2020-05-05 | $1.4B | 179% | Marketed (Accelerated Approval) + Phase 2 | $16.00→$18.00 | 2 | 8.3 mo | inbound | yes | -73% | -76% | -83% | -84% |
| Momenta Pharmaceuticals | MNTA | Johnson & Johnson | 2020-06-15 | $6.2B | 94% | Phase 2 lead + 1 marketed drug | $47.50→$52.50 | 3 | 14.0 mo | inbound | no | -40% | -29% | -3% | +24% |
| Tetraphase Pharmaceuticals, Inc. | TTPH | La Jolla Pharmaceutical Co | 2020-06-24 | $14M | -24% | Commercial-stage, 1 approved drug + Phase 2 lead | $1.24→$2.00 | 16 | 17.6 mo | both | no | +17% | +8% | +230% | -29% |
| Pfenex Inc. | PFNX | Ligand Pharmaceuticals Inc | 2020-08-10 | $412M | 46% | Approved lead asset + commercial platform | $10.50→$12.00 | 1 | 5.4 mo | inbound | no | -10% | -35% | +33% | +67% |
| Principia Biopharma Inc. | PRNB | Sanofi | 2020-08-16 | $3.3B | 26% | Phase 3 initiated + Phase 2b lead asset | $76.00→$100.00 | 2 | 2.9 mo | inbound | yes | +321% | +488% | +335% | +143% |
| Akcea Therapeutics, Inc. | AKCA | Ionis Pharmaceuticals, Inc | 2020-08-31 | $1.8B | 67% | Phase 3 lead + 2 approved drugs | $16.00→$18.15 | 2 | 1.7 mo | inbound | no | -28% | -37% | -48% | -59% |
| IMMUNOMEDICS INC | IMMU | Gilead Sciences, Inc. | 2020-09-13 | $20.4B | 120% | FDA approved (accelerated) + Phase 3 confirmatory | $55.00→$88.00 | 12 | 20.2 mo | both | no | +18% | +118% | +168% | +80% |
| AMAG PHARMACEUTICALS, INC. | AMAG | Covis Group S.à r.l. | 2020-10-01 | $474M | 34% | Commercial with Phase 3 pipeline | $11.00→$13.75 | 17 | 10.0 mo | inbound | no | +33% | +33% | -6% | -54% |
| MyoKardia, Inc. | MYOK | Bristol-Myers Squibb Compa | 2020-10-05 | $12.0B | 99% | Phase 3 lead + clinical-stage pipeline | $185.00→$225.00 | 2 | 19.2 mo | inbound | no | +15% | +80% | +116% | +114% |
| BioSpecifics Technologies Corp. | BSTC | Endo International plc | 2020-10-19 | $650M | 56% | Marketed + 1 approved drug (launching 2021) | $85.00→$88.50 | 2 | 2.2 mo | inbound | no | -6% | +28% | -2% | -10% |
| Prevail Therapeutics Inc. | PRVL | Eli Lilly and Company | 2020-12-15 | $771M | 131% | Clinical-stage gene therapy | $21.00→$22.50 | 20 | 17.6 mo | both | no | -24% | -34% | -8% | — |
| Viela Bio, Inc. | VIE | Horizon Therapeutics plc | 2021-02-01 | $2.9B | 47% | Approved/Marketed lead asset + Phase 3 pipeline | $44.00→$53.00 | 9 | 7.0 mo | both | no | +26% | -16% | +40% | — |
| Pandion Therapeutics, Inc. | PAND | Merck & Co., Inc. | 2021-02-25 | $1.8B | 231% | Phase 1a lead + preclinical platform | $40.00→$60.00 | 2 | 34.6 mo | inbound | no | +60% | +2% | — | — |
| Five Prime Therapeutics, Inc. | FPRX | Amgen Inc. | 2021-03-04 | $1.7B | -9% | Clinical-stage, Phase 2 lead asset | $25.00→$38.00 | 15 | 19.2 mo | outbound | no | +685% | +685% | +685% | +278% |
| CONSTELLATION PHARMACEUTICALS INC | CNST | MorphoSys AG | 2021-06-02 | $1.6B | 57% | Phase 3 lead + Phase 2 pipeline | $29.00→$34.00 | 9 | 10.1 mo | both | no | -34% | +10% | -40% | +132% |
| Translate Bio, Inc. | TBIO | Sanofi | 2021-08-03 | $2.9B | 30% | Clinical stage (MRT5005 and MRT5500) | $28.00→$38.00 | 4 | 2.2 mo | both | no | — | — | — | — |
| ACCELERON PHARMA INC | XLRN | Merck & Co., Inc. | 2021-09-30 | $11.0B | 39% | Phase 3 lead + 1 approved drug | $160.00→$180.00 | 4 | 2.5 mo | both | no | -1% | -5% | +35% | +221% |
| Adamas Pharmaceuticals Inc | ADMS | Supernus Pharmaceuticals,  | 2021-10-10 | $371M | 78% | Commercial with 2 approved drugs + Phase 3/Regulatory | $8.10→$8.10 | 1 | — | unclear | no | -11% | -9% | +6% | +14% |
| Flexion Therapeutics Inc | FLXN | Pacira BioSciences, Inc. | 2021-10-11 | $428M | 40% | Commercial + Phase 1/2 pipeline | $7.50→$8.50 | 21 | 4.7 mo | inbound | yes | -35% | -49% | -49% | -58% |
| Dicerna Pharmaceuticals, Inc. | DRNA | Novo Nordisk A/S (Danish a | 2021-11-18 | $3.0B | 80% | Late-stage development (planned marketing applications for nedosiran) | $32.50→$38.25 | 3 | 3.6 mo | inbound | no | -44% | -27% | +4% | -6% |
| ZOGENIX, INC. | ZGNX | UCB S.A. (société anonyme  | 2022-01-19 | $1.5B | 86% | Commercial (1 approved drug) + Phase 3/sNDA expansion | $20.50→$26.00 | 3 | 6.1 mo | inbound | no | -8% | -22% | -30% | -73% |
| BioDelivery Sciences International | BDSI | Collegium Pharmaceuticals  | 2022-02-14 | $569M | 60% | Commercial stage + Phase 3 | $4.60→$5.60 | 4 | 1.8 mo | inbound | no | +8% | +13% | -19% | -33% |
| Checkmate Pharmaceuticals, Inc. | CMPI | Regeneron Pharmaceuticals, | 2022-04-19 | $231M | 233% | Phase 1b/2 lead asset | $7.50→$10.50 | 6 | 16.6 mo | inbound | no | +11% | -35% | -77% | -78% |
| Entasis Therapeutics Holdings Inc. | ETTX | Innoviva, Inc. | 2022-05-23 | $105M | 17% | Phase 3 lead + Phase 3 pipeline | $1.80→$2.20 | 35 | 3.7 mo | both | yes | +8% | -29% | -6% | -32% |
| TherapeuticsMD, Inc. | TXMD | EW Healthcare Partners | 2022-05-31 | $88M | 367% | Commercial with 3 approved drugs (IMVEXXY, ANNOVERA, BIJUVA) | $10.00→$10.00 | 83 | 4.5 mo | outbound | no | -29% | -73% | -83% | -83% |
| Turning Point Therapeutics, Inc. | TPTX | Bristol-Myers Squibb Compa | 2022-06-03 | $3.8B | 184% | Phase 1/2 (Registrational) lead asset | $58.00→$76.00 | 33 | 4.7 mo | outbound | no | -25% | -36% | -65% | -57% |
| Radius Health, Inc. | RDUS | Ginger Acquisition Inc. | 2022-06-23 | $476M | 60% | Commercial + Phase 2/3 pipeline | $9.00→$10.00 | 70 | 4.9 mo | outbound | no | -10% | -64% | -70% | -56% |
| Epizyme, Inc. | EPZM | Ipsen S.A. | 2022-06-27 | $244M | 222% | Commercial + Phase 3 confirmatory | $1.10→$1.45 | 38 | 6.8 mo | inbound | no | -70% | -87% | -95% | -97% |
| LA JOLLA PHARMACEUTICAL CO | LJPC | Innoviva, Inc. | 2022-07-11 | $155M | 80% | 2 approved drugs / Commercial | $4.90→$6.23 | 25 | 3.7 mo | both | no | -16% | -24% | -32% | -26% |
| Forma Therapeutics Holdings, Inc. | FMTX | Novo Nordisk A/S | 2022-09-01 | $957M | 142% | Phase 2/3 lead + NDA stage oncology asset | $8.20→$20.00 | 4 | 20.0 mo | inbound | no | +10% | -28% | -64% | -79% |
| LogicBio Therapeutics, Inc. | LOGC | AstraZeneca PLC | 2022-10-03 | $68M | 71% | Phase 1/2 lead + Preclinical platform | $1.56→$2.07 | 2 | 11.8 mo | inbound | no | -32% | -36% | -83% | -95% |
| Akouos, Inc. | AKUS | Eli Lilly and Company | 2022-10-18 | $462M | 142% | Phase 1/2 (IND cleared) lead asset | $9.00→$12.50 | 4 | 7.8 mo | inbound | no | +43% | +8% | -59% | -74% |
| Applied Genetic Technologies Corpo | AGTC | Syncona Limited | 2022-10-24 | $23M | 17% | Phase 1/2 lead + clinical ocular portfolio | $0.34→$1.07 | 33 | 4.1 mo | outbound | no | -53% | -76% | -91% | -94% |
| Oyster Point Pharma, Inc. | OYST | Viatris Inc. | 2022-11-07 | $299M | 55% | Approved/Marketed lead asset + Phase 2 pipeline | $10.00→$11.00 | 9 | 12.2 mo | both | no | +56% | -20% | -36% | -71% |
| Imago BioSciences, Inc. | IMGO | Merck & Co., Inc. | 2022-11-21 | $1.2B | 137% | Phase 2 lead asset | $28.00→$36.00 | 11 | 21.8 mo | both | no | -13% | -15% | -42% | — |
| ALBIREO PHARMA, INC. | ALBO | Ipsen S.A. | 2023-01-09 | $876M | 97% | Marketed + Phase 3 lead | $28.00→$42.00 | 4 | 1.8 mo | both | no | +13% | +6% | -1% | -40% |
| CinCor Pharma, Inc. | CINC | AstraZeneca PLC | 2023-01-09 | $1.1B | 118% | Phase 2 lead, pre-revenue | $22.00→$26.00 | 3 | 20.0 mo | inbound | no | -60% | -19% | -25% | — |
| Concert Pharmaceuticals, Inc. | CNCE | Sun Pharmaceutical Industr | 2023-01-19 | $498M | 70% | Phase 3 lead asset | $7.00→$8.00 | 40 | 6.3 mo | both | no | -26% | +15% | +41% | -56% |
| CHEMBIO DIAGNOSTICS, INC. | CEMI | Biosynex SA | 2023-01-31 | $16M | 105% | Commercial + EUA Revoked | $0.40→$0.45 | 81 | 8.3 mo | outbound | no | -39% | -66% | -81% | -97% |
| Provention Bio, Inc. | PRVB | Sanofi S.A. | 2023-03-13 | $2.4B | 140% | Approved / Commercial lead asset + Phase 2 pipeline | $21.00→$25.00 | 1 | 15.4 mo | inbound | no | +25% | +85% | +64% | -22% |
| Jounce Therapeutics, Inc. | JNCE | Concentra Biosciences, LLC | 2023-03-27 | $97M | 36% | Phase 2 lead + multiple clinical/preclinical assets | $1.80→$1.85 | 3 | 0.4 mo | both | no | — | — | — | — |
| Satsuma Pharmaceuticals, Inc. | STSA | Shin Nippon Biomedical Lab | 2023-04-16 | $30M | 12% | Phase 3 lead (failed) + NDA Accepted | $0.91→$0.91 | 30 | 4.3 mo | outbound | no | -14% | -88% | -79% | -84% |
| CTI BIOPHARMA CORP | CTIC | Swedish Orphan Biovitrum A | 2023-05-10 | $1.2B | 115% | Commercial / Phase 3 (label expansion) | $8.00→$9.10 | 4 | 2.9 mo | inbound | no | -22% | -21% | -12% | +94% |
| VectivBio Holding AG | VECT | Ironwood Pharmaceuticals,  | 2023-05-22 | $1.1B | 56% | Phase 3 lead asset | $14.00→$17.00 | 8 | 2.0 mo | inbound | no | +42% | +47% | +113% | -27% |
| GreenLight Biosciences Holdings, P | GRNA | SW ParentCo, Inc. | 2023-05-30 | $46M | -6% | Pre-revenue, Launch 2024 (Agricultural) + Pre-clinical/Phase 1 (Human Health) | $0.30→$0.30 | 140 | 3.2 mo | both | yes | -70% | -82% | -96% | — |
| Sigilon Therapeutics, Inc. | SGTX | Eli Lilly and Company | 2023-06-29 | $37M | 204% | Pre-clinical lead + Phase 1/2 clinical hold | $14.92→$14.92 | 141 | 63.0 mo | both | no | +463% | +965% | +505% | -53% |
| PARDES BIOSCIENCES, INC. | PRDS | MediPacific, Inc. | 2023-07-17 | $132M | 13% | Phase 2, suspended development | $1.93→$2.13 | 144 | 2.9 mo | both | no | +43% | +54% | -61% | -81% |
| Decibel Therapeutics, Inc. | DBTX | Regeneron Pharmaceuticals, | 2023-08-09 | $101M | 14% | Phase 1/2 lead, pre-revenue | $3.25→$4.00 | 5 | 4.3 mo | both | no | +13% | +38% | -30% | -53% |
| Thorne HealthTech, Inc. | THRN | Healthspan Buyer, LLC | 2023-08-28 | $551M | 72% | Commercial + OneDraw Regulatory Approval Pending | $7.00→$10.20 | 38 | 8.2 mo | both | no | +34% | +33% | +14% | -29% |
| INTERCEPT PHARMACEUTICALS, INC. | ICPT | Alfasigma S.p.A. | 2023-09-26 | $794M | 76% | Marketed (Conditional Approval) + Phase 2 | $12.00→$19.00 | 18 | 3.1 mo | both | no | +5% | -45% | -40% | -29% |
| POINT Biopharma Global Inc. | PNT | Eli Lilly and Company | 2023-10-03 | $1.3B | 53% | Phase 3 lead | $12.00→$12.50 | 3 | 3.6 mo | inbound | no | -12% | +7% | -20% | +12% |
| Miromatrix Medical Inc. | MIRO | United Therapeutics Corpor | 2023-10-30 | $89M | 148% | Preclinical, bioengineered organ technology | $2.75→$5.00 | 51 | 3.5 mo | outbound | no | -25% | -22% | -70% | -84% |
| Icosavax, Inc. | ICVX | AstraZeneca PLC | 2023-12-12 | $762M | 119% | Phase 2 lead, Pre-revenue | $12.00→$15.00 | 14 | 16.7 mo | both | no | -12% | -15% | +175% | -72% |
| Theseus Pharmaceuticals, Inc. | THRX | Concentra Biosciences, LLC | 2023-12-22 | $181M | 12% | Preclinical/Early Clinical, lead asset discontinued | $3.80→$4.05 | 71 | 0.9 mo | both | yes | +16% | -67% | -45% | -68% |
| RayzeBio, Inc. | RYZB | Bristol-Myers Squibb Compa | 2023-12-26 | $3.8B | 173% | Phase 3 lead asset | $36.00→$62.50 | 4 | 1.6 mo | inbound | no | -5% | — | — | — |
| MorphoSys AG | MOR | Novartis AG | 2024-02-05 | $2.6B | 89% | Phase 3 lead oncology pipeline | $68.00→$68.00 | 2 | 2.3 mo | inbound | no | +57% | +24% | +149% | +30% |
| CymaBay Therapeutics, Inc. | CBAY | Gilead Sciences, Inc. | 2024-02-12 | $3.7B | 37% | Phase 3 lead asset | $23.00→$32.50 | 22 | 13.9 mo | inbound | no | +76% | +105% | +265% | +603% |
| Kinnate Biopharma Inc. | KNTE | XOMA Corporation | 2024-02-16 | $122M | 8% | Clinical stage, Phase 1 lead asset | $2.17→$2.59 | 119 | 3.1 mo | outbound | no | +110% | -22% | -63% | -73% |
| NGM Biopharmaceuticals, Inc. | NGM | The Column Group, LP (TCG) | 2024-02-26 | $129M | 4% | Clinical-stage, Phase 2 lead | $1.45→$1.55 | 8 | 8.0 mo | inbound | no | +94% | -35% | -71% | -90% |
| Societal CDMO, Inc. | SCTL | CoreRx, Inc. | 2024-02-28 | $116M | 214% | Commercial CDMO services + legacy products | $0.42→$1.10 | 4 | 4.1 mo | outbound | no | +0% | -60% | -74% | -80% |
| ALPINE IMMUNE SCIENCES, INC. | ALPN | Vertex Pharmaceuticals Inc | 2024-04-10 | $4.3B | 81% | Phase 1b/2a, Phase 3 planned | $60.00→$65.00 | 5 | 12.1 mo | both | no | +113% | +188% | +397% | +349% |
| Deciphera Pharmaceuticals, Inc. | DCPH | ONO Pharmaceutical Co., Lt | 2024-04-29 | $2.2B | 63% | Phase 3 lead + 1 approved drug | $19.00→$25.60 | 5 | 22.5 mo | inbound | no | -2% | +24% | +2% | +62% |
| Calliditas Therapeutics AB (publ) | CALT | Asahi Kasei Corporation | 2024-05-28 | $12.5B | 83% | Commercial | $131.00→$208.00 | 4 | 13.5 mo | both | no | -14% | +21% | -16% | +2% |
| Morphic Holding, Inc. | MORF | Eli Lilly and Company | 2024-07-08 | $2.9B | 85% | Phase 2b lead asset | $46.00→$57.00 | 3 | 42.3 mo | both | no | -17% | +13% | -50% | +27% |
| G1 Therapeutics, Inc. | GTHX | Pharmacosmos A/S | 2024-08-07 | $378M | 185% | Phase 3 lead + 1 approved drug | $2.25→$7.15 | 14 | 20.2 mo | both | no | -47% | -14% | +4% | -80% |
| Revance Therapeutics, Inc. | RVNC | Crown Holdings Interco LLC | 2024-08-12 | $383M | 2% | Commercial-stage, 2 primary products (DAXXIFY + RHA Collection) | $2.25→$6.66 | 16 | 9.0 mo | both | no | -13% | -40% | -84% | -82% |
| Longboard Pharmaceuticals, Inc. | LBPH | H. Lundbeck A/S | 2024-10-14 | $2.3B | 75% | Phase 3 ready lead asset | $29.00→$60.00 | 2 | 10.3 mo | inbound | no | +85% | +78% | +451% | +1014% |
| Lumos Pharma, Inc. | LUMO | Double Point Ventures LLC | 2024-10-23 | $37M | 8% | Phase 3 ready, lead asset LUM-201 | $2.83→$4.25 | 51 | 9.7 mo | both | no | +76% | +41% | +34% | -57% |
| Poseida Therapeutics, Inc. | PSTV | F. Hoffmann-La Roche Ltd | 2024-11-26 | $880M | 215% | Phase 1/1b lead assets | $5.75→$9.00 | 4 | 44.7 mo | both | no | -28% | -20% | +26% | +221% |
| MARINUS PHARMACEUTICALS, INC. | MRNS | Immedica Pharma AB | 2024-12-30 | $30M | 72% | Commercial (CDD) + Phase 3 failures (RSE/TSC) | $0.50→$0.55 | 77 | 1.4 mo | outbound | no | -77% | -77% | -96% | -93% |
| bluebird bio, Inc. | BLUE | Beacon Parent Holdings, L. | 2025-02-21 | $29M | -62% | Commercial with 3 approved gene therapies | $3.00→$5.00 | 103 | 3.3 mo | both | no | +1525% | +643% | +519% | +52% |
| Chimerix, Inc. | CMRX | Jazz Pharmaceuticals Publi | 2025-03-05 | $802M | 117% | Phase 3 lead + NDA accepted with priority review | $5.00→$8.55 | 8 | 2.7 mo | both | no | +298% | +380% | +324% | +190% |
| 2seventy bio, Inc. | TSVT | Bristol-Myers Squibb Compa | 2025-03-10 | $266M | 117% | Commercial (Abecma) | $4.75→$5.00 | 3 | 25.3 mo | both | no | -51% | -45% | -62% | -77% |
| Allakos Inc. | ALLK | Concentra Biosciences, LLC | 2025-04-02 | $30M | 18% | Phase 1 failure, lead asset discontinued | $0.32→$0.33 | 42 | 1.3 mo | outbound | yes | -73% | -61% | -83% | -94% |
| Regulus Therapeutics Inc. | RGLS | Novartis AG | 2025-04-30 | $529M | 305% | Phase 1b lead asset | $2.50→$7.00 | 5 | 3.6 mo | outbound | no | +12% | +7% | -40% | +23% |
| Kronos Bio, Inc. | KRON | Concentra Biosciences, LLC | 2025-05-01 | $35M | -30% | Pre-clinical lead + discontinued Phase 1/2 | $0.57→$0.57 | 25 | 1.4 mo | outbound | no | -13% | -16% | -37% | -57% |
| Inozyme Pharma, Inc. | INZY | BioMarin Pharmaceutical In | 2025-05-16 | $260M | 335% | Phase 3 lead asset | $1.75→$4.00 | 2 | 12.3 mo | both | no | -32% | -82% | -82% | -86% |
| Blueprint Medicines Corporation | BPMC | SANOFI | 2025-06-02 | $8.4B | 23% | Approved drug + Phase 2/3 lead | $124.00→$129.00 | 5 | 12.3 mo | both | no | -7% | +15% | -2% | +79% |
| Elevation Oncology, Inc. | ELEV | Concentra Biosciences, LLC | 2025-06-09 | $21M | 6% | Preclinical/Early Clinical, lead asset discontinued | $0.36→$0.36 | 23 | 1.5 mo | outbound | no | -46% | -48% | -90% | -77% |
| CureVac N.V. | CVAC | BioNTech SE | 2025-06-12 | $1.2B | 57% | Clinical/Pre-clinical oncology and infectious disease | —→$1,250,000,000.00 | 1 | 4.0 mo | both | no | -3% | +22% | +19% | -66% |
| Verve Therapeutics, Inc. | VERV | Eli Lilly and Company | 2025-06-17 | $938M | 127% | Phase 1b lead asset | $10.00→$10.50 | 8 | 7.0 mo | both | no | -46% | -3% | -23% | -75% |
| Turnstone Biologics Corp. | TSBX | XOMA Royalty Corporation | 2025-06-27 | $8M | 3% | Phase 1 (Discontinued), Pre-revenue | $0.34→$0.34 | 43 | 2.4 mo | outbound | no | -15% | -31% | -87% | -97% |
| IGM Biosciences, Inc. | IGMS | Tang Capital Partners, LP | 2025-07-01 | $75M | -2% | Pre-revenue, Phase 1b (discontinued lead) | $1.20→$1.25 | 10 | 1.3 mo | outbound | no | -7% | -87% | -85% | -87% |
| CARGO Therapeutics, Inc. | CRGX | Tang Capital Partners, LP | 2025-07-08 | $204M | -8% | Phase 2 (Discontinued) + Preclinical | $4.38→$4.55 | 157 | 3.4 mo | outbound | no | +20% | -74% | -74% | — |
| iTeos Therapeutics, Inc. | ITOS | Tang Capital Partners, LP | 2025-07-21 | $444M | 1% | Phase 2 lead (terminated) + clinical assets | $8.50→$10.05 | 20 | 1.3 mo | both | no | +45% | +34% | -33% | -29% |
| DURECT CORPORATION | DRRX | Bausch Health Companies In | 2025-07-29 | $54M | 178% | Phase 3 ready lead asset | $1.75→$1.75 | 1 | 18.1 mo | inbound | no | -21% | -34% | -51% | -81% |
| HilleVax, Inc. | HLVX | XOMA Royalty Corporation | 2025-08-04 | $98M | -5% | Phase 2b lead (discontinued) + clinical-stage pipeline | $1.95→$1.95 | 33 | 5.4 mo | outbound | no | +45% | -1% | -85% | -86% |
| LAVA Therapeutics N.V. | LVTX | XOMA Royalty Corporation | 2025-08-04 | $27M | -21% | Clinical stage + partnered programs | $1.04→$1.16 | 100 | 5.8 mo | outbound | no | +14% | +25% | -30% | -20% |
| Y-mAbs Therapeutics, Inc. | YMAB | SERB Pharmaceuticals (Star | 2025-08-05 | $391M | 100% | Marketed lead asset + Clinical platform | $7.80→$8.60 | 30 | 6.0 mo | both | no | -5% | -47% | -62% | -23% |
| scPharmaceuticals Inc. | SCPH | MannKind Corporation | 2025-08-25 | $288M | -4% | Commercial (FUROSCIX) + Phase 3 (SCP-111) | $4.50→$5.35 | 26 | 3.6 mo | both | no | +123% | +70% | +13% | -25% |
| Tourmaline Bio, Inc. | TRML | Novartis AG | 2025-09-09 | $1.2B | 132% | Phase 2 lead asset | $25.00→$48.00 | 12 | 1.6 mo | both | no | +37% | +45% | +48% | +653% |
| 89bio, Inc. | ETNB | Roche Holdings, Inc. | 2025-09-18 | $2.3B | 57% | Phase 3 lead asset | $13.00→$14.50 | 1 | 29.8 mo | outbound | no | +19% | -13% | +15% | -42% |
| Merus N.V. | MRUS | Genmab A/S | 2025-09-29 | $7.4B | 47% | Phase 2, clinical-stage oncology | $81.00→$97.00 | 5 | 1.7 mo | both | no | +17% | +40% | +29% | +201% |
| Adverum Biotechnologies, Inc. | ADVM | Eli Lilly and Company | 2025-10-24 | $79M | -21% | Phase 3 lead, pre-revenue | $3.24→$3.56 | 30 | 24.5 mo | outbound | no | +94% | -12% | -40% | +375% |
| Evoke Pharma, Inc. | EVOK | QOL Medical, LLC | 2025-11-04 | $19M | 141% | FDA-approved / Commercial | $7.50→$11.00 | 3 | 6.9 mo | outbound | no | +68% | +103% | -13% | +266% |
| Mersana Therapeutics, Inc. | MRSN | Day One Biopharmaceuticals | 2025-11-13 | $125M | 171% | Phase 1 lead, pre-revenue | $12.00→$25.00 | 33 | 8.1 mo | outbound | no | +2618% | +2881% | +369% | +496% |
| Cidara Therapeutics, Inc. | CDTX | Merck & Co., Inc. | 2025-11-14 | $7.0B | 118% | Phase 3 lead, Pre-revenue | $118.00→$221.50 | 7 | 12.1 mo | both | no | +69% | +458% | +857% | +12915% |
| Applied Therapeutics, Inc. | APLT | Cycle Group Holdings Limit | 2025-12-11 | $14M | -90% | NDA / Phase 3 lead, pre-revenue | $0.09→$0.09 | 9 | 10.4 mo | both | no | +98% | +112% | -92% | -71% |
| Generation Bio Co. | GBIO | XOMA Royalty Corporation | 2025-12-15 | $29M | -21% | Preclinical lead + Moderna research collaboration | $2.15→$4.29 | 71 | 1.9 mo | outbound | no | -14% | +1326% | +252% | +184% |
| Dynavax Technologies Corporation | DVAX | Sanofi | 2025-12-24 | $1.8B | 39% | Commercial + Phase 1/2 lead pipeline | $14.40→$15.50 | 3 | 12.4 mo | both | yes | +6% | +14% | -10% | -20% |
| RAPT Therapeutics, Inc. | RAPT | GSK plc | 2026-01-20 | $1.8B | 72% | Phase 2b lead asset, pre-revenue | $50.00→$58.00 | 10 | 3.7 mo | both | no | +70% | +355% | +4023% | +34% |
| Arcellx, Inc. | ACLX | Gilead Sciences, Inc. | 2026-02-23 | $6.7B | 70% | Phase 3 lead + clinical stage assets | $98.00→$115.00 | 2 | 0.3 mo | inbound | no | -20% | -5% | +7% | +1% |
| Day One Biopharmaceuticals, Inc. | DAWN | Servier S.A.S. | 2026-03-06 | $2.2B | 88% | Commercial / Phase 3 lead | $13.00→$21.50 | 3 | 1.7 mo | inbound | no | +17% | +72% | -8% | -27% |
| Lisata Therapeutics, Inc. | LSTA | Kuva Labs Inc. | 2026-03-06 | $36M | -12% | Phase 2a lead asset | $4.00→$4.00 | 1 | 15.2 mo | inbound | no | +120% | +82% | +82% | +43% |
| Terns Pharmaceuticals, Inc. | TERN | Merck & Co., Inc. | 2026-03-25 | $6.1B | 35% | Phase 1/2 lead asset | $50.00→$53.00 | 2 | 1.9 mo | both | no | +49% | +466% | +881% | +498% |
| Kezar Life Sciences, Inc. | KZR | Aurinia Pharmaceuticals In | 2026-03-30 | $51M | 4% | Phase 2 lead (discontinued) + Phase 1 oncology | $1.10→$6.96 | 77 | 17.7 mo | both | no | +8% | +70% | +17% | +738% |
| Apellis Pharmaceuticals, Inc. | APLS | Biogen Inc. | 2026-03-31 | $5.2B | 96% | 2 approved drugs (SYFOVRE and EMPAVELI) | $26.00→$41.00 | 8 | 18.3 mo | both | yes | -2% | -24% | -17% | -63% |
| Soleno Therapeutics, Inc. | SLNO | Neurocrine Biosciences, In | 2026-04-06 | $2.7B | 34% | Commercial-stage, 1 approved drug | $50.00→$53.00 | 11 | 1.8 mo | both | no | -23% | -43% | -11% | +5% |
| KalVista Pharmaceuticals, Inc. | KALV | Chiesi Farmaceutici S.p.A. | 2026-04-29 | $1.4B | 40% | Approved / Commercial | $21.00→$27.00 | 4 | 3.5 mo | both | yes | +27% | +56% | +62% | +59% |
| Assertio Holdings, Inc. | ASRT | Zydus Worldwide DMCC | 2026-05-13 | $152M | 30% | Commercial (Rolvedon) + Divested mature assets | $13.50→$23.50 | 30 | 0.9 mo | outbound | no | +96% | +2071% | +2806% | +1584% |
| Pfizer Acquisition of King Pharmac | — |  | — | — | — | Commercial stage with specialty portfolio and EpiPen franchise | $12.00→$14.25 | 5 | — | inbound | no | — | — | — | — |

## Per-Deal Detail

### SCHERING AKTIENGESELLSCHAFT (no_ticker)
- **Acquirer:** Bayer Aktiengesellschaft
- **Announced / Closed:** 2006-03-23 / 2006-10-27
- **Deal size:** $17.3B  ·  $89.36/sh
- **Premium (vs unaffected):** —
- **Stage:** Marketed products + Pipeline
- **Value-inflecting events:** Merck KGaA unsolicited EUR 77.00 bid; Bayer AG friendly EUR 86.00 counter-offer; Bayer purchase of 21.8% stake from Merck; Domination Agreement and Mandatory Offer
- **Offer range (low→high):** $77.00 → $89.36
- **Interested parties:** 3
- **Interest direction:** inbound
- **Engagement → deal:** 0.3 months
- **Reported early (1mo+):** yes — PharmaTimes + recurring rumors since early 2000s
- **Trailing return to unaffected:** 3mo — · 6mo — · 12mo — · 2yr —

### VIRBAC CORPORATION (VBAC)
- **Acquirer:** Virbac S.A.
- **Announced / Closed:** 2006-08-08 / 2006-11-01
- **Deal size:** $130M  ·  $5.75/sh
- **Premium (vs unaffected):** 37%
- **Stage:** Commercial + R&D pipeline
- **Value-inflecting events:** —
- **Offer range (low→high):** $4.15 → $5.75
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 7.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -4% · 6mo -5% · 12mo +61% · 2yr +64%

### AnorMED Inc. (ANOR)
- **Acquirer:** Genzyme Corporation
- **Announced / Closed:** 2006-08-30 / 2006-11-07
- **Deal size:** $567M  ·  $13.50/sh
- **Premium (vs unaffected):** 111%
- **Stage:** Phase 3 lead + Phase 1/2 clinical
- **Value-inflecting events:** Genzyme unsolicited $8.55 bid; Millennium $12.00 white knight agreement
- **Offer range (low→high):** $8.55 → $12.00
- **Interested parties:** 3
- **Interest direction:** both
- **Engagement → deal:** 11.0 months
- **Reported early (1mo+):** yes — BioWorld Today/The Street + 10 months early
- **Trailing return to unaffected:** 3mo -6% · 6mo +12% · 12mo — · 2yr —

### Myogen, Inc. (MYOG)
- **Acquirer:** Gilead Sciences, Inc.
- **Announced / Closed:** 2006-10-02 / 2006-11-17
- **Deal size:** $2.3B  ·  $52.50/sh
- **Premium (vs unaffected):** 50%
- **Stage:** Phase 3 lead + Phase 2b
- **Value-inflecting events:** Phase 3 ambrisentan results; GSK collaboration agreement
- **Offer range (low→high):** $44.00 → $52.50
- **Interested parties:** 3
- **Interest direction:** both
- **Engagement → deal:** 6.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +10% · 6mo -15% · 12mo +71% · 2yr +322%

### KOS PHARMACEUTICALS INC (KOSP)
- **Acquirer:** Abbott Laboratories
- **Announced / Closed:** 2006-11-06 / 2006-12-13
- **Deal size:** $3.7B  ·  $78.00/sh
- **Premium (vs unaffected):** 60%
- **Stage:** Marketed products + Phase 3 pipeline
- **Value-inflecting events:** —
- **Offer range (low→high):** $60.00 → $78.00
- **Interested parties:** 10
- **Interest direction:** both
- **Engagement → deal:** 1.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +26% · 6mo +9% · 12mo -24% · 2yr +11%

### COTHERIX INC (CTRX)
- **Acquirer:** Actelion Ltd.
- **Announced / Closed:** 2006-11-19 / 2007-01-09
- **Deal size:** $389M  ·  $13.50/sh
- **Premium (vs unaffected):** 249%
- **Stage:** Marketed lead asset + Phase 2
- **Value-inflecting events:** Ventavis (iloprost) marketing approval; ACTIVE Trial Phase 2 initiation
- **Offer range (low→high):** $10.00 → $13.50
- **Interested parties:** 3
- **Interest direction:** inbound
- **Engagement → deal:** 3.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +33% · 6mo — · 12mo — · 2yr —

### PRAECIS PHARMACEUTICALS INCORPORATED (PRCS)
- **Acquirer:** GlaxoSmithKline plc
- **Announced / Closed:** 2006-12-21 / 2007-02-16
- **Deal size:** $54M  ·  $5.00/sh
- **Premium (vs unaffected):** 140%
- **Stage:** Phase 1 lead + 1 marketed drug (EU)
- **Value-inflecting events:** Strategic restructuring and 60% workforce reduction; Execution of Pilot Study and Option Agreement with GSK; Engagement of Canaccord Adams for strategic options; Divestiture of Plenaxis assets to SEP
- **Offer range (low→high):** $4.29 → $5.00
- **Interested parties:** 100
- **Interest direction:** both
- **Engagement → deal:** 14.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +4% · 6mo -61% · 12mo -48% · 2yr -77%

### NEW RIVER PHARMACEUTICALS INC (NRPH)
- **Acquirer:** Shire plc
- **Announced / Closed:** 2007-02-20 / 2007-04-19
- **Deal size:** $2.4B  ·  $64.00/sh
- **Premium (vs unaffected):** 15%
- **Stage:** Approved lead asset (VYVANSE)
- **Value-inflecting events:** VYVANSE FDA approval Feb 23, 2007; 74.8% share price increase Oct 2006
- **Offer range (low→high):** $61.50 → $64.00
- **Interested parties:** 15
- **Interest direction:** both
- **Engagement → deal:** 24.7 months
- **Reported early (1mo+):** yes — The Economic Times/Bloomberg + 1 month early
- **Trailing return to unaffected:** 3mo +17% · 6mo +120% · 12mo +67% · 2yr +364%

### MedImmune, Inc. (MEDI)
- **Acquirer:** AstraZeneca PLC
- **Announced / Closed:** 2007-04-23 / 2007-06-18
- **Deal size:** $13.8B  ·  $58.00/sh
- **Premium (vs unaffected):** 70%
- **Stage:** Marketed products + Phase 3 lead
- **Value-inflecting events:** Public announcement of strategic review; News leak regarding sale process; AstraZeneca final binding proposal
- **Offer range (low→high):** $50.00 → $58.00
- **Interested parties:** 20
- **Interest direction:** outbound
- **Engagement → deal:** 1.0 months
- **Reported early (1mo+):** yes — FierceBiotech/Washington Business Journal reported sale pressure 4 months early
- **Trailing return to unaffected:** 3mo +7% · 6mo +19% · 12mo -6% · 2yr +34%

### BIOENVISION, INC. (BIVN)
- **Acquirer:** Genzyme Corporation
- **Announced / Closed:** 2007-05-29 / 2007-10-10
- **Deal size:** $308M  ·  $5.60/sh
- **Premium (vs unaffected):** 51%
- **Stage:** Marketed lead asset + Phase 3
- **Value-inflecting events:** Clofarabine European approval; SRI Amendment improving economic terms; Genzyme withdrawal from 2006 discussions; Company A non-binding proposal
- **Offer range (low→high):** $5.25 → $5.60
- **Interested parties:** 21
- **Interest direction:** both
- **Engagement → deal:** 35.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -23% · 6mo -31% · 12mo -43% · 2yr -40%

### DIGENE CORPORATION (DIGE)
- **Acquirer:** QIAGEN N.V.
- **Announced / Closed:** 2007-06-03 / 2007-07-30
- **Deal size:** $1.5B  ·  $61.25/sh
- **Premium (vs unaffected):** 33%
- **Stage:** Marketed diagnostic franchise
- **Value-inflecting events:** Merger announcement with QIAGEN
- **Offer range (low→high):** $58.00 → $61.25
- **Interested parties:** 12
- **Interest direction:** both
- **Engagement → deal:** 4.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -8% · 6mo -3% · 12mo +7% · 2yr +84%

### Coley Pharmaceutical Group, Inc. (COLY)
- **Acquirer:** Pfizer Inc.
- **Announced / Closed:** 2007-11-16 / 2008-01-04
- **Deal size:** $214M  ·  $8.00/sh
- **Premium (vs unaffected):** 169%
- **Stage:** Phase 2/3 lead + clinical adjuvant platform
- **Value-inflecting events:** Pfizer discontinues two Phase III trials of PF-3512676; Coley and Pfizer enter license agreement for PF-3512676
- **Offer range (low→high):** $6.25 → $8.00
- **Interested parties:** 3
- **Interest direction:** outbound
- **Engagement → deal:** 4.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -11% · 6mo -70% · 12mo -77% · 2yr -81%

### NATROL, INC. (NTOL)
- **Acquirer:** Plethico Pharmaceuticals Limited
- **Announced / Closed:** 2007-11-18 / 2007-12-28
- **Deal size:** $63M  ·  $4.40/sh
- **Premium (vs unaffected):** 40%
- **Stage:** Commercial, multiple marketed nutraceutical brands
- **Value-inflecting events:** Acquisition of Nu Hair and Shen Min brands; Acquisition of Medical Research Institute (MRI); Disappointing Q3 financial results
- **Offer range (low→high):** $3.50 → $4.40
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 7.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -21% · 6mo +1% · 12mo +57% · 2yr +34%

### Adams Respiratory Therapeutics, Inc. (ARXT)
- **Acquirer:** Reckitt Benckiser Group plc
- **Announced / Closed:** 2007-12-10 / 2008-01-29
- **Deal size:** $2.2B  ·  $60.00/sh
- **Premium (vs unaffected):** 39%
- **Stage:** Commercial consumer healthcare portfolio
- **Value-inflecting events:** —
- **Offer range (low→high):** $48.00 → $60.00
- **Interested parties:** 10
- **Interest direction:** both
- **Engagement → deal:** 2.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +4% · 6mo +11% · 12mo +2% · 2yr +1%

### MGI PHARMA INC (MOGN)
- **Acquirer:** Eisai Co., Ltd.
- **Announced / Closed:** 2007-12-10 / 2008-01-28
- **Deal size:** $3.3B  ·  $41.00/sh
- **Premium (vs unaffected):** 37%
- **Stage:** 2 marketed drugs + NDA filing
- **Value-inflecting events:** Aloxi and Dacogen commercialization; Saforis NDA filing; Strategic review announcement
- **Offer range (low→high):** $33.00 → $41.00
- **Interested parties:** 19
- **Interest direction:** inbound
- **Engagement → deal:** 14.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +33% · 6mo +40% · 12mo +58% · 2yr +79%

### ENCYSIVE PHARMACEUTICALS INC (ENCY)
- **Acquirer:** Pfizer Inc.
- **Announced / Closed:** 2008-02-20 / 2008-06-10
- **Deal size:** $190M  ·  $2.35/sh
- **Premium (vs unaffected):** 246%
- **Stage:** Marketed (EU/AU/CA), Phase 3 (US)
- **Value-inflecting events:** Third FDA approvable letter for THELIN; Board forms Strategic Options Committee; Morgan Stanley engaged for sale process; Receipt of eleven preliminary bids
- **Offer range (low→high):** $1.25 → $2.35
- **Interested parties:** 70
- **Interest direction:** outbound
- **Engagement → deal:** 4.4 months
- **Reported early (1mo+):** yes — GlobeNewswire/24/7 Wall St. 7-8 months early
- **Trailing return to unaffected:** 3mo -53% · 6mo -67% · 12mo -82% · 2yr -93%

### COLLAGENEX PHARMACEUTICALS INC (CGPI)
- **Acquirer:** Galderma Pharma S.A.
- **Announced / Closed:** 2008-02-26 / 2008-04-10
- **Deal size:** $358M  ·  $16.60/sh
- **Premium (vs unaffected):** 41%
- **Stage:** Marketed lead asset (Oracea)
- **Value-inflecting events:** Oracea commercialization; Galderma acquisition proposal
- **Offer range (low→high):** $12.50 → $16.60
- **Interested parties:** 14
- **Interest direction:** both
- **Engagement → deal:** 31.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +14% · 6mo -4% · 12mo -19% · 2yr -12%

### Millennium Pharmaceuticals, Inc. (MLNM)
- **Acquirer:** Takeda Pharmaceutical Company Limited
- **Announced / Closed:** 2008-04-10 / 2008-05-14
- **Deal size:** $8.2B  ·  $25.00/sh
- **Premium (vs unaffected):** 91%
- **Stage:** Marketed lead asset + Phase 2 and IND pipeline
- **Value-inflecting events:** VELCADE approval/label expansion; Transition to profitability in 2008; Eisai acquisition of MGI Pharma (sector tailwind)
- **Offer range (low→high):** $23.00 → $25.00
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 9.0 months
- **Reported early (1mo+):** yes — Reuters/Forbes/Bloomberg reported Japanese firm interest 3-4 months early
- **Trailing return to unaffected:** 3mo -13% · 6mo +31% · 12mo +23% · 2yr +39%

### Sirtris Pharmaceuticals, Inc. (SIRT)
- **Acquirer:** GlaxoSmithKline plc
- **Announced / Closed:** 2008-04-22 / 2008-06-05
- **Deal size:** $658M  ·  $22.50/sh
- **Premium (vs unaffected):** 109%
- **Stage:** Clinical/Pre-clinical SIRT1 activation platform
- **Value-inflecting events:** —
- **Offer range (low→high):** $18.50 → $22.50
- **Interested parties:** 2
- **Interest direction:** both
- **Engagement → deal:** 26.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -23% · 6mo -35% · 12mo -14% · 2yr —

### USANA HEALTH SCIENCES, INC. (USNA)
- **Acquirer:** Gull-Unity Holding Corp.
- **Announced / Closed:** 2008-05-13 / —
- **Deal size:** $426M  ·  $26.00/sh
- **Premium (vs unaffected):** 23%
- **Stage:** Marketed nutritional supplements
- **Value-inflecting events:** —
- **Offer range (low→high):** $26.00 → $26.00
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 11.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -57% · 6mo -52% · 12mo -49% · 2yr -43%

### Third Wave Technologies, Inc. (TWTI)
- **Acquirer:** Hologic, Inc.
- **Announced / Closed:** 2008-06-09 / 2008-07-17
- **Deal size:** $510M  ·  $11.25/sh
- **Premium (vs unaffected):** 33%
- **Stage:** PMA Submission (HPV tests) + FDA Cleared (Cystic Fibrosis)
- **Value-inflecting events:** Achievement of clinical endpoints in HPV test trials; PMA Submission for HPV Cervista High Risk screening assay
- **Offer range (low→high):** $4.75 → $11.25
- **Interested parties:** 11
- **Interest direction:** both
- **Engagement → deal:** 2.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +6% · 6mo -5% · 12mo +65% · 2yr +206%

### TARO PHARMACEUTICAL INDUSTRIES LTD. (TARO)
- **Acquirer:** Sun Pharmaceutical Industries Ltd.
- **Announced / Closed:** 2008-06-25 / —
- **Deal size:** $306M  ·  $7.75/sh
- **Premium (vs unaffected):** -7%
- **Stage:** Commercial, generic product pipeline
- **Value-inflecting events:** 2007 dramatic financial turnaround; Termination of 2007 Merger Agreement; Sun purchase of Brandes block at $10.25; Sun purchase of Harel block at $9.50
- **Offer range (low→high):** $7.75 → $7.75
- **Interested parties:** 4
- **Interest direction:** inbound
- **Engagement → deal:** 29.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -1% · 6mo +15% · 12mo +11% · 2yr -22%

### GENENTECH INC (DNA)
- **Acquirer:** Roche Holding Ltd
- **Announced / Closed:** 2008-07-21 / 2009-03-26
- **Deal size:** $100.1B  ·  $95.00/sh
- **Premium (vs unaffected):** 27%
- **Stage:** Marketed products + Phase 3 pipeline
- **Value-inflecting events:** Adjuvant Colon Cancer (C-08) trial data; Release of 2008 Financial Plan; Rejection of $89.00 proposal; Positive clinical data release
- **Offer range (low→high):** $86.50 → $95.00
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 7.7 months
- **Reported early (1mo+):** yes — The Wall Street Journal + 8 months early (June 2008)
- **Trailing return to unaffected:** 3mo -6% · 6mo +10% · 12mo -0% · 2yr -7%

### SCIELE PHARMA, INC. (SCRX)
- **Acquirer:** Shionogi & Co., Ltd.
- **Announced / Closed:** 2008-09-01 / 2008-10-09
- **Deal size:** $1.0B  ·  $31.00/sh
- **Premium (vs unaffected):** 63%
- **Stage:** Marketed lead asset (Sular)
- **Value-inflecting events:** Shionogi acquisition announcement
- **Offer range (low→high):** $28.50 → $31.00
- **Interested parties:** 6
- **Interest direction:** inbound
- **Engagement → deal:** 4.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -11% · 6mo -22% · 12mo -19% · 2yr +7%

### GENELABS TECHNOLOGIES, INC. (GNLB)
- **Acquirer:** GlaxoSmithKline plc
- **Announced / Closed:** 2008-10-29 / 2009-01-07
- **Deal size:** $57M  ·  $1.30/sh
- **Premium (vs unaffected):** 177%
- **Stage:** Late-stage (Prestara) + Discovery/Preclinical (HCV)
- **Value-inflecting events:** —
- **Offer range (low→high):** $1.03 → $1.30
- **Interested parties:** 23
- **Interest direction:** both
- **Engagement → deal:** 1.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -31% · 6mo -45% · 12mo -75% · 2yr -70%

### ALPHARMA INC (ALO)
- **Acquirer:** King Pharmaceuticals, Inc.
- **Announced / Closed:** 2008-11-24 / 2008-12-29
- **Deal size:** $1.5B  ·  $37.00/sh
- **Premium (vs unaffected):** 26%
- **Stage:** NDA / Priority Review lead + 1 marketed drug
- **Value-inflecting events:** EMBEDA NDA / Priority Review; ELADUR Phase 2 licensing deal; Kadian divestiture to Actavis
- **Offer range (low→high):** $33.00 → $37.00
- **Interested parties:** 3
- **Interest direction:** inbound
- **Engagement → deal:** 4.5 months
- **Reported early (1mo+):** yes — Forbes + 3 months early
- **Trailing return to unaffected:** 3mo +18% · 6mo +15% · 12mo +42% · 2yr +33%

### Omrix Biopharmaceuticals, Inc. (OMRI)
- **Acquirer:** Johnson & Johnson
- **Announced / Closed:** 2008-11-24 / —
- **Deal size:** $428M  ·  $25.00/sh
- **Premium (vs unaffected):** 69%
- **Stage:** Phase 3 lead + 2 marketed products
- **Value-inflecting events:** —
- **Offer range (low→high):** $21.00 → $25.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 3.8 months
- **Reported early (1mo+):** yes — Globes + 3 months early
- **Trailing return to unaffected:** 3mo -22% · 6mo -5% · 12mo -56% · 2yr -48%

### MEMORY PHARMACEUTICALS CORP (MEMY)
- **Acquirer:** Hoffmann-La Roche Inc.
- **Announced / Closed:** 2008-11-25 / 2009-01-05
- **Deal size:** $50M  ·  $0.61/sh
- **Premium (vs unaffected):** 319%
- **Stage:** Phase 2 lead + Phase 1 and 2 assets
- **Value-inflecting events:** —
- **Offer range (low→high):** $0.55 → $0.61
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 1.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -77% · 6mo -81% · 12mo -93% · 2yr -97%

### Indevus Pharmaceuticals, Inc. (ENDP)
- **Acquirer:** Endo Pharmaceuticals Holdings Inc.
- **Announced / Closed:** 2009-01-05 / 2009-03-23
- **Deal size:** $352M  ·  $4.50/sh  + CVR
- **Premium (vs unaffected):** 87%
- **Stage:** 1 approved drug + Phase 3/NDA lead assets
- **Value-inflecting events:** FDA Complete Response Letter for NEBIDO (June 2008)
- **Offer range (low→high):** $6.50 → $7.50
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 3.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +28% · 6mo +75% · 12mo -68% · 2yr -65%

### Targanta Therapeutics Corporation (TARG)
- **Acquirer:** The Medicines Company
- **Announced / Closed:** 2009-01-12 / 2009-02-25
- **Deal size:** $42M  ·  $2.00/sh  + CVR
- **Premium (vs unaffected):** 92%
- **Stage:** Phase 3 (Complete Response Letter received)
- **Value-inflecting events:** FDA advisory committee negative vote; FDA Complete Response Letter for oritavancin; Stock price drop of 82% following FDA panel
- **Offer range (low→high):** $1.80 → $6.55
- **Interested parties:** 26
- **Interest direction:** outbound
- **Engagement → deal:** 4.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -85% · 6mo -86% · 12mo -89% · 2yr —

### IDM PHARMA, INC. (IDMI)
- **Acquirer:** Takeda Pharmaceutical Company Limited
- **Announced / Closed:** 2009-05-18 / 2009-06-24
- **Deal size:** $67M  ·  $2.64/sh
- **Premium (vs unaffected):** 43%
- **Stage:** Approved (Europe) / Phase 3 (US)
- **Value-inflecting events:** FDA ODAC negative vote on MEPACT; CHMP positive opinion for MEPACT in Europe
- **Offer range (low→high):** $1.94 → $2.64
- **Interested parties:** 50
- **Interest direction:** outbound
- **Engagement → deal:** 29.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +1% · 6mo +11% · 12mo -19% · 2yr -42%

### Cougar Biotechnology, Inc. (CGRB)
- **Acquirer:** Johnson & Johnson
- **Announced / Closed:** 2009-05-21 / 2009-07-03
- **Deal size:** $894M  ·  $43.00/sh
- **Premium (vs unaffected):** 27%
- **Stage:** Phase 3 lead, pre-revenue
- **Value-inflecting events:** FDA Special Protocol Assessment (SPA) for abiraterone acetate; Phase 3 clinical trial initiation for prostate cancer
- **Offer range (low→high):** $28.00 → $43.00
- **Interested parties:** 20
- **Interest direction:** outbound
- **Engagement → deal:** 6.2 months
- **Reported early (1mo+):** yes — Rodman & Renshaw analyst note 1 month early
- **Trailing return to unaffected:** 3mo +15% · 6mo +26% · 12mo +72% · 2yr +37%

### Monogram Biosciences, Inc. (MGRM)
- **Acquirer:** Laboratory Corporation of America Holdings
- **Announced / Closed:** 2009-06-23 / 2009-08-04
- **Deal size:** $105M  ·  $4.55/sh
- **Premium (vs unaffected):** 82%
- **Stage:** Commercial (HIV and Oncology diagnostics)
- **Value-inflecting events:** Scientific diligence on VeraTag oncology platform; Re-evaluation of 0% notes 'put right' cost; Maturing $55M convertible debt obligations
- **Offer range (low→high):** $3.00 → $4.55
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 7.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -12% · 6mo +11% · 12mo -62% · 2yr -75%

### NOVEN PHARMACEUTICALS INC (NOVN)
- **Acquirer:** Hisamitsu Pharmaceutical Co., Inc.
- **Announced / Closed:** 2009-07-14 / 2009-08-20
- **Deal size:** $414M  ·  $16.50/sh
- **Premium (vs unaffected):** 38%
- **Stage:** Marketed product + Phase 2 lead asset
- **Value-inflecting events:** Daytrana peel force issues; Generic challenges to Novogyne JV; Positive Phase 2 results for Mesafem
- **Offer range (low→high):** $14.00 → $16.50
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 3.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +24% · 6mo +4% · 12mo +5% · 2yr -40%

### Avigen, Inc. (AVGN)
- **Acquirer:** MediciNova, Inc.
- **Announced / Closed:** 2009-08-21 / 2009-12-15
- **Deal size:** $32M  ·  $1.19/sh  + CVR
- **Premium (vs unaffected):** -9%
- **Stage:** Phase 2 lead + 1 failed Phase 2 asset
- **Value-inflecting events:** AV650 trial failure (Oct 2008); AV513 asset sale to Baxter (Dec 2008); BVF hostile tender offer launch (Jan 2009); MediciNova definitive merger agreement (Aug 2009)
- **Offer range (low→high):** $1.00 → $1.24
- **Interested parties:** 3
- **Interest direction:** both
- **Engagement → deal:** 8.4 months
- **Reported early (1mo+):** yes — Greenbackd/PR Newswire + 8 months early
- **Trailing return to unaffected:** 3mo +8% · 6mo +41% · 12mo -59% · 2yr -77%

### Sepracor Inc. (SEPR)
- **Acquirer:** Dainippon Sumitomo Pharma Co., Ltd.
- **Announced / Closed:** 2009-09-03 / 2009-10-20
- **Deal size:** $2.6B  ·  $23.00/sh
- **Premium (vs unaffected):** 31%
- **Stage:** Marketed products + Phase 3 lead
- **Value-inflecting events:** Lunesta pediatric exclusivity extension; SEP-225289 Phase 2 trial failure; Strong Q2 results and synergy value; Stedesa Phase 3 / NDA status
- **Offer range (low→high):** $15.00 → $23.00
- **Interested parties:** 7
- **Interest direction:** both
- **Engagement → deal:** 3.3 months
- **Reported early (1mo+):** yes — BioCentury/Analysts + 2-5 years early
- **Trailing return to unaffected:** 3mo +32% · 6mo +15% · 12mo -0% · 2yr -37%

### CHATTEM INC (CHTT)
- **Acquirer:** sanofi-aventis
- **Announced / Closed:** 2009-12-21 / 2010-03-10
- **Deal size:** $1.8B  ·  $93.50/sh
- **Premium (vs unaffected):** 41%
- **Stage:** Marketed OTC portfolio + Rx-to-OTC switch platform
- **Value-inflecting events:** Sanofi-aventis acquisition announcement
- **Offer range (low→high):** $85.00 → $93.50
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 3.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +8% · 6mo +18% · 12mo -4% · 2yr -12%

### OSI PHARMACEUTICALS INC (OSIP)
- **Acquirer:** Astellas US Holding, Inc.
- **Announced / Closed:** 2010-03-01 / 2010-06-08
- **Deal size:** $3.4B  ·  $57.50/sh
- **Premium (vs unaffected):** 68%
- **Stage:** Marketed lead + Phase 3 pipeline
- **Value-inflecting events:** Astellas public hostile tender offer; FDA approval of Tarceva for first-line maintenance; OSI Board rejection of $52.00 offer
- **Offer range (low→high):** $52.00 → $57.50
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 13.5 months
- **Reported early (1mo+):** yes — Astellas/Reuters + 14 months early
- **Trailing return to unaffected:** 3mo +6% · 6mo +1% · 12mo -4% · 2yr -7%

### PENWEST PHARMACEUTICALS CO (PPCO)
- **Acquirer:** Endo Pharmaceuticals Holdings Inc.
- **Announced / Closed:** 2010-08-09 / 2010-11-04
- **Deal size:** $160M  ·  $5.00/sh
- **Premium (vs unaffected):** 53%
- **Stage:** Marketed product + Phase 2 lead asset
- **Value-inflecting events:** Endo NDA for non-Penwest TRF Product; Tang Capital proxy contest victory; Board mandate to wind down and return capital
- **Offer range (low→high):** $4.00 → $5.00
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 0.6 months
- **Reported early (1mo+):** yes — Reuters/Bloomberg + 2 months early
- **Trailing return to unaffected:** 3mo -9% · 6mo +29% · 12mo +26% · 2yr -19%

### ZYMOGENETICS, INC. (ZGEN)
- **Acquirer:** Bristol-Myers Squibb Company
- **Announced / Closed:** 2010-09-07 / 2010-10-12
- **Deal size:** $844M  ·  $9.75/sh
- **Premium (vs unaffected):** 139%
- **Stage:** Phase 2 lead + 1 marketed product
- **Value-inflecting events:** Global collaboration with BMS for PEG-IFN-lambda; Phase 2 development of PEG-IFN-lambda; Commercialization of RECOTHROM; Phase 2 development of IL-21
- **Offer range (low→high):** $8.00 → $9.75
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 25.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -16% · 6mo -21% · 12mo -21% · 2yr -44%

### GENZYME CORP (GENZ)
- **Acquirer:** sanofi-aventis
- **Announced / Closed:** 2010-10-04 / 2011-04-08
- **Deal size:** $19.2B  ·  $74.00/sh
- **Premium (vs unaffected):** 5%
- **Stage:** Phase 3 lead + 2 approved drugs
- **Value-inflecting events:** Manufacturing supply issues (Cerezyme/Fabrazyme); Alemtuzumab Phase 3 clinical progress; Sanofi unsolicited $69.00 tender offer
- **Offer range (low→high):** $69.00 → $74.00
- **Interested parties:** 3
- **Interest direction:** inbound
- **Engagement → deal:** 2.2 months
- **Reported early (1mo+):** yes — Bloomberg/WSJ + 7 months early
- **Trailing return to unaffected:** 3mo +48% · 6mo +23% · 12mo +23% · 2yr +9%

### KING PHARMACEUTICALS INC (KG)
- **Acquirer:** Pfizer Inc.
- **Announced / Closed:** 2010-10-11 / 2011-02-28
- **Deal size:** $3.6B  ·  $14.25/sh
- **Premium (vs unaffected):** 52%
- **Stage:** Commercial with marketed products (Altace) + pipeline
- **Value-inflecting events:** —
- **Offer range (low→high):** $11.00 → $14.25
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 4.3 months
- **Reported early (1mo+):** yes — Wall Street Journal/Barron's 4 months early
- **Trailing return to unaffected:** 3mo +17% · 6mo -24% · 12mo -12% · 2yr +14%

### EURAND N.V. (EURX)
- **Acquirer:** Axcan Holdings Inc.
- **Announced / Closed:** 2010-12-01 / 2011-01-20
- **Deal size:** $576M  ·  $12.00/sh
- **Premium (vs unaffected):** 9%
- **Stage:** Marketed lead asset + Phase 3/Pending FDA
- **Value-inflecting events:** ZENPEP market share projections; Ultrase/Ultresa FDA approval delays
- **Offer range (low→high):** $11.00 → $12.00
- **Interested parties:** 26
- **Interest direction:** both
- **Engagement → deal:** 4.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +38% · 6mo +6% · 12mo -17% · 2yr +48%

### CYPRESS BIOSCIENCE INC (CYPB)
- **Acquirer:** Ramius Value and Opportunity Advisors LLC
- **Announced / Closed:** 2010-12-14 / 2010-12-14
- **Deal size:** $251M  ·  $6.50/sh
- **Premium (vs unaffected):** 63%
- **Stage:** Phase 2b lead + 1 marketed drug (royalty interest)
- **Value-inflecting events:** License agreement with BioLineRx for CYP-1020; Ramius unsolicited $4.00 per share proposal; Ramius hostile tender offer at $4.25; Cypress Board strategic alternatives evaluation
- **Offer range (low→high):** $4.00 → $6.50
- **Interested parties:** 3
- **Interest direction:** inbound
- **Engagement → deal:** 6.6 months
- **Reported early (1mo+):** yes — Business Wire reported Ramius's $4.00 offer 5 months early
- **Trailing return to unaffected:** 3mo +4% · 6mo -6% · 12mo -33% · 2yr -33%

### MATRIXX INITIATIVES, INC. (MTXX)
- **Acquirer:** H.I.G. Capital, LLC
- **Announced / Closed:** 2010-12-14 / 2011-02-18
- **Deal size:** $82M  ·  $8.75/sh
- **Premium (vs unaffected):** 65%
- **Stage:** Marketed OTC products + product recall status
- **Value-inflecting events:** FDA warning letter and product recall; Settlement of $15.5M personal injury litigation
- **Offer range (low→high):** $6.50 → $8.75
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 10.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +15% · 6mo +13% · 12mo +40% · 2yr -66%

### MARTEK BIOSCIENCES CORPORATION (MATK)
- **Acquirer:** Koninklijke DSM N.V.
- **Announced / Closed:** 2010-12-21 / 2011-02-25
- **Deal size:** $1.1B  ·  $31.50/sh
- **Premium (vs unaffected):** 43%
- **Stage:** Marketed products (ARA + Amerifit)
- **Value-inflecting events:** —
- **Offer range (low→high):** $27.00 → $31.50
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 12.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +7% · 6mo +16% · 12mo +22% · 2yr -23%

### CLINICAL DATA INC (CLDA)
- **Acquirer:** Forest Laboratories, Inc.
- **Announced / Closed:** 2011-02-22 / 2011-04-12
- **Deal size:** $933M  ·  $30.00/sh  + CVR
- **Premium (vs unaffected):** 100%
- **Stage:** Approved lead asset + Phase 3 pipeline
- **Value-inflecting events:** FDA approval of Viibryd; Hiring J.P. Morgan for strategic alternatives; Company A offer of $24.00/share
- **Offer range (low→high):** $24.00 → $30.00
- **Interested parties:** 24
- **Interest direction:** outbound
- **Engagement → deal:** 22.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -20% · 6mo +9% · 12mo -6% · 2yr +80%

### Inspire Pharmaceuticals, Inc. (ISPH)
- **Acquirer:** Merck & Co., Inc.
- **Announced / Closed:** 2011-04-05 / 2011-05-16
- **Deal size:** $416M  ·  $5.00/sh
- **Premium (vs unaffected):** 25%
- **Stage:** Phase 3 (failed) lead + 2 marketed drugs
- **Value-inflecting events:** Denufosol Phase 3 trial failure; Merck acquisition announcement
- **Offer range (low→high):** $4.40 → $5.00
- **Interested parties:** 4
- **Interest direction:** outbound
- **Engagement → deal:** 1.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -43% · 6mo -19% · 12mo -36% · 2yr -11%

### ICAGEN INC (ICGN)
- **Acquirer:** Pfizer Inc.
- **Announced / Closed:** 2011-07-20 / 2011-10-27
- **Deal size:** $53M  ·  $6.00/sh
- **Premium (vs unaffected):** 180%
- **Stage:** Phase 2 lead + Pre-clinical
- **Value-inflecting events:** Pfizer 13D filing disclosing strategic evaluation; Nav 1.7 Program partnership with Pfizer; ICA-105665 Phase 2 development
- **Offer range (low→high):** $4.00 → $6.00
- **Interested parties:** 43
- **Interest direction:** both
- **Engagement → deal:** 3.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -20% · 6mo +48% · 12mo -36% · 2yr -33%

### Anadys Pharmaceuticals, Inc. (ANDS)
- **Acquirer:** Roche Holding Ltd
- **Announced / Closed:** 2011-10-17 / 2011-11-23
- **Deal size:** $212M  ·  $3.70/sh
- **Premium (vs unaffected):** 289%
- **Stage:** Phase 2 lead + clinical secondary asset
- **Value-inflecting events:** Phase IIa clinical data for setrobuvir; Pricing of $25M public offering; Clinical collaboration agreement with Party A; Unblinded 12-week Phase IIb data for setrobuvir
- **Offer range (low→high):** $3.00 → $3.70
- **Interested parties:** 15
- **Interest direction:** outbound
- **Engagement → deal:** 13.8 months
- **Reported early (1mo+):** yes — FierceBiotech/Reuters + 17 months early (Strategic Review announcement)
- **Trailing return to unaffected:** 3mo +2% · 6mo -16% · 12mo -47% · 2yr -57%

### ADOLOR CORPORATION (ADLR)
- **Acquirer:** Cubist Pharmaceuticals, Inc.
- **Announced / Closed:** 2011-10-24 / 2011-12-12
- **Deal size:** $198M  ·  $4.25/sh  + CVR
- **Premium (vs unaffected):** 146%
- **Stage:** Phase 2 lead + 1 approved drug
- **Value-inflecting events:** Positive Phase 2 results for ADL5945
- **Offer range (low→high):** $4.00 → $4.25
- **Interested parties:** 11
- **Interest direction:** both
- **Engagement → deal:** 6.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -3% · 6mo +20% · 12mo +57% · 2yr +19%

### Pharmasset Inc (VRUS)
- **Acquirer:** Gilead Sciences, Inc.
- **Announced / Closed:** 2011-11-21 / 2012-01-17
- **Deal size:** $10.4B  ·  $137.00/sh
- **Premium (vs unaffected):** —
- **Stage:** Phase 3 lead + Phase 2b assets
- **Value-inflecting events:** AASLD conference data for PSI-7977; Commencement of late-stage clinical trials for PSI-7977
- **Offer range (low→high):** $100.00 → $137.00
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 5.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo — · 6mo — · 12mo — · 2yr —

### MICROMET, INC. (MITI)
- **Acquirer:** Amgen Inc.
- **Announced / Closed:** 2012-01-26 / 2012-03-07
- **Deal size:** $1.0B  ·  $11.00/sh
- **Premium (vs unaffected):** —
- **Stage:** Phase 2 lead + BiTE platform
- **Value-inflecting events:** Solid tumor BiTE collaboration with Amgen; Initiation of formal partnering process for blinatumomab; Amgen acquisition proposal
- **Offer range (low→high):** $9.00 → $11.00
- **Interested parties:** 28
- **Interest direction:** both
- **Engagement → deal:** 12.5 months
- **Reported early (1mo+):** yes — Industry Analysis + 6 months early
- **Trailing return to unaffected:** 3mo — · 6mo — · 12mo — · 2yr —

### AMYLIN PHARMACEUTICALS INC (AMLN)
- **Acquirer:** Bristol-Myers Squibb Company
- **Announced / Closed:** 2012-06-29 / 2012-08-08
- **Deal size:** $5.1B  ·  $31.00/sh
- **Premium (vs unaffected):** 16%
- **Stage:** Commercial, 2 approved drugs + Phase 2/3 pipeline
- **Value-inflecting events:** Termination of Eli Lilly collaboration; FDA approval of BYDUREON; Bloomberg report of rejected $22.00 BMS bid; Initiation of formal auction process
- **Offer range (low→high):** $22.00 → $31.00
- **Interested parties:** 12
- **Interest direction:** both
- **Engagement → deal:** 4.4 months
- **Reported early (1mo+):** yes — Bloomberg + 3 months early
- **Trailing return to unaffected:** 3mo +56% · 6mo +169% · 12mo +99% · 2yr +44%

### DUSA PHARMACEUTICALS, INC. (DUSA)
- **Acquirer:** Sun Pharmaceutical Industries Limited
- **Announced / Closed:** 2012-11-08 / 2012-12-20
- **Deal size:** $200M  ·  $8.00/sh
- **Premium (vs unaffected):** 17%
- **Stage:** Marketed products (Levulan Kerastick, BLU-U) + Phase 2 label expansion
- **Value-inflecting events:** —
- **Offer range (low→high):** $6.98 → $8.00
- **Interested parties:** 30
- **Interest direction:** outbound
- **Engagement → deal:** 6.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +28% · 6mo +15% · 12mo +84% · 2yr +159%

### MAP Pharmaceuticals, Inc. (MAPP)
- **Acquirer:** Allergan, Inc.
- **Announced / Closed:** 2013-01-22 / 2013-03-01
- **Deal size:** $889M  ·  $25.00/sh
- **Premium (vs unaffected):** —
- **Stage:** NDA Resubmission (PDUFA April 2013)
- **Value-inflecting events:** FDA accepts NDA resubmission for LEVADEX; Collaboration and Co-Promotion Agreements with Allergan
- **Offer range (low→high):** $19.00 → $25.00
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 2.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo — · 6mo — · 12mo — · 2yr —

### Obagi Medical Products, Inc. (OMPI)
- **Acquirer:** Valeant Pharmaceuticals International, Inc.
- **Announced / Closed:** 2013-03-20 / 2013-04-25
- **Deal size:** $418M  ·  $24.00/sh
- **Premium (vs unaffected):** 68%
- **Stage:** Commercial, marketed core product line
- **Value-inflecting events:** Unsolicited bid from Bidder C; Allergan acquisition of SkinMedica; Retention of professional advisors for strategic review; Amendment of merger agreement to $24.00
- **Offer range (low→high):** $16.50 → $24.00
- **Interested parties:** 12
- **Interest direction:** both
- **Engagement → deal:** 1.2 months
- **Reported early (1mo+):** yes — L.A. Business Journal reported Allergan/Medicis interest 3+ months early
- **Trailing return to unaffected:** 3mo +11% · 6mo +7% · 12mo +19% · 2yr +14%

### ELAN CORPORATION, PLC (ELN)
- **Acquirer:** Royalty Pharma
- **Announced / Closed:** 2013-05-15 / —
- **Deal size:** —
- **Premium (vs unaffected):** —
- **Stage:** Commercial (Tysabri royalty interest)
- **Value-inflecting events:** Sale of Tysabri interest to Biogen Idec; Royalty Pharma unsolicited approach; Launch of formal sale process
- **Offer range (low→high):** $11.00 → $15.50
- **Interested parties:** 7
- **Interest direction:** both
- **Engagement → deal:** 2.7 months
- **Reported early (1mo+):** yes — Bloomberg/Reuters reported bids/rumors starting Jan 2009 and Feb 2013
- **Trailing return to unaffected:** 3mo +16% · 6mo +10% · 12mo -10% · 2yr +42%

### Trius Therapeutics Inc (TSRX)
- **Acquirer:** Cubist Pharmaceuticals, Inc.
- **Announced / Closed:** 2013-07-30 / 2013-09-11
- **Deal size:** $652M  ·  $13.50/sh  + CVR
- **Premium (vs unaffected):** 67%
- **Stage:** Phase 3 / NDA preparation
- **Value-inflecting events:** —
- **Offer range (low→high):** $12.25 → $13.50
- **Interested parties:** 13
- **Interest direction:** inbound
- **Engagement → deal:** 12.2 months
- **Reported early (1mo+):** yes — Zacks Investment Research + 16 months early
- **Trailing return to unaffected:** 3mo +18% · 6mo +69% · 12mo +41% · 2yr +9%

### Onyx Pharmaceuticals, Inc. (ONXX)
- **Acquirer:** Amgen Inc.
- **Announced / Closed:** 2013-08-25 / 2013-10-01
- **Deal size:** $9.2B  ·  $125.00/sh
- **Premium (vs unaffected):** -5%
- **Stage:** 3 approved drugs + Phase 3 lead asset
- **Value-inflecting events:** Amgen unsolicited $120 proposal; DMC FOCUS study continuation recommendation; Amgen demand for unblinded FOCUS data
- **Offer range (low→high):** $120.00 → $125.00
- **Interested parties:** 13
- **Interest direction:** inbound
- **Engagement → deal:** 2.6 months
- **Reported early (1mo+):** yes — Reuters/BioSpace + 16 months early
- **Trailing return to unaffected:** 3mo +39% · 6mo +68% · 12mo +69% · 2yr +312%

### SANTARUS INC (SNTS)
- **Acquirer:** Salix Pharmaceuticals, Ltd.
- **Announced / Closed:** 2013-11-07 / 2014-01-02
- **Deal size:** $2.2B  ·  $32.00/sh
- **Premium (vs unaffected):** 43%
- **Stage:** Marketed (Uceris) + Phase 3 (Ruconest)
- **Value-inflecting events:** Commercial success of Uceris; Ruconest regulatory pathway concerns; License Amendment with Cosmo Technologies
- **Offer range (low→high):** $4.50 → $32.00
- **Interested parties:** 16
- **Interest direction:** both
- **Engagement → deal:** 41.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +2% · 6mo +33% · 12mo +135% · 2yr +688%

### Cadence Pharmaceuticals Inc (CADX)
- **Acquirer:** Mallinckrodt plc
- **Announced / Closed:** 2014-02-10 / 2014-03-19
- **Deal size:** $1.2B  ·  $14.00/sh
- **Premium (vs unaffected):** 36%
- **Stage:** 1 approved drug
- **Value-inflecting events:** Favorable patent infringement ruling vs Exela; Board approval of strategic transaction path; Execution of Merger Agreement with Mallinckrodt
- **Offer range (low→high):** $11.25 → $14.00
- **Interested parties:** 8
- **Interest direction:** both
- **Engagement → deal:** 3.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +74% · 6mo +37% · 12mo +91% · 2yr +155%

### Chelsea Therapeutics International, Ltd. (CHTP)
- **Acquirer:** H. Lundbeck A/S
- **Announced / Closed:** 2014-05-08 / 2014-06-23
- **Deal size:** $508M  ·  $6.44/sh  + CVR
- **Premium (vs unaffected):** 21%
- **Stage:** 1 approved drug (accelerated approval)
- **Value-inflecting events:** FDA Complete Response Letter for Northera; FDA Advisory Committee 16-to-1 vote for approval; FDA accelerated approval for Northera
- **Offer range (low→high):** $6.44 → $6.44
- **Interested parties:** 13
- **Interest direction:** outbound
- **Engagement → deal:** 12.9 months
- **Reported early (1mo+):** yes — Fierce Pharma + 1.5 months early
- **Trailing return to unaffected:** 3mo +52% · 6mo +82% · 12mo +177% · 2yr +142%

### Idenix Pharmaceuticals, Inc. (IDIX)
- **Acquirer:** Merck & Co., Inc.
- **Announced / Closed:** 2014-06-09 / 2014-08-05
- **Deal size:** $3.7B  ·  $24.50/sh
- **Premium (vs unaffected):** 379%
- **Stage:** Phase 1/2 lead asset
- **Value-inflecting events:** FDA clinical hold on IDX184 (Aug 2012); Positive Phase I/II data for IDX21437 (April 2014)
- **Offer range (low→high):** $7.18 → $24.50
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 6.2 months
- **Reported early (1mo+):** yes — FierceBiotech + 2 years early
- **Trailing return to unaffected:** 3mo -25% · 6mo +18% · 12mo +41% · 2yr -46%

### Cadista Holdings Inc. (CADI)
- **Acquirer:** Jubilant Life Sciences Ltd.
- **Announced / Closed:** 2014-08-01 / —
- **Deal size:** $188M  ·  $1.60/sh
- **Premium (vs unaffected):** —
- **Stage:** Commercial + Marketed generic products
- **Value-inflecting events:** Loss of major retail customer for Methylprednisolone; Increased competition and pricing pressure for Meclizine; Requirement for $17 million in capital expenditures
- **Offer range (low→high):** $1.20 → $1.60
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 10.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo — · 6mo — · 12mo — · 2yr —

### INTERMUNE, INC. (ITMN)
- **Acquirer:** Roche Holding Ltd
- **Announced / Closed:** 2014-08-24 / 2014-09-29
- **Deal size:** $8.0B  ·  $74.00/sh
- **Premium (vs unaffected):** 63%
- **Stage:** Phase 3 / NDA Resubmission
- **Value-inflecting events:** Positive top-line data from Phase 3 ASCEND study; Breakthrough Therapy designation from FDA; Public rumors of potential transaction
- **Offer range (low→high):** $57.00 → $74.00
- **Interested parties:** 5
- **Interest direction:** inbound
- **Engagement → deal:** 1.0 months
- **Reported early (1mo+):** yes — Reuters reported M&A interest 5 months early
- **Trailing return to unaffected:** 3mo +53% · 6mo +170% · 12mo +207% · 2yr +472%

### AMBIT BIOSCIENCES CORP (AMBI)
- **Acquirer:** Daiichi Sankyo Company, Limited
- **Announced / Closed:** 2014-09-28 / 2014-11-10
- **Deal size:** $270M  ·  $15.00/sh  + CVR
- **Premium (vs unaffected):** 98%
- **Stage:** Phase 3 lead asset
- **Value-inflecting events:** —
- **Offer range (low→high):** $12.00 → $15.00
- **Interested parties:** 2
- **Interest direction:** both
- **Engagement → deal:** 9.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +10% · 6mo -31% · 12mo -44% · 2yr —

### Durata Therapeutics, Inc. (DRTX)
- **Acquirer:** Actavis plc
- **Announced / Closed:** 2014-10-06 / 2014-11-17
- **Deal size:** $616M  ·  $23.00/sh  + CVR
- **Premium (vs unaffected):** 54%
- **Stage:** Approved lead asset + Phase 3 expansion
- **Value-inflecting events:** Positive Phase 3 data for dalbavancin; FDA approval of Dalvance (dalbavancin); EMA approval and single-dose labeling milestones
- **Offer range (low→high):** $18.00 → $23.00
- **Interested parties:** 7
- **Interest direction:** both
- **Engagement → deal:** 0.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -7% · 6mo +6% · 12mo +68% · 2yr +58%

### ALLERGAN INC (AGN)
- **Acquirer:** Actavis plc
- **Announced / Closed:** 2014-11-16 / 2015-03-17
- **Deal size:** $38.4B  ·  $129.22/sh  + CVR
- **Premium (vs unaffected):** -27%
- **Stage:** Phase 3 lead + 1 approved drug
- **Value-inflecting events:** DARPin (abicipar pegol) Phase 3; OZURDEX approval for DME; Valeant/Pershing Square hostile bid; Actavis white knight approach
- **Offer range (low→high):** $153.00 → $219.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 6.9 months
- **Reported early (1mo+):** yes — WSJ + 18 months early (Oct 2012)
- **Trailing return to unaffected:** 3mo +6% · 6mo +33% · 12mo +96% · 2yr +100%

### AVANIR PHARMACEUTICALS, INC. (AVNR)
- **Acquirer:** Otsuka Pharmaceutical Co., Ltd.
- **Announced / Closed:** 2014-12-02 / 2015-01-13
- **Deal size:** $3.3B  ·  $17.00/sh
- **Premium (vs unaffected):** 31%
- **Stage:** 1 marketed drug + Phase 2/3 pipeline
- **Value-inflecting events:** Positive Phase II results for AVP-923 in Alzheimer's agitation; FDA Complete Response Letter for AVP-825; 85% stock surge following Alzheimer's data
- **Offer range (low→high):** $15.00 → $17.00
- **Interested parties:** 5
- **Interest direction:** inbound
- **Engagement → deal:** 18.7 months
- **Reported early (1mo+):** yes — Bloomberg/JMP Group + 2 months early
- **Trailing return to unaffected:** 3mo +146% · 6mo +179% · 12mo +202% · 2yr +404%

### Cubist Pharmaceuticals Inc. (CBST)
- **Acquirer:** Merck & Co., Inc.
- **Announced / Closed:** 2014-12-08 / 2015-01-21
- **Deal size:** $7.8B  ·  $102.00/sh
- **Premium (vs unaffected):** 25%
- **Stage:** Phase 3 lead + 4 approved drugs
- **Value-inflecting events:** Merger announcement with Merck
- **Offer range (low→high):** $85.00 → $102.00
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 7.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +2% · 6mo +6% · 12mo +35% · 2yr +92%

### NPS Pharmaceuticals, Inc. (NPSP)
- **Acquirer:** Shire plc
- **Announced / Closed:** 2015-01-11 / 2015-02-21
- **Deal size:** $5.0B  ·  $46.00/sh
- **Premium (vs unaffected):** 47%
- **Stage:** 1 commercial drug + 1 pending FDA approval
- **Value-inflecting events:** Natpara PDUFA date (Jan 24, 2015); Gattex commercialization
- **Offer range (low→high):** $41.00 → $46.00
- **Interested parties:** 12
- **Interest direction:** both
- **Engagement → deal:** 1.9 months
- **Reported early (1mo+):** yes — Financial Times reported Shire interest 7 months early
- **Trailing return to unaffected:** 3mo -4% · 6mo -10% · 12mo +27% · 2yr +250%

### SALIX PHARMACEUTICALS LTD (SLXP)
- **Acquirer:** Valeant Pharmaceuticals International, Inc.
- **Announced / Closed:** 2015-02-22 / 2015-04-01
- **Deal size:** $11.1B  ·  $173.00/sh
- **Premium (vs unaffected):** 37%
- **Stage:** Marketed products + Phase 3 lead
- **Value-inflecting events:** Santarus acquisition; Wholesaler inventory disclosure/CFO resignation; Xifaxan 550 Phase 3/FDA PDUFA; Cosmo Pharmaceuticals merger termination
- **Offer range (low→high):** $150.00 → $173.00
- **Interested parties:** 9
- **Interest direction:** both
- **Engagement → deal:** 1.1 months
- **Reported early (1mo+):** yes — The Wall Street Journal + 6 months early
- **Trailing return to unaffected:** 3mo -10% · 6mo -5% · 12mo +28% · 2yr +155%

### Auspex Pharmaceuticals, Inc. (ASPX)
- **Acquirer:** Teva Pharmaceutical Industries Ltd.
- **Announced / Closed:** 2015-03-30 / 2015-05-05
- **Deal size:** $3.2B  ·  $101.00/sh
- **Premium (vs unaffected):** 50%
- **Stage:** Phase 3 lead, pre-revenue
- **Value-inflecting events:** Positive Phase 3 results for SD-809 in Huntington's disease chorea
- **Offer range (low→high):** $85.00 → $101.00
- **Interested parties:** 6
- **Interest direction:** both
- **Engagement → deal:** 21.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +178% · 6mo +192% · 12mo +172% · 2yr —

### CELLULAR DYNAMICS INTERNATIONAL, INC. (ICEL)
- **Acquirer:** FUJIFILM Holdings Corporation
- **Announced / Closed:** 2015-03-30 / 2015-05-01
- **Deal size:** $261M  ·  $16.50/sh
- **Premium (vs unaffected):** 204%
- **Stage:** Commercial (iCell Hepatocytes) + Development (Pharma Cellular Therapeutic)
- **Value-inflecting events:** —
- **Offer range (low→high):** $13.00 → $16.50
- **Interested parties:** 9
- **Interest direction:** outbound
- **Engagement → deal:** 9.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -18% · 6mo -53% · 12mo -64% · 2yr -46%

### HYPERION THERAPEUTICS INC (HPTX)
- **Acquirer:** Horizon Pharma plc
- **Announced / Closed:** 2015-03-30 / 2015-05-07
- **Deal size:** $960M  ·  $46.00/sh
- **Premium (vs unaffected):** 56%
- **Stage:** 2 approved drugs + Phase 2/3 lead expansion
- **Value-inflecting events:** Settlement of Andromeda litigation; Strong fourth-quarter results; RAVICTI and BUPHENYL commercialization
- **Offer range (low→high):** $30.00 → $46.00
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 1.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +44% · 6mo +14% · 12mo -5% · 2yr +20%

### Perrigo Company plc (PRGO)
- **Acquirer:** Mylan N.V.
- **Announced / Closed:** 2015-04-08 / —
- **Deal size:** $11.0B  ·  $75.00/sh  + CVR
- **Premium (vs unaffected):** -52%
- **Stage:** Marketed portfolio + Phase 3
- **Value-inflecting events:** Mylan unsolicited proposal disclosure
- **Offer range (low→high):** $205.00 → $205.00
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 10.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -0% · 6mo +7% · 12mo -5% · 2yr +31%

### Depomed, Inc. (ASRT)
- **Acquirer:** Horizon Pharma plc
- **Announced / Closed:** 2015-07-07 / —
- **Deal size:** $57M  ·  $0.95/sh  + CVR
- **Premium (vs unaffected):** -96%
- **Stage:** Commercial with multiple approved drugs (NUCYNTA, Gralise)
- **Value-inflecting events:** Acquisition of NUCYNTA franchise from Janssen; Horizon Pharma unsolicited $29.25 per share proposal; California court preliminary injunction against Horizon; Starboard Value LP activist stake disclosure
- **Offer range (low→high):** $29.25 → $33.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 1.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -7% · 6mo +36% · 12mo +75% · 2yr +257%

### Receptos, Inc. (RCPT (NASDAQ Global Market))
- **Acquirer:** Celgene Corporation
- **Announced / Closed:** 2015-07-14 / 2015-08-27
- **Deal size:** $7.3B  ·  $232.00/sh
- **Premium (vs unaffected):** 30%
- **Stage:** Phase 3 lead, pre-revenue
- **Value-inflecting events:** Phase 2 RADIANCE interim analysis (Dec 2013); Phase 2 RADIANCE primary endpoint met (June 2014); TOUCHSTONE Phase 2 primary endpoint met (Oct 2014); Media reports of sale process (April 2015)
- **Offer range (low→high):** $175.00 → $232.00
- **Interested parties:** 14
- **Interest direction:** both
- **Engagement → deal:** 22.5 months
- **Reported early (1mo+):** yes — Bloomberg reported sale process 3.5 months early
- **Trailing return to unaffected:** 3mo +19% · 6mo +48% · 12mo +345% · 2yr +868%

### INSITE VISION INCORPORATED (INSV)
- **Acquirer:** Sun Pharmaceutical Industries Ltd.
- **Announced / Closed:** 2015-09-15 / 2015-11-02
- **Deal size:** $46M  ·  $0.35/sh
- **Premium (vs unaffected):** 59%
- **Stage:** NDA Filed lead + 1 marketed drug
- **Value-inflecting events:** BromSite NDA filing; FDA acceptance of BromSite NDA; Strategic review initiation; Sun Pharma unsolicited proposal
- **Offer range (low→high):** $0.25 → $0.35
- **Interested parties:** 36
- **Interest direction:** both
- **Engagement → deal:** 19.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +57% · 6mo +22% · 12mo -12% · 2yr +10%

### ZS Pharma, Inc. (ZSPH)
- **Acquirer:** AstraZeneca PLC
- **Announced / Closed:** 2015-11-06 / 2015-12-17
- **Deal size:** $2.3B  ·  $90.00/sh
- **Premium (vs unaffected):** 35%
- **Stage:** NDA (Under FDA Review), lead asset ZS-9
- **Value-inflecting events:** NDA submission for ZS-9; Actelion takeover proposal leak; FDA approval of rival drug Veltassa; AstraZeneca acquisition announcement
- **Offer range (low→high):** $83.00 → $90.00
- **Interested parties:** 8
- **Interest direction:** inbound
- **Engagement → deal:** 1.8 months
- **Reported early (1mo+):** yes — Bloomberg reported Actelion offer 2 months early
- **Trailing return to unaffected:** 3mo +14% · 6mo +61% · 12mo +74% · 2yr —

### Ocata Therapeutics, Inc. (OCAT)
- **Acquirer:** Astellas Pharma Inc.
- **Announced / Closed:** 2015-11-10 / 2016-02-10
- **Deal size:** $360M  ·  $8.50/sh
- **Premium (vs unaffected):** 81%
- **Stage:** Phase 1/2 lead asset
- **Value-inflecting events:** —
- **Offer range (low→high):** $8.00 → $8.50
- **Interested parties:** 11
- **Interest direction:** both
- **Engagement → deal:** 15.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -10% · 6mo -29% · 12mo -32% · 2yr -22%

### Biotie Therapies Oyj (BITI)
- **Acquirer:** Acorda Therapeutics, Inc.
- **Announced / Closed:** 2016-01-19 / 2016-04-11
- **Deal size:** $289M  ·  $0.29/sh
- **Premium (vs unaffected):** -98%
- **Stage:** Phase 3 lead + 1 marketed drug
- **Value-inflecting events:** Tozadenant Phase 3 entry; Selincro marketing approval; Baupost Group 12.92% stake acquisition
- **Offer range (low→high):** $25.50 → $25.60
- **Interested parties:** 7
- **Interest direction:** both
- **Engagement → deal:** 3.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -17% · 6mo -42% · 12mo — · 2yr —

### ALERE INC. (ALR)
- **Acquirer:** Abbott Laboratories
- **Announced / Closed:** 2016-01-30 / 2017-10-03
- **Deal size:** $4.5B  ·  $51.00/sh
- **Premium (vs unaffected):** 30%
- **Stage:** Commercial diagnostic platforms
- **Value-inflecting events:** Unsolicited $46.00/share take-private proposal from former CEO; Abbott Laboratories acquisition announcement; FTC and EC regulatory divestiture requirements
- **Offer range (low→high):** $46.00 → $51.00
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** —
- **Reported early (1mo+):** yes — Reuters/Bloomberg reported unsolicited bid 16 months early
- **Trailing return to unaffected:** 3mo -23% · 6mo -28% · 12mo +4% · 2yr +3%

### Alexza Pharmaceuticals Inc. (ALXA)
- **Acquirer:** Grupo Ferrer Internacional, S.A.
- **Announced / Closed:** 2016-05-10 / 2016-06-21
- **Deal size:** $20M  ·  $0.90/sh  + CVR
- **Premium (vs unaffected):** 80%
- **Stage:** Approved/Commercial lead asset
- **Value-inflecting events:** Teva termination of U.S. marketing partnership; Default on Atlas Notes; Strategic alternatives exploration announcement; ADASUVE U.S. rights reacquisition
- **Offer range (low→high):** $0.60 → $0.90
- **Interested parties:** 83
- **Interest direction:** outbound
- **Engagement → deal:** 7.4 months
- **Reported early (1mo+):** yes — SEC Filing/Press Release +2 months early
- **Trailing return to unaffected:** 3mo -7% · 6mo -60% · 12mo -75% · 2yr -88%

### Anacor Pharmaceuticals, Inc. (ANAC)
- **Acquirer:** Pfizer Inc.
- **Announced / Closed:** 2016-05-16 / 2016-06-24
- **Deal size:** $4.5B  ·  $99.25/sh
- **Premium (vs unaffected):** 53%
- **Stage:** Phase 3 / NDA submitted lead + 1 marketed drug
- **Value-inflecting events:** Positive Phase 3 results for crisaborole; NDA submission for crisaborole; Pfizer acquisition announcement
- **Offer range (low→high):** $82.00 → $99.25
- **Interested parties:** 3
- **Interest direction:** both
- **Engagement → deal:** 1.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -31% · 6mo — · 12mo — · 2yr —

### XENOPORT, INC. (XNPT)
- **Acquirer:** Arbor Pharmaceuticals, Inc.
- **Announced / Closed:** 2016-05-23 / 2016-07-05
- **Deal size:** $449M  ·  $7.03/sh
- **Premium (vs unaffected):** 43%
- **Stage:** Commercial with 1 approved drug + Phase 3 ready asset
- **Value-inflecting events:** Phase 2 results for XP23829; Strategic shift to focus on HORIZANT; Licensing of XP23829 to Dr. Reddy’s; Arbor final offer of $7.03
- **Offer range (low→high):** $5.65 → $7.03
- **Interested parties:** 33
- **Interest direction:** outbound
- **Engagement → deal:** 1.8 months
- **Reported early (1mo+):** yes — FierceBiotech/FirstWord Pharma reported sale exploration 4 months early
- **Trailing return to unaffected:** 3mo -3% · 6mo -5% · 12mo -33% · 2yr +21%

### Celator Pharmaceuticals Inc (CPXX)
- **Acquirer:** Jazz Pharmaceuticals plc
- **Announced / Closed:** 2016-05-27 / 2016-07-12
- **Deal size:** $1.3B  ·  $30.25/sh
- **Premium (vs unaffected):** 104%
- **Stage:** Pre-commercial, Phase 3 lead
- **Value-inflecting events:** Positive Phase 3 trial results for VYXEOS (March 2016); Jazz submits initial $20.00 per share indication (April 2016); Receipt of four competing acquisition proposals (May 2016)
- **Offer range (low→high):** $3.00 → $30.25
- **Interested parties:** 41
- **Interest direction:** both
- **Engagement → deal:** 17.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +9% · 6mo +21% · 12mo +36% · 2yr +452%

### Sagent Pharmaceuticals, Inc. (SGNT)
- **Acquirer:** Nichi-Iko Pharmaceutical Co., Ltd. (Japanese corporation)
- **Announced / Closed:** 2016-07-11 / 2016-08-29
- **Deal size:** $716M  ·  $21.75/sh
- **Premium (vs unaffected):** 55%
- **Stage:** Commercial generic injectable portfolio + 20 pipeline ANDAs
- **Value-inflecting events:** CEO Jeffrey Yordon retirement announcement; Reuters report of potential sale and advisor hire; Acquisition of 5 ANDAs from Teva/Actavis; Launch of Chlorothiazide Sodium and Amikacin Sulfate
- **Offer range (low→high):** $20.32 → $21.75
- **Interested parties:** 7
- **Interest direction:** both
- **Engagement → deal:** 5.3 months
- **Reported early (1mo+):** yes — Reuters reported sale consideration 6 months early
- **Trailing return to unaffected:** 3mo +4% · 6mo -4% · 12mo -40% · 2yr -48%

### Relypsa, Inc. (RLYP)
- **Acquirer:** Galenica AG
- **Announced / Closed:** 2016-07-21 / 2016-09-01
- **Deal size:** $1.4B  ·  $32.00/sh
- **Premium (vs unaffected):** 79%
- **Stage:** Approved / Commercial
- **Value-inflecting events:** FDA approval of Veltassa; Reuters reports sale exploration; AstraZeneca FDA CRL for competitor ZS-9; Public announcement of Merger Agreement
- **Offer range (low→high):** $29.00 → $32.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 26.5 months
- **Reported early (1mo+):** yes — StreetInsider/Reuters + 3-7 months early
- **Trailing return to unaffected:** 3mo +33% · 6mo -36% · 12mo -47% · 2yr -24%

### MEDIVATION, INC. (MDVN)
- **Acquirer:** Pfizer Inc.
- **Announced / Closed:** 2016-08-22 / 2016-09-28
- **Deal size:** $13.5B  ·  $81.50/sh
- **Premium (vs unaffected):** 30%
- **Stage:** Marketed lead asset + Phase 3 pipeline
- **Value-inflecting events:** —
- **Offer range (low→high):** $52.50 → $81.50
- **Interested parties:** 15
- **Interest direction:** inbound
- **Engagement → deal:** 4.1 months
- **Reported early (1mo+):** yes — Bloomberg/Reuters + 4 months early
- **Trailing return to unaffected:** 3mo +19% · 6mo +66% · 12mo -39% · 2yr -31%

### Raptor Pharmaceutical Corp (RPTP)
- **Acquirer:** Horizon Pharma plc
- **Announced / Closed:** 2016-09-12 / 2016-10-25
- **Deal size:** $772M  ·  $9.00/sh  + CVR
- **Premium (vs unaffected):** 33%
- **Stage:** 1 approved drug + 1 drug approved in EU/Canada under FDA review
- **Value-inflecting events:** Phase 2b CyNCh study failure in pediatric NASH; NIDDK data presentation at AASLD; QUINSAIR launch in Europe; Horizon Pharma acquisition announcement
- **Offer range (low→high):** $9.00 → $9.00
- **Interested parties:** 3
- **Interest direction:** outbound
- **Engagement → deal:** —
- **Reported early (1mo+):** yes — Reuters reported sale exploration 5 months early
- **Trailing return to unaffected:** 3mo +60% · 6mo +70% · 12mo -49% · 2yr -39%

### Vitae Pharmaceuticals, Inc. (VTAE)
- **Acquirer:** Allergan plc
- **Announced / Closed:** 2016-09-14 / 2016-10-25
- **Deal size:** $606M  ·  $21.00/sh
- **Premium (vs unaffected):** 143%
- **Stage:** Phase 2 lead
- **Value-inflecting events:** VTP-43742 Phase 2a top-line results
- **Offer range (low→high):** $20.50 → $21.00
- **Interested parties:** 38
- **Interest direction:** both
- **Engagement → deal:** 8.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +35% · 6mo +1% · 12mo +4% · 2yr +9%

### Tobira Therapeutics, Inc. (TBRA)
- **Acquirer:** Allergan plc
- **Announced / Closed:** 2016-09-20 / 2016-11-01
- **Deal size:** $534M  ·  $28.35/sh  + CVR
- **Premium (vs unaffected):** 482%
- **Stage:** Phase 2b lead asset
- **Value-inflecting events:** Phase 2b CENTAUR trial results
- **Offer range (low→high):** $28.35 → $28.35
- **Interested parties:** 11
- **Interest direction:** inbound
- **Engagement → deal:** 3.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -41% · 6mo -30% · 12mo -63% · 2yr -53%

### ARIAD PHARMACEUTICALS INC (ARIA)
- **Acquirer:** Takeda Pharmaceutical Company Limited
- **Announced / Closed:** 2017-01-09 / 2017-02-16
- **Deal size:** $4.7B  ·  $24.00/sh
- **Premium (vs unaffected):** 89%
- **Stage:** 1 marketed drug + 1 NDA review asset
- **Value-inflecting events:** Divestiture of European operations to Incyte; Brigatinib NDA Review / FDA PDUFA date set; Iclusig relaunch following FDA safety suspension
- **Offer range (low→high):** $20.00 → $24.00
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 20.4 months
- **Reported early (1mo+):** yes — Bloomberg reported Baxalta talks 16 months early; FiercePharma rumors 3 years early
- **Trailing return to unaffected:** 3mo +25% · 6mo +53% · 12mo +110% · 2yr +103%

### CoLucid Pharmaceuticals, Inc. (CLCD)
- **Acquirer:** Eli Lilly and Company
- **Announced / Closed:** 2017-01-18 / 2017-03-01
- **Deal size:** $897M  ·  $46.50/sh
- **Premium (vs unaffected):** 29%
- **Stage:** Phase 3 lead
- **Value-inflecting events:** Positive top-line results from SAMURAI Phase 3 trial
- **Offer range (low→high):** $42.70 → $46.50
- **Interested parties:** 50
- **Interest direction:** both
- **Engagement → deal:** 4.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +29% · 6mo +421% · 12mo +434% · 2yr +352%

### Nabriva Therapeutics AG (NBRV)
- **Acquirer:** Nabriva Therapeutics plc
- **Announced / Closed:** 2017-04-18 / 2017-06-23
- **Deal size:** $2M  ·  $1.00/sh  + CVR
- **Premium (vs unaffected):** —
- **Stage:** Phase 3 lead
- **Value-inflecting events:** —
- **Offer range (low→high):** —
- **Interested parties:** 1
- **Interest direction:** outbound
- **Engagement → deal:** 0.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +124% · 6mo +53% · 12mo +30% · 2yr —

### Patheon N.V. (PTHN)
- **Acquirer:** Thermo Fisher Scientific Inc.
- **Announced / Closed:** 2017-05-15 / 2017-08-29
- **Deal size:** $5.1B  ·  $35.00/sh
- **Premium (vs unaffected):** 36%
- **Stage:** Commercial CDMO services
- **Value-inflecting events:** —
- **Offer range (low→high):** $33.00 → $35.00
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 2.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -9% · 6mo -6% · 12mo — · 2yr —

### Kite Pharma, Inc. (KITE)
- **Acquirer:** Gilead Sciences, Inc.
- **Announced / Closed:** 2017-08-28 / 2017-10-03
- **Deal size:** $10.3B  ·  $180.00/sh
- **Premium (vs unaffected):** 62%
- **Stage:** Registration/Pre-approval lead asset
- **Value-inflecting events:** Novartis CAR-T FDA advisory committee vote; Axi-cel nearing FDA approval; J.P. Morgan Healthcare Conference discussions
- **Offer range (low→high):** $127.00 → $180.00
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 7.9 months
- **Reported early (1mo+):** yes — Endpoints News + 7 months early
- **Trailing return to unaffected:** 3mo +36% · 6mo +130% · 12mo +97% · 2yr +106%

### Dimension Therapeutics, Inc. (DMTX)
- **Acquirer:** Ultragenyx Pharmaceutical Inc.
- **Announced / Closed:** 2017-10-03 / 2017-11-07
- **Deal size:** $151M  ·  $6.00/sh
- **Premium (vs unaffected):** 72%
- **Stage:** Phase 1/2 lead + multiple pre-clinical
- **Value-inflecting events:** DTX101 interim topline results failure; REGENXBIO definitive agreement announcement; Ultragenyx unsolicited cash proposal
- **Offer range (low→high):** $1.40 → $6.00
- **Interested parties:** 21
- **Interest direction:** both
- **Engagement → deal:** 0.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +203% · 6mo +88% · 12mo -41% · 2yr -72%

### Advanced Accelerator Applications S.A. (AAAP)
- **Acquirer:** Novartis AG
- **Announced / Closed:** 2017-10-30 / 2018-01-22
- **Deal size:** $3.6B  ·  $41.00/sh
- **Premium (vs unaffected):** -39%
- **Stage:** Approved (EU) / NDA Resubmitted (US), lead asset Lutathera
- **Value-inflecting events:** Lutathera European approval; Lutathera NDA resubmission (US)
- **Offer range (low→high):** $62.50 → $82.00
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 3.1 months
- **Reported early (1mo+):** yes — Bloomberg +1 month early (2017-09-27)
- **Trailing return to unaffected:** 3mo +73% · 6mo +70% · 12mo +78% · 2yr +142%

### Ocera Therapeutics, Inc. (OCRX)
- **Acquirer:** Mallinckrodt plc
- **Announced / Closed:** 2017-11-02 / 2017-12-11
- **Deal size:** $40M  ·  $1.52/sh  + CVR
- **Premium (vs unaffected):** 33%
- **Stage:** Phase 2b, pre-revenue
- **Value-inflecting events:** Phase 2b STOP-HE trial failed primary endpoint; Strategic Committee established to explore alternatives; Party A withdraws $1.60/share proposal; Mallinckrodt submits final $1.52/share + CVR offer
- **Offer range (low→high):** $1.52 → $1.52
- **Interested parties:** 34
- **Interest direction:** both
- **Engagement → deal:** 9.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -2% · 6mo -13% · 12mo -57% · 2yr -67%

### REPROS THERAPEUTICS INC. (RPRX)
- **Acquirer:** Allergan plc
- **Announced / Closed:** 2017-12-12 / 2018-01-31
- **Deal size:** $26M  ·  $0.67/sh
- **Premium (vs unaffected):** 63%
- **Stage:** Phase 3 (Enclomiphene) and Phase 2 (Proellex)
- **Value-inflecting events:** Enclomiphene regulatory review (EMA); Proellex Phase 2 development
- **Offer range (low→high):** $0.45 → $0.67
- **Interested parties:** 6
- **Interest direction:** inbound
- **Engagement → deal:** 8.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +17% · 6mo -51% · 12mo -77% · 2yr -68%

### Ignyta, Inc. (RXDX)
- **Acquirer:** Roche Holdings, Inc.
- **Announced / Closed:** 2017-12-22 / 2018-02-08
- **Deal size:** $1.8B  ·  $27.00/sh
- **Premium (vs unaffected):** 62%
- **Stage:** Phase 2 lead asset
- **Value-inflecting events:** Anticipated dual NDA submissions in 2018; Positive clinical data for entrectinib
- **Offer range (low→high):** $23.00 → $27.00
- **Interested parties:** 26
- **Interest direction:** both
- **Engagement → deal:** 19.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +79% · 6mo +142% · 12mo +145% · 2yr +22%

### Sucampo Pharmaceuticals, Inc. (SCMP)
- **Acquirer:** Mallinckrodt plc (Irish public limited company)
- **Announced / Closed:** 2017-12-26 / 2018-02-13
- **Deal size:** $851M  ·  $18.00/sh
- **Premium (vs unaffected):** 71%
- **Stage:** Commercial with 1 approved drug + Phase 3 pipeline
- **Value-inflecting events:** Vtesse, Inc. acquisition (VTS-270); Bloomberg sale rumor (Dec 7, 2017); AMITIZA pediatric sNDA Priority Review; Generic competition risk for AMITIZA
- **Offer range (low→high):** $17.00 → $18.00
- **Interested parties:** 5
- **Interest direction:** inbound
- **Engagement → deal:** 3.0 months
- **Reported early (1mo+):** no — Bloomberg reported sale consideration on Dec 7, 2017 (~19 days early)
- **Trailing return to unaffected:** 3mo -7% · 6mo +3% · 12mo -33% · 2yr -41%

### TiGenix NV (TIG)
- **Acquirer:** Takeda Pharmaceutical Company Limited
- **Announced / Closed:** 2018-01-05 / —
- **Deal size:** $527M  ·  $1.78/sh
- **Premium (vs unaffected):** 82%
- **Stage:** Approved (EU) / Phase 3 (US)
- **Value-inflecting events:** Positive CHMP Opinion for Cx601; Execution of Mesoblast Licensing Agreement; European marketing authorization for Cx601
- **Offer range (low→high):** $1.25 → $1.78
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 6.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -3% · 6mo +28% · 12mo +61% · 2yr —

### Bioverativ Inc. (BIVV)
- **Acquirer:** Sanofi
- **Announced / Closed:** 2018-01-22 / 2018-03-08
- **Deal size:** $11.4B  ·  $105.00/sh
- **Premium (vs unaffected):** 94%
- **Stage:** Commercial + 2 marketed drugs
- **Value-inflecting events:** Spin-off from Biogen; Acquisition of True North Therapeutics; Management presentation of long-range plans
- **Offer range (low→high):** $98.50 → $105.00
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 8.4 months
- **Reported early (1mo+):** yes — Spin-Off Research + 1 year early
- **Trailing return to unaffected:** 3mo -5% · 6mo -14% · 12mo +22% · 2yr —

### Ablynx NV (ABLX)
- **Acquirer:** Sanofi
- **Announced / Closed:** 2018-01-29 / —
- **Deal size:** $3.4B  ·  $45.00/sh
- **Premium (vs unaffected):** 21%
- **Stage:** Pre-marketing lead asset + Phase 2 pipeline
- **Value-inflecting events:** Novo Nordisk public disclosure of unsolicited bid; Caplacizumab (Capla) pre-marketing stage; Sanofi superior offer reports
- **Offer range (low→high):** $26.75 → $45.00
- **Interested parties:** 10
- **Interest direction:** both
- **Engagement → deal:** 0.7 months
- **Reported early (1mo+):** yes — Novo Nordisk private bid on 2017-12-07 (reported 2018-01-08)
- **Trailing return to unaffected:** 3mo — · 6mo — · 12mo — · 2yr —

### AveXis, Inc. (AVXS)
- **Acquirer:** Novartis AG
- **Announced / Closed:** 2018-04-09 / 2018-05-15
- **Deal size:** $8.0B  ·  $218.00/sh  + CVR
- **Premium (vs unaffected):** 59%
- **Stage:** Phase 3 / BLA Preparation
- **Value-inflecting events:** Alignment with FDA on BLA submission for AVXS-101; Compelling clinical data in SMA; Novartis licensing Spark Therapeutics' Luxturna
- **Offer range (low→high):** $112.00 → $218.00
- **Interested parties:** 4
- **Interest direction:** inbound
- **Engagement → deal:** 1.7 months
- **Reported early (1mo+):** yes — HC Sleuth / Investors Hub + 20 months early
- **Trailing return to unaffected:** 3mo +37% · 6mo +47% · 12mo +90% · 2yr +482%

### ARMO BioSciences, Inc. (ARMO)
- **Acquirer:** Eli Lilly and Company
- **Announced / Closed:** 2018-05-10 / 2018-06-22
- **Deal size:** $1.5B  ·  $50.00/sh
- **Premium (vs unaffected):** 39%
- **Stage:** Phase 3 lead asset, pre-revenue
- **Value-inflecting events:** ARMO IPO and post-IPO volatility; Competitor releases positive clinical data; Eli Lilly acquisition announcement
- **Offer range (low→high):** $48.00 → $50.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 1.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +21% · 6mo — · 12mo — · 2yr —

### JUNIPER PHARMACEUTICALS INC (JNP)
- **Acquirer:** Catalent, Inc.
- **Announced / Closed:** 2018-07-03 / 2018-08-14
- **Deal size:** $128M  ·  $11.50/sh
- **Premium (vs unaffected):** 29%
- **Stage:** Phase 2b failure; commercial CDMO and progesterone gel business
- **Value-inflecting events:** Phase 2b failure of COL-1077; Strategic reprioritization announcement; Public announcement of strategic alternatives exploration
- **Offer range (low→high):** $8.00 → $11.50
- **Interested parties:** 38
- **Interest direction:** both
- **Engagement → deal:** 4.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +1% · 6mo +77% · 12mo +98% · 2yr +13%

### TESARO, Inc. (TSRO)
- **Acquirer:** GlaxoSmithKline plc
- **Announced / Closed:** 2018-12-03 / 2019-01-22
- **Deal size:** $4.1B  ·  $75.00/sh
- **Premium (vs unaffected):** 148%
- **Stage:** Marketed lead + Phase 3 pipeline
- **Value-inflecting events:** ZEJULA Phase 3 data; Decision to cease marketing VARUBI IV; GSK acquisition interest shift
- **Offer range (low→high):** $66.00 → $75.00
- **Interested parties:** 10
- **Interest direction:** both
- **Engagement → deal:** 5.8 months
- **Reported early (1mo+):** yes — StreetInsider / Fierce Pharma reported sale process 18 months early
- **Trailing return to unaffected:** 3mo +12% · 6mo -39% · 12mo -73% · 2yr -77%

### Loxo Oncology, Inc. (LOXO)
- **Acquirer:** Eli Lilly and Company
- **Announced / Closed:** 2019-01-07 / 2019-02-15
- **Deal size:** $7.2B  ·  $235.00/sh
- **Premium (vs unaffected):** 74%
- **Stage:** 1 approved drug + Phase 1/2 lead asset
- **Value-inflecting events:** —
- **Offer range (low→high):** $230.00 → $235.00
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 8.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -16% · 6mo -25% · 12mo +62% · 2yr +254%

### Immune Design Corp. (IMDZ)
- **Acquirer:** Merck & Co., Inc.
- **Announced / Closed:** 2019-02-21 / 2019-04-02
- **Deal size:** $283M  ·  $5.85/sh
- **Premium (vs unaffected):** 312%
- **Stage:** Phase 2 lead + Phase 3 discontinued
- **Value-inflecting events:** G100 + pembrolizumab Phase 1/2 data (ASCO 2017); CMB305 + checkpoint inhibitor data (ESMO 2017); Discontinuation of Phase 3 SYNOVATE trial; G100 + pembrolizumab ASH 2018 data
- **Offer range (low→high):** $5.18 → $5.85
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 5.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -14% · 6mo -67% · 12mo -62% · 2yr -74%

### Spark Therapeutics, Inc. (ONCE)
- **Acquirer:** Roche Holding Ltd
- **Announced / Closed:** 2019-02-25 / 2019-12-17
- **Deal size:** $4.4B  ·  $114.50/sh
- **Premium (vs unaffected):** 164%
- **Stage:** Phase 3 lead + 1 approved drug
- **Value-inflecting events:** —
- **Offer range (low→high):** $70.00 → $114.50
- **Interested parties:** 3
- **Interest direction:** both
- **Engagement → deal:** 4.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -6% · 6mo -41% · 12mo -25% · 2yr -31%

### Osiris Therapeutics, Inc. (OSIR)
- **Acquirer:** Smith & Nephew plc (English public limited company)
- **Announced / Closed:** 2019-03-12 / 2019-04-17
- **Deal size:** $656M  ·  $19.00/sh
- **Premium (vs unaffected):** 24%
- **Stage:** Commercial (multiple products) + royalty interest
- **Value-inflecting events:** Nasdaq delisting notice (March 2017); Nasdaq re-listing (August 2018); Appointment of Samson Tom as CEO (November 2018); Merger Agreement announcement (March 2019)
- **Offer range (low→high):** $17.50 → $19.00
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 8.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +46% · 6mo +72% · 12mo +296% · 2yr +165%

### ARRAY BIOPHARMA INC (ARRY)
- **Acquirer:** Pfizer Inc.
- **Announced / Closed:** 2019-06-17 / 2019-07-30
- **Deal size:** $10.7B  ·  $48.00/sh
- **Premium (vs unaffected):** 120%
- **Stage:** Approved drugs + Phase 3 lead asset
- **Value-inflecting events:** Positive interim results from Phase 3 BEACON CRC trial
- **Offer range (low→high):** $44.00 → $48.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 2.9 months
- **Reported early (1mo+):** yes — Fierce Pharma + 29 months early
- **Trailing return to unaffected:** 3mo -5% · 6mo +33% · 12mo +39% · 2yr +141%

### Alder BioPharmaceuticals, Inc. (ALDR)
- **Acquirer:** H. Lundbeck A/S
- **Announced / Closed:** 2019-09-16 / 2019-10-22
- **Deal size:** $1.5B  ·  $18.00/sh  + CVR
- **Premium (vs unaffected):** 88%
- **Stage:** BLA submitted / Phase 3 lead
- **Value-inflecting events:** Eptinezumab BLA submission; Eptinezumab Phase 3 data
- **Offer range (low→high):** $14.00 → $18.00
- **Interested parties:** 11
- **Interest direction:** both
- **Engagement → deal:** 8.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -11% · 6mo -33% · 12mo -48% · 2yr -12%

### Dova Pharmaceuticals, Inc. (DOVA)
- **Acquirer:** Swedish Orphan Biovitrum AB (publ)
- **Announced / Closed:** 2019-09-30 / 2019-11-12
- **Deal size:** $793M  ·  $27.50/sh  + CVR
- **Premium (vs unaffected):** 83%
- **Stage:** Approved lead asset + Phase 3 pipeline
- **Value-inflecting events:** FDA approval of Doptelet for ITP; Phase 3 potential in CIT
- **Offer range (low→high):** $23.00 → $29.00
- **Interested parties:** 28
- **Interest direction:** both
- **Engagement → deal:** 20.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +70% · 6mo +85% · 12mo -41% · 2yr -46%

### The Medicines Company (MDCO)
- **Acquirer:** Novartis AG
- **Announced / Closed:** 2019-11-24 / 2020-01-06
- **Deal size:** $6.8B  ·  $85.00/sh
- **Premium (vs unaffected):** 49%
- **Stage:** Phase 3 lead asset
- **Value-inflecting events:** Positive ORION-3 data; Positive Phase 3 clinical trial data for inclisiran
- **Offer range (low→high):** $74.03 → $85.00
- **Interested parties:** 12
- **Interest direction:** both
- **Engagement → deal:** 5.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +54% · 6mo +80% · 12mo +135% · 2yr +84%

### Audentes Therapeutics, Inc. (BOLD)
- **Acquirer:** Astellas Pharma Inc.
- **Announced / Closed:** 2019-12-02 / 2020-01-15
- **Deal size:** $2.8B  ·  $60.00/sh
- **Premium (vs unaffected):** 106%
- **Stage:** Phase 1/2 lead asset
- **Value-inflecting events:** —
- **Offer range (low→high):** $49.00 → $60.00
- **Interested parties:** 4
- **Interest direction:** inbound
- **Engagement → deal:** 6.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -23% · 6mo -23% · 12mo -1% · 2yr -0%

### Synthorx, Inc. (THOR)
- **Acquirer:** Sanofi
- **Announced / Closed:** 2019-12-08 / 2020-01-23
- **Deal size:** $2.2B  ·  $68.00/sh
- **Premium (vs unaffected):** 324%
- **Stage:** Clinical-stage lead asset + pre-clinical pipeline
- **Value-inflecting events:** Initial Public Offering; Sanofi non-binding partnering term sheet; Sanofi unsolicited acquisition offer; Company A unsolicited $62.00 per share offer
- **Offer range (low→high):** $36.00 → $68.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 13.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +7% · 6mo -4% · 12mo +27% · 2yr —

### ArQule, Inc. (ARQL)
- **Acquirer:** Merck Sharp & Dohme Corp.
- **Announced / Closed:** 2019-12-09 / 2020-01-16
- **Deal size:** $2.4B  ·  $20.00/sh
- **Premium (vs unaffected):** 177%
- **Stage:** Phase 1 lead + multiple clinical assets
- **Value-inflecting events:** ASH Conference Phase 1 ARQ 531 data; Merck acquisition proposal; Merck partnership interest
- **Offer range (low→high):** $18.00 → $20.00
- **Interested parties:** 10
- **Interest direction:** inbound
- **Engagement → deal:** 5.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +35% · 6mo +51% · 12mo +128% · 2yr +29%

### Dermira, Inc. (DERM)
- **Acquirer:** Eli Lilly and Company
- **Announced / Closed:** 2020-01-10 / 2020-02-20
- **Deal size:** $1.0B  ·  $18.75/sh
- **Premium (vs unaffected):** 48%
- **Stage:** Phase 3 lead + 1 approved drug
- **Value-inflecting events:** —
- **Offer range (low→high):** $13.00 → $18.75
- **Interested parties:** 13
- **Interest direction:** outbound
- **Engagement → deal:** 4.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +42% · 6mo +26% · 12mo +17% · 2yr -54%

### Forty Seven, Inc. (FTSV)
- **Acquirer:** Gilead Sciences, Inc.
- **Announced / Closed:** 2020-03-02 / 2020-04-07
- **Deal size:** $4.6B  ·  $95.50/sh
- **Premium (vs unaffected):** 159%
- **Stage:** Phase 2 lead
- **Value-inflecting events:** Updated clinical data for magrolimab in MDS and AML (Dec 2019); Bloomberg reports Gilead takeover approach (Feb 2020)
- **Offer range (low→high):** $57.50 → $95.50
- **Interested parties:** 4
- **Interest direction:** inbound
- **Engagement → deal:** 1.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +388% · 6mo +340% · 12mo +146% · 2yr +130%

### QIAGEN N.V. (QGEN)
- **Acquirer:** Thermo Fisher Scientific Inc.
- **Announced / Closed:** 2020-03-03 / —
- **Deal size:** —  ·  $39.00/sh
- **Premium (vs unaffected):** 25%
- **Stage:** Marketed diagnostics and sample technologies
- **Value-inflecting events:** CEO resignation and sales guidance reduction; Receipt of multiple non-binding indications of interest; Review of strategic alternatives
- **Offer range (low→high):** $39.00 → $39.00
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 3.7 months
- **Reported early (1mo+):** yes — Bloomberg reported Thermo Fisher approach 4 months early (Nov 2019)
- **Trailing return to unaffected:** 3mo +10% · 6mo -9% · 12mo -8% · 2yr -2%

### STEMLINE THERAPEUTICS INC (STML)
- **Acquirer:** A. Menarini - Industrie Farmaceutiche Riunite - S.r.l.
- **Announced / Closed:** 2020-05-04 / 2020-06-10
- **Deal size:** $604M  ·  $11.50/sh  + CVR
- **Premium (vs unaffected):** 158%
- **Stage:** Marketed (US) / Pending (EU)
- **Value-inflecting events:** ELZONRIS US marketing approval; Pending EU approval for ELZONRIS
- **Offer range (low→high):** $10.00 → $11.50
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 11.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -59% · 6mo -52% · 12mo -69% · 2yr -76%

### Portola Pharmaceuticals, Inc. (PTLA)
- **Acquirer:** Alexion Pharmaceuticals, Inc.
- **Announced / Closed:** 2020-05-05 / 2020-07-02
- **Deal size:** $1.4B  ·  $18.00/sh
- **Premium (vs unaffected):** 179%
- **Stage:** Marketed (Accelerated Approval) + Phase 2
- **Value-inflecting events:** Q4 2019 Andexxa revenue miss; COVID-19 pandemic market impact; Regained Japan rights from BMS/Pfizer
- **Offer range (low→high):** $16.00 → $18.00
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 8.3 months
- **Reported early (1mo+):** yes — Forbes + Motley Fool; multiple years early
- **Trailing return to unaffected:** 3mo -73% · 6mo -76% · 12mo -83% · 2yr -84%

### Momenta Pharmaceuticals (MNTA)
- **Acquirer:** Johnson & Johnson
- **Announced / Closed:** 2020-06-15 / 2020-10-01
- **Deal size:** $6.2B  ·  $52.50/sh
- **Premium (vs unaffected):** 94%
- **Stage:** Phase 2 lead + 1 marketed drug
- **Value-inflecting events:** Positive Phase 1 data in myasthenia gravis; Positive M281 Phase 2 interim data; FDA rare pediatric disease designation for M281; J&J Board approval of final offer
- **Offer range (low→high):** $47.50 → $52.50
- **Interested parties:** 3
- **Interest direction:** inbound
- **Engagement → deal:** 14.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -40% · 6mo -29% · 12mo -3% · 2yr +24%

### Tetraphase Pharmaceuticals, Inc. (TTPH)
- **Acquirer:** La Jolla Pharmaceutical Company (California corporation)
- **Announced / Closed:** 2020-06-24 / 2020-07-28
- **Deal size:** $14M  ·  $2.00/sh  + CVR
- **Premium (vs unaffected):** -24%
- **Stage:** Commercial-stage, 1 approved drug + Phase 2 lead
- **Value-inflecting events:** IGNITE3 Phase 3 trial failure in cUTI; XERAVA FDA approval; La Jolla unsolicited cash proposal; Melinta unsolicited superior proposal
- **Offer range (low→high):** $1.24 → $2.00
- **Interested parties:** 16
- **Interest direction:** both
- **Engagement → deal:** 17.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +17% · 6mo +8% · 12mo +230% · 2yr -29%

### Pfenex Inc. (PFNX)
- **Acquirer:** Ligand Pharmaceuticals Incorporated
- **Announced / Closed:** 2020-08-10 / 2020-10-01
- **Deal size:** $412M  ·  $12.00/sh  + CVR
- **Premium (vs unaffected):** 46%
- **Stage:** Approved lead asset + commercial platform
- **Value-inflecting events:** FDA approval of PF708 (Bonsity); COVID-19 market dislocation; FDA General Advice Letter delaying TE Rating; Merger Agreement with Ligand
- **Offer range (low→high):** $10.50 → $12.00
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 5.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -10% · 6mo -35% · 12mo +33% · 2yr +67%

### Principia Biopharma Inc. (PRNB)
- **Acquirer:** Sanofi
- **Announced / Closed:** 2020-08-16 / 2020-09-28
- **Deal size:** $3.3B  ·  $100.00/sh
- **Premium (vs unaffected):** 26%
- **Stage:** Phase 3 initiated + Phase 2b lead asset
- **Value-inflecting events:** Positive Phase 2b data for PRN2246 in MS (Feb 2020); Confirmation of Phase 2b secondary endpoints (Apr 2020); Sanofi decision to proceed to Phase 3 trials (May 2020); Bloomberg report of Sanofi acquisition interest (Jul 2020)
- **Offer range (low→high):** $76.00 → $100.00
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 2.9 months
- **Reported early (1mo+):** yes — Bloomberg +1 month early (July 16, 2020)
- **Trailing return to unaffected:** 3mo +321% · 6mo +488% · 12mo +335% · 2yr +143%

### Akcea Therapeutics, Inc. (AKCA)
- **Acquirer:** Ionis Pharmaceuticals, Inc.
- **Announced / Closed:** 2020-08-31 / 2020-10-12
- **Deal size:** $1.8B  ·  $18.15/sh
- **Premium (vs unaffected):** 67%
- **Stage:** Phase 3 lead + 2 approved drugs
- **Value-inflecting events:** —
- **Offer range (low→high):** $16.00 → $18.15
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 1.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -28% · 6mo -37% · 12mo -48% · 2yr -59%

### IMMUNOMEDICS INC (IMMU)
- **Acquirer:** Gilead Sciences, Inc.
- **Announced / Closed:** 2020-09-13 / 2020-10-23
- **Deal size:** $20.4B  ·  $88.00/sh
- **Premium (vs unaffected):** 120%
- **Stage:** FDA approved (accelerated) + Phase 3 confirmatory
- **Value-inflecting events:** ASCENT Study halted for efficacy; FDA approval of Trodelvy for mTNBC; Topline results for ASCENT Study; Positive Phase 2 TROPHY study results
- **Offer range (low→high):** $55.00 → $88.00
- **Interested parties:** 12
- **Interest direction:** both
- **Engagement → deal:** 20.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +18% · 6mo +118% · 12mo +168% · 2yr +80%

### AMAG PHARMACEUTICALS, INC. (AMAG)
- **Acquirer:** Covis Group S.à r.l.
- **Announced / Closed:** 2020-10-01 / 2020-11-16
- **Deal size:** $474M  ·  $13.75/sh
- **Premium (vs unaffected):** 34%
- **Stage:** Commercial with Phase 3 pipeline
- **Value-inflecting events:** Strategic review and CEO transition announcement; Divestiture of Intrarosa to Millicent Pharma; Discontinuation of AMAG-423 Phase 2b/3a study; Divestiture of Vyleesi rights to Palatin
- **Offer range (low→high):** $11.00 → $13.75
- **Interested parties:** 17
- **Interest direction:** inbound
- **Engagement → deal:** 10.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +33% · 6mo +33% · 12mo -6% · 2yr -54%

### MyoKardia, Inc. (MYOK)
- **Acquirer:** Bristol-Myers Squibb Company
- **Announced / Closed:** 2020-10-05 / 2020-11-17
- **Deal size:** $12.0B  ·  $225.00/sh
- **Premium (vs unaffected):** 99%
- **Stage:** Phase 3 lead + clinical-stage pipeline
- **Value-inflecting events:** Positive Phase 3 EXPLORER-HCM study results; Breakthrough Therapy Designation for mavacamten
- **Offer range (low→high):** $185.00 → $225.00
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 19.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +15% · 6mo +80% · 12mo +116% · 2yr +114%

### BioSpecifics Technologies Corp. (BSTC)
- **Acquirer:** Endo International plc
- **Announced / Closed:** 2020-10-19 / 2020-12-02
- **Deal size:** $650M  ·  $88.50/sh
- **Premium (vs unaffected):** 56%
- **Stage:** Marketed + 1 approved drug (launching 2021)
- **Value-inflecting events:** FDA approval of Qwo for cellulite; XIAFLEX marketed for Dupuytren's and Peyronie's; Phase 2 pipeline for CCH indications
- **Offer range (low→high):** $85.00 → $88.50
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 2.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -6% · 6mo +28% · 12mo -2% · 2yr -10%

### Prevail Therapeutics Inc. (PRVL)
- **Acquirer:** Eli Lilly and Company
- **Announced / Closed:** 2020-12-15 / 2021-01-22
- **Deal size:** $771M  ·  $22.50/sh  + CVR
- **Premium (vs unaffected):** 131%
- **Stage:** Clinical-stage gene therapy
- **Value-inflecting events:** —
- **Offer range (low→high):** $21.00 → $22.50
- **Interested parties:** 20
- **Interest direction:** both
- **Engagement → deal:** 17.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -24% · 6mo -34% · 12mo -8% · 2yr —

### Viela Bio, Inc. (VIE)
- **Acquirer:** Horizon Therapeutics plc
- **Announced / Closed:** 2021-02-01 / 2021-03-15
- **Deal size:** $2.9B  ·  $53.00/sh
- **Premium (vs unaffected):** 47%
- **Stage:** Approved/Marketed lead asset + Phase 3 pipeline
- **Value-inflecting events:** —
- **Offer range (low→high):** $44.00 → $53.00
- **Interested parties:** 9
- **Interest direction:** both
- **Engagement → deal:** 7.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +26% · 6mo -16% · 12mo +40% · 2yr —

### Pandion Therapeutics, Inc. (PAND)
- **Acquirer:** Merck & Co., Inc.
- **Announced / Closed:** 2021-02-25 / 2021-04-01
- **Deal size:** $1.8B  ·  $60.00/sh
- **Premium (vs unaffected):** 231%
- **Stage:** Phase 1a lead + preclinical platform
- **Value-inflecting events:** Initial Public Offering; Positive Phase 1a data for PT-101
- **Offer range (low→high):** $40.00 → $60.00
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 34.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +60% · 6mo +2% · 12mo — · 2yr —

### Five Prime Therapeutics, Inc. (FPRX)
- **Acquirer:** Amgen Inc.
- **Announced / Closed:** 2021-03-04 / 2021-04-16
- **Deal size:** $1.7B  ·  $38.00/sh
- **Premium (vs unaffected):** -9%
- **Stage:** Clinical-stage, Phase 2 lead asset
- **Value-inflecting events:** FIGHT trial topline results (Bema); $174.0 million public stock offering; Strategic interest from multiple parties; Amgen acquisition announcement
- **Offer range (low→high):** $25.00 → $38.00
- **Interested parties:** 15
- **Interest direction:** outbound
- **Engagement → deal:** 19.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +685% · 6mo +685% · 12mo +685% · 2yr +278%

### CONSTELLATION PHARMACEUTICALS INC (CNST)
- **Acquirer:** MorphoSys AG
- **Announced / Closed:** 2021-06-02 / 2021-07-15
- **Deal size:** $1.6B  ·  $34.00/sh
- **Premium (vs unaffected):** 57%
- **Stage:** Phase 3 lead + Phase 2 pipeline
- **Value-inflecting events:** —
- **Offer range (low→high):** $29.00 → $34.00
- **Interested parties:** 9
- **Interest direction:** both
- **Engagement → deal:** 10.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -34% · 6mo +10% · 12mo -40% · 2yr +132%

### Translate Bio, Inc. (TBIO)
- **Acquirer:** Sanofi
- **Announced / Closed:** 2021-08-03 / 2021-09-14
- **Deal size:** $2.9B  ·  $38.00/sh
- **Premium (vs unaffected):** 30%
- **Stage:** Clinical stage (MRT5005 and MRT5500)
- **Value-inflecting events:** —
- **Offer range (low→high):** $28.00 → $38.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 2.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo — · 6mo — · 12mo — · 2yr —

### ACCELERON PHARMA INC (XLRN)
- **Acquirer:** Merck & Co., Inc.
- **Announced / Closed:** 2021-09-30 / 2021-11-19
- **Deal size:** $11.0B  ·  $180.00/sh
- **Premium (vs unaffected):** 39%
- **Stage:** Phase 3 lead + 1 approved drug
- **Value-inflecting events:** Sotatercept Phase 3 (STELLAR trial) prospects; Reblozyl commercialization and royalty stream
- **Offer range (low→high):** $160.00 → $180.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 2.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -1% · 6mo -5% · 12mo +35% · 2yr +221%

### Adamas Pharmaceuticals Inc (ADMS)
- **Acquirer:** Supernus Pharmaceuticals, Inc.
- **Announced / Closed:** 2021-10-10 / —
- **Deal size:** $371M  ·  $8.10/sh  + CVR
- **Premium (vs unaffected):** 78%
- **Stage:** Commercial with 2 approved drugs + Phase 3/Regulatory
- **Value-inflecting events:** Gocovri failed clinical trial in MS; Merger announcement with Supernus Pharmaceuticals
- **Offer range (low→high):** $8.10 → $8.10
- **Interested parties:** 1
- **Interest direction:** unclear
- **Engagement → deal:** —
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -11% · 6mo -9% · 12mo +6% · 2yr +14%

### Flexion Therapeutics Inc (FLXN)
- **Acquirer:** Pacira BioSciences, Inc.
- **Announced / Closed:** 2021-10-11 / 2021-11-19
- **Deal size:** $428M  ·  $8.50/sh  + CVR
- **Premium (vs unaffected):** 40%
- **Stage:** Commercial + Phase 1/2 pipeline
- **Value-inflecting events:** ZILRETTA FDA approval; ZILRETTA commercial rollout; FX-201 clinical development; FX-301 clinical development
- **Offer range (low→high):** $7.50 → $8.50
- **Interested parties:** 21
- **Interest direction:** inbound
- **Engagement → deal:** 4.7 months
- **Reported early (1mo+):** yes — FiercePharma + 4 years early
- **Trailing return to unaffected:** 3mo -35% · 6mo -49% · 12mo -49% · 2yr -58%

### Dicerna Pharmaceuticals, Inc. (DRNA)
- **Acquirer:** Novo Nordisk A/S (Danish aktieselskab)
- **Announced / Closed:** 2021-11-18 / 2021-12-28
- **Deal size:** $3.0B  ·  $38.25/sh
- **Premium (vs unaffected):** 80%
- **Stage:** Late-stage development (planned marketing applications for nedosiran)
- **Value-inflecting events:** Sharp mid-week decline (August 2021); Announcement of Merger Agreement with Novo Nordisk
- **Offer range (low→high):** $32.50 → $38.25
- **Interested parties:** 3
- **Interest direction:** inbound
- **Engagement → deal:** 3.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -44% · 6mo -27% · 12mo +4% · 2yr -6%

### ZOGENIX, INC. (ZGNX)
- **Acquirer:** UCB S.A. (société anonyme formed under the laws of Belgium; principal executive office: Allée de la Recherche, 60, 1070 Brussels, Belgium)
- **Announced / Closed:** 2022-01-19 / 2022-03-07
- **Deal size:** $1.5B  ·  $26.00/sh  + CVR
- **Premium (vs unaffected):** 86%
- **Stage:** Commercial (1 approved drug) + Phase 3/sNDA expansion
- **Value-inflecting events:** Positive top-line Phase 3 LGS trial results (Feb 2020); Dilutive $200M convertible senior notes offering (Sept 2020); UCB acquisition announcement (Jan 2022)
- **Offer range (low→high):** $20.50 → $26.00
- **Interested parties:** 3
- **Interest direction:** inbound
- **Engagement → deal:** 6.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -8% · 6mo -22% · 12mo -30% · 2yr -73%

### BioDelivery Sciences International Inc. (BDSI)
- **Acquirer:** Collegium Pharmaceuticals Inc.
- **Announced / Closed:** 2022-02-14 / 2022-03-22
- **Deal size:** $569M  ·  $5.60/sh
- **Premium (vs unaffected):** 60%
- **Stage:** Commercial stage + Phase 3
- **Value-inflecting events:** BELBUCA patent litigation favorable ruling; ELYXYB launch plans for 2022; Initial outreach from Collegium (Dec 2021); Merger announcement at $5.60 per share
- **Offer range (low→high):** $4.60 → $5.60
- **Interested parties:** 4
- **Interest direction:** inbound
- **Engagement → deal:** 1.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +8% · 6mo +13% · 12mo -19% · 2yr -33%

### Checkmate Pharmaceuticals, Inc. (CMPI)
- **Acquirer:** Regeneron Pharmaceuticals, Inc.
- **Announced / Closed:** 2022-04-19 / 2022-05-31
- **Deal size:** $231M  ·  $10.50/sh
- **Premium (vs unaffected):** 233%
- **Stage:** Phase 1b/2 lead asset
- **Value-inflecting events:** CEO transition; Clinical data milestone delays; Declining cash position
- **Offer range (low→high):** $7.50 → $10.50
- **Interested parties:** 6
- **Interest direction:** inbound
- **Engagement → deal:** 16.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +11% · 6mo -35% · 12mo -77% · 2yr -78%

### Entasis Therapeutics Holdings Inc. (ETTX)
- **Acquirer:** Innoviva, Inc.
- **Announced / Closed:** 2022-05-23 / 2022-07-11
- **Deal size:** $105M  ·  $2.20/sh
- **Premium (vs unaffected):** 17%
- **Stage:** Phase 3 lead + Phase 3 pipeline
- **Value-inflecting events:** Positive Phase 3 ATTACK trial data for SUL-DUR; Innoviva initial non-binding proposal ($1.80/share); Execution of $15 million bridge financing agreement
- **Offer range (low→high):** $1.80 → $2.20
- **Interested parties:** 35
- **Interest direction:** both
- **Engagement → deal:** 3.7 months
- **Reported early (1mo+):** yes — Endpoints News + 3 months early
- **Trailing return to unaffected:** 3mo +8% · 6mo -29% · 12mo -6% · 2yr -32%

### TherapeuticsMD, Inc. (TXMD)
- **Acquirer:** EW Healthcare Partners
- **Announced / Closed:** 2022-05-31 / —
- **Deal size:** $88M  ·  $10.00/sh
- **Premium (vs unaffected):** 367%
- **Stage:** Commercial with 3 approved drugs (IMVEXXY, ANNOVERA, BIJUVA)
- **Value-inflecting events:** ANNOVERA manufacturing failure rates; FDA sNDA approval (May 20, 2022); Sixth Street debt maturity/liquidity crisis; Sale of vitaMedMD and BocaGreenMD assets
- **Offer range (low→high):** $10.00 → $10.00
- **Interested parties:** 83
- **Interest direction:** outbound
- **Engagement → deal:** 4.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -29% · 6mo -73% · 12mo -83% · 2yr -83%

### Turning Point Therapeutics, Inc. (TPTX)
- **Acquirer:** Bristol-Myers Squibb Company
- **Announced / Closed:** 2022-06-03 / 2022-08-17
- **Deal size:** $3.8B  ·  $76.00/sh
- **Premium (vs unaffected):** 184%
- **Stage:** Phase 1/2 (Registrational) lead asset
- **Value-inflecting events:** Positive top-line BICR data for repotrectinib (TRIDENT-1 study)
- **Offer range (low→high):** $58.00 → $76.00
- **Interested parties:** 33
- **Interest direction:** outbound
- **Engagement → deal:** 4.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -25% · 6mo -36% · 12mo -65% · 2yr -57%

### Radius Health, Inc. (RDUS)
- **Acquirer:** Ginger Acquisition Inc.
- **Announced / Closed:** 2022-06-23 / 2022-08-15
- **Deal size:** $476M  ·  $10.00/sh  + CVR
- **Premium (vs unaffected):** 60%
- **Stage:** Commercial + Phase 2/3 pipeline
- **Value-inflecting events:** Abaloparatide transdermal patch Phase III trial failure; Activist investor 13D filing and proxy contest; Initiation of strategic review process
- **Offer range (low→high):** $9.00 → $10.00
- **Interested parties:** 70
- **Interest direction:** outbound
- **Engagement → deal:** 4.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -10% · 6mo -64% · 12mo -70% · 2yr -56%

### Epizyme, Inc. (EPZM)
- **Acquirer:** Ipsen S.A.
- **Announced / Closed:** 2022-06-27 / 2022-08-12
- **Deal size:** $244M  ·  $1.45/sh  + CVR
- **Premium (vs unaffected):** 222%
- **Stage:** Commercial + Phase 3 confirmatory
- **Value-inflecting events:** FDA approval of Tazverik; Ipsen initial outreach; Special Committee formation; Lease and debt cost reductions
- **Offer range (low→high):** $1.10 → $1.45
- **Interested parties:** 38
- **Interest direction:** inbound
- **Engagement → deal:** 6.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -70% · 6mo -87% · 12mo -95% · 2yr -97%

### LA JOLLA PHARMACEUTICAL CO (LJPC)
- **Acquirer:** Innoviva, Inc.
- **Announced / Closed:** 2022-07-11 / 2022-08-22
- **Deal size:** $155M  ·  $6.23/sh
- **Premium (vs unaffected):** 80%
- **Stage:** 2 approved drugs / Commercial
- **Value-inflecting events:** —
- **Offer range (low→high):** $4.90 → $6.23
- **Interested parties:** 25
- **Interest direction:** both
- **Engagement → deal:** 3.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -16% · 6mo -24% · 12mo -32% · 2yr -26%

### Forma Therapeutics Holdings, Inc. (FMTX)
- **Acquirer:** Novo Nordisk A/S
- **Announced / Closed:** 2022-09-01 / 2022-10-14
- **Deal size:** $957M  ·  $20.00/sh
- **Premium (vs unaffected):** 142%
- **Stage:** Phase 2/3 lead + NDA stage oncology asset
- **Value-inflecting events:** ASH Annual Meeting data; Out-licensing of olutasidenib to Rigel Pharmaceuticals
- **Offer range (low→high):** $8.20 → $20.00
- **Interested parties:** 4
- **Interest direction:** inbound
- **Engagement → deal:** 20.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +10% · 6mo -28% · 12mo -64% · 2yr -79%

### LogicBio Therapeutics, Inc. (LOGC)
- **Acquirer:** AstraZeneca PLC
- **Announced / Closed:** 2022-10-03 / 2022-11-16
- **Deal size:** $68M  ·  $2.07/sh
- **Premium (vs unaffected):** 71%
- **Stage:** Phase 1/2 lead + Preclinical platform
- **Value-inflecting events:** FDA clinical hold on Phase 1/2 SUNRISE trial; Nasdaq delisting notice; FDA lifts clinical hold on SUNRISE trial
- **Offer range (low→high):** $1.56 → $2.07
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 11.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -32% · 6mo -36% · 12mo -83% · 2yr -95%

### Akouos, Inc. (AKUS)
- **Acquirer:** Eli Lilly and Company
- **Announced / Closed:** 2022-10-18 / 2022-12-01
- **Deal size:** $462M  ·  $12.50/sh  + CVR
- **Premium (vs unaffected):** 142%
- **Stage:** Phase 1/2 (IND cleared) lead asset
- **Value-inflecting events:** FDA clearance of IND application for AK-OTOF
- **Offer range (low→high):** $9.00 → $12.50
- **Interested parties:** 4
- **Interest direction:** inbound
- **Engagement → deal:** 7.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +43% · 6mo +8% · 12mo -59% · 2yr -74%

### Applied Genetic Technologies Corporation (AGTC)
- **Acquirer:** Syncona Limited
- **Announced / Closed:** 2022-10-24 / 2022-11-30
- **Deal size:** $23M  ·  $0.34/sh  + CVR
- **Premium (vs unaffected):** 17%
- **Stage:** Phase 1/2 lead + clinical ocular portfolio
- **Value-inflecting events:** Nasdaq delisting notice; Critical liquidity shortfall/bankruptcy risk; July 2022 warrant issuance; Skyline/Vista Phase 1/2 trials
- **Offer range (low→high):** $0.34 → $1.07
- **Interested parties:** 33
- **Interest direction:** outbound
- **Engagement → deal:** 4.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -53% · 6mo -76% · 12mo -91% · 2yr -94%

### Oyster Point Pharma, Inc. (OYST)
- **Acquirer:** Viatris Inc.
- **Announced / Closed:** 2022-11-07 / 2023-01-03
- **Deal size:** $299M  ·  $11.00/sh  + CVR
- **Premium (vs unaffected):** 55%
- **Stage:** Approved/Marketed lead asset + Phase 2 pipeline
- **Value-inflecting events:** —
- **Offer range (low→high):** $10.00 → $11.00
- **Interested parties:** 9
- **Interest direction:** both
- **Engagement → deal:** 12.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +56% · 6mo -20% · 12mo -36% · 2yr -71%

### Imago BioSciences, Inc. (IMGO)
- **Acquirer:** Merck & Co., Inc.
- **Announced / Closed:** 2022-11-21 / 2023-01-11
- **Deal size:** $1.2B  ·  $36.00/sh
- **Premium (vs unaffected):** 137%
- **Stage:** Phase 2 lead asset
- **Value-inflecting events:** End-of-Phase 2 meeting with FDA; Clinical data presented at ASH 2022
- **Offer range (low→high):** $28.00 → $36.00
- **Interested parties:** 11
- **Interest direction:** both
- **Engagement → deal:** 21.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -13% · 6mo -15% · 12mo -42% · 2yr —

### ALBIREO PHARMA, INC. (ALBO)
- **Acquirer:** Ipsen S.A.
- **Announced / Closed:** 2023-01-09 / 2023-03-02
- **Deal size:** $876M  ·  $42.00/sh  + CVR
- **Premium (vs unaffected):** 97%
- **Stage:** Marketed + Phase 3 lead
- **Value-inflecting events:** —
- **Offer range (low→high):** $28.00 → $42.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 1.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +13% · 6mo +6% · 12mo -1% · 2yr -40%

### CinCor Pharma, Inc. (CINC)
- **Acquirer:** AstraZeneca PLC
- **Announced / Closed:** 2023-01-09 / 2023-02-24
- **Deal size:** $1.1B  ·  $26.00/sh  + CVR
- **Premium (vs unaffected):** 118%
- **Stage:** Phase 2 lead, pre-revenue
- **Value-inflecting events:** Positive Phase 2 BrigHtn trial results; Phase 2 HALO trial missed primary endpoint
- **Offer range (low→high):** $22.00 → $26.00
- **Interested parties:** 3
- **Interest direction:** inbound
- **Engagement → deal:** 20.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -60% · 6mo -19% · 12mo -25% · 2yr —

### Concert Pharmaceuticals, Inc. (CNCE)
- **Acquirer:** Sun Pharmaceutical Industries Ltd.
- **Announced / Closed:** 2023-01-19 / 2023-03-06
- **Deal size:** $498M  ·  $8.00/sh  + CVR
- **Premium (vs unaffected):** 70%
- **Stage:** Phase 3 lead asset
- **Value-inflecting events:** —
- **Offer range (low→high):** $7.00 → $8.00
- **Interested parties:** 40
- **Interest direction:** both
- **Engagement → deal:** 6.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -26% · 6mo +15% · 12mo +41% · 2yr -56%

### CHEMBIO DIAGNOSTICS, INC. (CEMI)
- **Acquirer:** Biosynex SA
- **Announced / Closed:** 2023-01-31 / 2023-04-27
- **Deal size:** $16M  ·  $0.45/sh
- **Premium (vs unaffected):** 105%
- **Stage:** Commercial + EUA Revoked
- **Value-inflecting events:** FDA revokes EUA for COVID-19 System; Nasdaq non-compliance notice; Abandoned $17M public offering; Engagement of Craig-Hallum for sale process
- **Offer range (low→high):** $0.40 → $0.45
- **Interested parties:** 81
- **Interest direction:** outbound
- **Engagement → deal:** 8.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -39% · 6mo -66% · 12mo -81% · 2yr -97%

### Provention Bio, Inc. (PRVB)
- **Acquirer:** Sanofi S.A.
- **Announced / Closed:** 2023-03-13 / 2023-04-27
- **Deal size:** $2.4B  ·  $25.00/sh
- **Premium (vs unaffected):** 140%
- **Stage:** Approved / Commercial lead asset + Phase 2 pipeline
- **Value-inflecting events:** Co-Promotion Agreement with Sanofi; FDA approval of TZIELD (teplizumab-mzwv); Sanofi equity investment
- **Offer range (low→high):** $21.00 → $25.00
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 15.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +25% · 6mo +85% · 12mo +64% · 2yr -22%

### Jounce Therapeutics, Inc. (JNCE)
- **Acquirer:** Concentra Biosciences, LLC
- **Announced / Closed:** 2023-03-27 / 2023-05-03
- **Deal size:** $97M  ·  $1.85/sh
- **Premium (vs unaffected):** 36%
- **Stage:** Phase 2 lead + multiple clinical/preclinical assets
- **Value-inflecting events:** Gilead GS-1811 buyout ($67M); Redx Pharma merger announcement; Concentra unsolicited $1.80 proposal; Concentra revised $1.85 proposal
- **Offer range (low→high):** $1.80 → $1.85
- **Interested parties:** 3
- **Interest direction:** both
- **Engagement → deal:** 0.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo — · 6mo — · 12mo — · 2yr —

### Satsuma Pharmaceuticals, Inc. (STSA)
- **Acquirer:** Shin Nippon Biomedical Laboratories, Ltd.
- **Announced / Closed:** 2023-04-16 / 2023-06-08
- **Deal size:** $30M  ·  $0.91/sh  + CVR
- **Premium (vs unaffected):** 12%
- **Stage:** Phase 3 lead (failed) + NDA Accepted
- **Value-inflecting events:** SUMMIT Phase 3 trial failure; Announcement of strategic alternatives exploration; STS101 NDA Acceptance
- **Offer range (low→high):** $0.91 → $0.91
- **Interested parties:** 30
- **Interest direction:** outbound
- **Engagement → deal:** 4.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -14% · 6mo -88% · 12mo -79% · 2yr -84%

### CTI BIOPHARMA CORP (CTIC)
- **Acquirer:** Swedish Orphan Biovitrum AB (publ)
- **Announced / Closed:** 2023-05-10 / 2023-06-26
- **Deal size:** $1.2B  ·  $9.10/sh
- **Premium (vs unaffected):** 115%
- **Stage:** Commercial / Phase 3 (label expansion)
- **Value-inflecting events:** —
- **Offer range (low→high):** $8.00 → $9.10
- **Interested parties:** 4
- **Interest direction:** inbound
- **Engagement → deal:** 2.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -22% · 6mo -21% · 12mo -12% · 2yr +94%

### VectivBio Holding AG (VECT)
- **Acquirer:** Ironwood Pharmaceuticals, Inc.
- **Announced / Closed:** 2023-05-22 / —
- **Deal size:** $1.1B  ·  $17.00/sh
- **Premium (vs unaffected):** 56%
- **Stage:** Phase 3 lead asset
- **Value-inflecting events:** —
- **Offer range (low→high):** $14.00 → $17.00
- **Interested parties:** 8
- **Interest direction:** inbound
- **Engagement → deal:** 2.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +42% · 6mo +47% · 12mo +113% · 2yr -27%

### GreenLight Biosciences Holdings, PBC (GRNA)
- **Acquirer:** SW ParentCo, Inc.
- **Announced / Closed:** 2023-05-30 / 2023-07-24
- **Deal size:** $46M  ·  $0.30/sh
- **Premium (vs unaffected):** -6%
- **Stage:** Pre-revenue, Launch 2024 (Agricultural) + Pre-clinical/Phase 1 (Human Health)
- **Value-inflecting events:** —
- **Offer range (low→high):** $0.30 → $0.30
- **Interested parties:** 140
- **Interest direction:** both
- **Engagement → deal:** 3.2 months
- **Reported early (1mo+):** yes — GlobeNewswire/BioSpace 2 months early
- **Trailing return to unaffected:** 3mo -70% · 6mo -82% · 12mo -96% · 2yr —

### Sigilon Therapeutics, Inc. (SGTX)
- **Acquirer:** Eli Lilly and Company
- **Announced / Closed:** 2023-06-29 / 2023-08-11
- **Deal size:** $37M  ·  $14.92/sh  + CVR
- **Premium (vs unaffected):** 204%
- **Stage:** Pre-clinical lead + Phase 1/2 clinical hold
- **Value-inflecting events:** FDA clinical hold on SIG-001; Strategic reprioritization and workforce reduction; Collapse of Party E reverse merger; Lilly whole-company acquisition proposal
- **Offer range (low→high):** $14.92 → $14.92
- **Interested parties:** 141
- **Interest direction:** both
- **Engagement → deal:** 63.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +463% · 6mo +965% · 12mo +505% · 2yr -53%

### PARDES BIOSCIENCES, INC. (PRDS)
- **Acquirer:** MediPacific, Inc.
- **Announced / Closed:** 2023-07-17 / 2023-08-31
- **Deal size:** $132M  ·  $2.13/sh
- **Premium (vs unaffected):** 13%
- **Stage:** Phase 2, suspended development
- **Value-inflecting events:** Phase 2 trial failure of pomotrelvir; Announcement of strategic review process
- **Offer range (low→high):** $1.93 → $2.13
- **Interested parties:** 144
- **Interest direction:** both
- **Engagement → deal:** 2.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +43% · 6mo +54% · 12mo -61% · 2yr -81%

### Decibel Therapeutics, Inc. (DBTX)
- **Acquirer:** Regeneron Pharmaceuticals, Inc.
- **Announced / Closed:** 2023-08-09 / 2023-09-25
- **Deal size:** $101M  ·  $4.00/sh  + CVR
- **Premium (vs unaffected):** 14%
- **Stage:** Phase 1/2 lead, pre-revenue
- **Value-inflecting events:** —
- **Offer range (low→high):** $3.25 → $4.00
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 4.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +13% · 6mo +38% · 12mo -30% · 2yr -53%

### Thorne HealthTech, Inc. (THRN)
- **Acquirer:** Healthspan Buyer, LLC
- **Announced / Closed:** 2023-08-28 / 2023-10-16
- **Deal size:** $551M  ·  $10.20/sh
- **Premium (vs unaffected):** 72%
- **Stage:** Commercial + OneDraw Regulatory Approval Pending
- **Value-inflecting events:** —
- **Offer range (low→high):** $7.00 → $10.20
- **Interested parties:** 38
- **Interest direction:** both
- **Engagement → deal:** 8.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +34% · 6mo +33% · 12mo +14% · 2yr -29%

### INTERCEPT PHARMACEUTICALS, INC. (ICPT)
- **Acquirer:** Alfasigma S.p.A.
- **Announced / Closed:** 2023-09-26 / 2023-11-08
- **Deal size:** $794M  ·  $19.00/sh
- **Premium (vs unaffected):** 76%
- **Stage:** Marketed (Conditional Approval) + Phase 2
- **Value-inflecting events:** FDA advisory committee negative vote on OCA for NASH; FDA Complete Response Letter for OCA in NASH; Discontinuation of NASH investment and restructuring
- **Offer range (low→high):** $12.00 → $19.00
- **Interested parties:** 18
- **Interest direction:** both
- **Engagement → deal:** 3.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +5% · 6mo -45% · 12mo -40% · 2yr -29%

### POINT Biopharma Global Inc. (PNT)
- **Acquirer:** Eli Lilly and Company
- **Announced / Closed:** 2023-10-03 / 2023-12-27
- **Deal size:** $1.3B  ·  $12.50/sh
- **Premium (vs unaffected):** 53%
- **Stage:** Phase 3 lead
- **Value-inflecting events:** —
- **Offer range (low→high):** $12.00 → $12.50
- **Interested parties:** 3
- **Interest direction:** inbound
- **Engagement → deal:** 3.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -12% · 6mo +7% · 12mo -20% · 2yr +12%

### Miromatrix Medical Inc. (MIRO)
- **Acquirer:** United Therapeutics Corporation
- **Announced / Closed:** 2023-10-30 / 2023-12-13
- **Deal size:** $89M  ·  $3.25/sh  + CVR
- **Premium (vs unaffected):** 148%
- **Stage:** Preclinical, bioengineered organ technology
- **Value-inflecting events:** March 2023 equity financing; May 2023 strategic partnering outreach; October 2023 merger agreement announcement
- **Offer range (low→high):** $2.75 → $5.00
- **Interested parties:** 51
- **Interest direction:** outbound
- **Engagement → deal:** 3.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -25% · 6mo -22% · 12mo -70% · 2yr -84%

### Icosavax, Inc. (ICVX)
- **Acquirer:** AstraZeneca PLC
- **Announced / Closed:** 2023-12-12 / 2024-02-19
- **Deal size:** $762M  ·  $15.00/sh  + CVR
- **Premium (vs unaffected):** 119%
- **Stage:** Phase 2 lead, Pre-revenue
- **Value-inflecting events:** Positive topline interim Phase 1 data for IVX-A12; Phase 2 topline data for IVX-A12
- **Offer range (low→high):** $12.00 → $15.00
- **Interested parties:** 14
- **Interest direction:** both
- **Engagement → deal:** 16.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -12% · 6mo -15% · 12mo +175% · 2yr -72%

### Theseus Pharmaceuticals, Inc. (THRX)
- **Acquirer:** Concentra Biosciences, LLC
- **Announced / Closed:** 2023-12-22 / 2024-02-14
- **Deal size:** $181M  ·  $4.05/sh
- **Premium (vs unaffected):** 12%
- **Stage:** Preclinical/Early Clinical, lead asset discontinued
- **Value-inflecting events:** Discontinuation of lead candidate THE-630; Public announcement of formal strategic review; Receipt of unsolicited proposal from Concentra; Receipt of joint interest from OrbiMed and Foresite
- **Offer range (low→high):** $3.80 → $4.05
- **Interested parties:** 71
- **Interest direction:** both
- **Engagement → deal:** 0.9 months
- **Reported early (1mo+):** yes — PR Newswire/Company Press Release + 1 month early
- **Trailing return to unaffected:** 3mo +16% · 6mo -67% · 12mo -45% · 2yr -68%

### RayzeBio, Inc. (RYZB)
- **Acquirer:** Bristol-Myers Squibb Company
- **Announced / Closed:** 2023-12-26 / 2024-02-26
- **Deal size:** $3.8B  ·  $62.50/sh
- **Premium (vs unaffected):** 173%
- **Stage:** Phase 3 lead asset
- **Value-inflecting events:** Lead asset RYZ101 enters Phase 3 for GEP-NETs; General sector interest in radiopharmaceuticals
- **Offer range (low→high):** $36.00 → $62.50
- **Interested parties:** 4
- **Interest direction:** inbound
- **Engagement → deal:** 1.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -5% · 6mo — · 12mo — · 2yr —

### MorphoSys AG (MOR)
- **Acquirer:** Novartis AG
- **Announced / Closed:** 2024-02-05 / 2024-05-31
- **Deal size:** $2.6B  ·  $68.00/sh
- **Premium (vs unaffected):** 89%
- **Stage:** Phase 3 lead oncology pipeline
- **Value-inflecting events:** —
- **Offer range (low→high):** $68.00 → $68.00
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 2.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +57% · 6mo +24% · 12mo +149% · 2yr +30%

### CymaBay Therapeutics, Inc. (CBAY)
- **Acquirer:** Gilead Sciences, Inc.
- **Announced / Closed:** 2024-02-12 / 2024-03-22
- **Deal size:** $3.7B  ·  $32.50/sh
- **Premium (vs unaffected):** 37%
- **Stage:** Phase 3 lead asset
- **Value-inflecting events:** Positive topline Phase 3 RESPONSE study results for seladelpar
- **Offer range (low→high):** $23.00 → $32.50
- **Interested parties:** 22
- **Interest direction:** inbound
- **Engagement → deal:** 13.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +76% · 6mo +105% · 12mo +265% · 2yr +603%

### Kinnate Biopharma Inc. (KNTE)
- **Acquirer:** XOMA Corporation
- **Announced / Closed:** 2024-02-16 / 2024-04-03
- **Deal size:** $122M  ·  $2.59/sh
- **Premium (vs unaffected):** 8%
- **Stage:** Clinical stage, Phase 1 lead asset
- **Value-inflecting events:** Exarafenib Phase 1 data market response; Strategic reprioritization and workforce restructuring; Sale of Exarafenib assets to Pierre Fabre
- **Offer range (low→high):** $2.17 → $2.59
- **Interested parties:** 119
- **Interest direction:** outbound
- **Engagement → deal:** 3.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +110% · 6mo -22% · 12mo -63% · 2yr -73%

### NGM Biopharmaceuticals, Inc. (NGM)
- **Acquirer:** The Column Group, LP (TCG) and affiliates
- **Announced / Closed:** 2024-02-26 / 2024-04-05
- **Deal size:** $129M  ·  $1.55/sh
- **Premium (vs unaffected):** 4%
- **Stage:** Clinical-stage, Phase 2 lead
- **Value-inflecting events:** Phase 2 ALPINE 4 aldafermin data in NASH (Oct 2022); TCG unsolicited expression of interest (Dec 2023); Strategy refocus on rare conditions (Jan 2024); Merger Agreement execution (Feb 2024)
- **Offer range (low→high):** $1.45 → $1.55
- **Interested parties:** 8
- **Interest direction:** inbound
- **Engagement → deal:** 8.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +94% · 6mo -35% · 12mo -71% · 2yr -90%

### Societal CDMO, Inc. (SCTL)
- **Acquirer:** CoreRx, Inc.
- **Announced / Closed:** 2024-02-28 / 2024-04-08
- **Deal size:** $116M  ·  $1.10/sh
- **Premium (vs unaffected):** 214%
- **Stage:** Commercial CDMO services + legacy products
- **Value-inflecting events:** Nasdaq deficiency letter; Establishment of Restructuring Committee; Strategic review of San Diego facility
- **Offer range (low→high):** $0.42 → $1.10
- **Interested parties:** 4
- **Interest direction:** outbound
- **Engagement → deal:** 4.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +0% · 6mo -60% · 12mo -74% · 2yr -80%

### ALPINE IMMUNE SCIENCES, INC. (ALPN)
- **Acquirer:** Vertex Pharmaceuticals Incorporated
- **Announced / Closed:** 2024-04-10 / 2024-05-20
- **Deal size:** $4.3B  ·  $65.00/sh
- **Premium (vs unaffected):** 81%
- **Stage:** Phase 1b/2a, Phase 3 planned
- **Value-inflecting events:** Phase 1b/2a data for povetacicept; American Society of Nephrology Kidney Week presentation
- **Offer range (low→high):** $60.00 → $65.00
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 12.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +113% · 6mo +188% · 12mo +397% · 2yr +349%

### Deciphera Pharmaceuticals, Inc. (DCPH)
- **Acquirer:** ONO Pharmaceutical Co., Ltd.
- **Announced / Closed:** 2024-04-29 / 2024-06-11
- **Deal size:** $2.2B  ·  $25.60/sh
- **Premium (vs unaffected):** 63%
- **Stage:** Phase 3 lead + 1 approved drug
- **Value-inflecting events:** FDA approval of QINLOCK; Positive top-line results from Phase 3 MOTION study of vimseltinib
- **Offer range (low→high):** $19.00 → $25.60
- **Interested parties:** 5
- **Interest direction:** inbound
- **Engagement → deal:** 22.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -2% · 6mo +24% · 12mo +2% · 2yr +62%

### Calliditas Therapeutics AB (publ) (CALT)
- **Acquirer:** Asahi Kasei Corporation
- **Announced / Closed:** 2024-05-28 / —
- **Deal size:** $12.5B  ·  $208.00/sh
- **Premium (vs unaffected):** 83%
- **Stage:** Commercial
- **Value-inflecting events:** —
- **Offer range (low→high):** $131.00 → $208.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 13.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -14% · 6mo +21% · 12mo -16% · 2yr +2%

### Morphic Holding, Inc. (MORF)
- **Acquirer:** Eli Lilly and Company
- **Announced / Closed:** 2024-07-08 / 2024-08-16
- **Deal size:** $2.9B  ·  $57.00/sh
- **Premium (vs unaffected):** 85%
- **Stage:** Phase 2b lead asset
- **Value-inflecting events:** —
- **Offer range (low→high):** $46.00 → $57.00
- **Interested parties:** 3
- **Interest direction:** both
- **Engagement → deal:** 42.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -17% · 6mo +13% · 12mo -50% · 2yr +27%

### G1 Therapeutics, Inc. (GTHX)
- **Acquirer:** Pharmacosmos A/S
- **Announced / Closed:** 2024-08-07 / 2024-09-18
- **Deal size:** $378M  ·  $7.15/sh
- **Premium (vs unaffected):** 185%
- **Stage:** Phase 3 lead + 1 approved drug
- **Value-inflecting events:** CRC Trial discontinuation; Interim TNBC Trial Data release; Final TNBC Trial results; COSELA commercialization
- **Offer range (low→high):** $2.25 → $7.15
- **Interested parties:** 14
- **Interest direction:** both
- **Engagement → deal:** 20.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -47% · 6mo -14% · 12mo +4% · 2yr -80%

### Revance Therapeutics, Inc. (RVNC)
- **Acquirer:** Crown Holdings Interco LLC (sole stockholder of Crown); Crown Laboratories Holdings, Inc. (sole member of Crown Interco); Hildred Capital Management, LLC (majority shareholder of Crown)
- **Announced / Closed:** 2024-08-12 / 2025-02-06
- **Deal size:** $383M  ·  $3.65/sh
- **Premium (vs unaffected):** 2%
- **Stage:** Commercial-stage, 2 primary products (DAXXIFY + RHA Collection)
- **Value-inflecting events:** Q1 2024 earnings miss and 23% stock drop; Teoxane SA breach notice and distribution agreement dispute; Going concern disclosure in Q3 2024 10-Q; DAXXIFY NMPA approvals in China
- **Offer range (low→high):** $2.25 → $6.66
- **Interested parties:** 16
- **Interest direction:** both
- **Engagement → deal:** 9.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -13% · 6mo -40% · 12mo -84% · 2yr -82%

### Longboard Pharmaceuticals, Inc. (LBPH)
- **Acquirer:** H. Lundbeck A/S
- **Announced / Closed:** 2024-10-14 / 2024-12-02
- **Deal size:** $2.3B  ·  $60.00/sh
- **Premium (vs unaffected):** 75%
- **Stage:** Phase 3 ready lead asset
- **Value-inflecting events:** Positive topline PACIFIC study data (bexicaserin); FDA Breakthrough Therapy designation for bexicaserin
- **Offer range (low→high):** $29.00 → $60.00
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 10.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +85% · 6mo +78% · 12mo +451% · 2yr +1014%

### Lumos Pharma, Inc. (LUMO)
- **Acquirer:** Double Point Ventures LLC
- **Announced / Closed:** 2024-10-23 / 2024-12-12
- **Deal size:** $37M  ·  $4.25/sh  + CVR
- **Premium (vs unaffected):** 8%
- **Stage:** Phase 3 ready, lead asset LUM-201
- **Value-inflecting events:** End of Phase 2 meeting with FDA; Engagement of Piper Sandler for sale process; Announcement of strategic alternatives evaluation
- **Offer range (low→high):** $2.83 → $4.25
- **Interested parties:** 51
- **Interest direction:** both
- **Engagement → deal:** 9.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +76% · 6mo +41% · 12mo +34% · 2yr -57%

### Poseida Therapeutics, Inc. (PSTV)
- **Acquirer:** F. Hoffmann-La Roche Ltd
- **Announced / Closed:** 2024-11-26 / 2025-01-08
- **Deal size:** $880M  ·  $9.00/sh  + CVR
- **Premium (vs unaffected):** 215%
- **Stage:** Phase 1/1b lead assets
- **Value-inflecting events:** Strategic global collaboration with Roche (July 2022); Astellas $50 million strategic investment (August 2023)
- **Offer range (low→high):** $5.75 → $9.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 44.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -28% · 6mo -20% · 12mo +26% · 2yr +221%

### MARINUS PHARMACEUTICALS, INC. (MRNS)
- **Acquirer:** Immedica Pharma AB
- **Announced / Closed:** 2024-12-30 / 2025-02-11
- **Deal size:** $30M  ·  $0.55/sh
- **Premium (vs unaffected):** 72%
- **Stage:** Commercial (CDD) + Phase 3 failures (RSE/TSC)
- **Value-inflecting events:** Phase 3 RAISE trial failed co-primary endpoint; Phase 3 TrustTSC trial failed primary endpoint; Discontinuation of ganaxolone clinical development; Commencement of strategic alternatives process
- **Offer range (low→high):** $0.50 → $0.55
- **Interested parties:** 77
- **Interest direction:** outbound
- **Engagement → deal:** 1.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -77% · 6mo -77% · 12mo -96% · 2yr -93%

### bluebird bio, Inc. (BLUE)
- **Acquirer:** Beacon Parent Holdings, L.P. (backed by The Carlyle Group and SK Capital Partners)
- **Announced / Closed:** 2025-02-21 / 2025-06-02
- **Deal size:** $29M  ·  $3.00/sh  + CVR
- **Premium (vs unaffected):** -62%
- **Stage:** Commercial with 3 approved gene therapies
- **Value-inflecting events:** FDA denial of PRV application for LYFGENIA; Severe cash runway crisis and restructuring; Unsolicited bid from Ayrmid Ltd; Amendment to include $5.00 all-cash election
- **Offer range (low→high):** $3.00 → $5.00
- **Interested parties:** 103
- **Interest direction:** both
- **Engagement → deal:** 3.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +1525% · 6mo +643% · 12mo +519% · 2yr +52%

### Chimerix, Inc. (CMRX)
- **Acquirer:** Jazz Pharmaceuticals Public Limited Company
- **Announced / Closed:** 2025-03-05 / 2025-04-21
- **Deal size:** $802M  ·  $8.55/sh
- **Premium (vs unaffected):** 117%
- **Stage:** Phase 3 lead + NDA accepted with priority review
- **Value-inflecting events:** NDA submission announcement for ONC201; FDA acceptance of NDA with priority review; Merger announcement at $8.55 per share
- **Offer range (low→high):** $5.00 → $8.55
- **Interested parties:** 8
- **Interest direction:** both
- **Engagement → deal:** 2.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +298% · 6mo +380% · 12mo +324% · 2yr +190%

### 2seventy bio, Inc. (TSVT)
- **Acquirer:** Bristol-Myers Squibb Company
- **Announced / Closed:** 2025-03-10 / 2025-05-13
- **Deal size:** $266M  ·  $5.00/sh
- **Premium (vs unaffected):** 117%
- **Stage:** Commercial (Abecma)
- **Value-inflecting events:** —
- **Offer range (low→high):** $4.75 → $5.00
- **Interested parties:** 3
- **Interest direction:** both
- **Engagement → deal:** 25.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -51% · 6mo -45% · 12mo -62% · 2yr -77%

### Allakos Inc. (ALLK)
- **Acquirer:** Concentra Biosciences, LLC
- **Announced / Closed:** 2025-04-02 / 2025-05-15
- **Deal size:** $30M  ·  $0.33/sh
- **Premium (vs unaffected):** 18%
- **Stage:** Phase 1 failure, lead asset discontinued
- **Value-inflecting events:** AK006 Phase 1 failure; Discontinuation of AK006 development; Initiation of strategic review process; Concentra/Tang Capital 13D filing
- **Offer range (low→high):** $0.32 → $0.33
- **Interested parties:** 42
- **Interest direction:** outbound
- **Engagement → deal:** 1.3 months
- **Reported early (1mo+):** yes — Bloomberg News reported sale exploration in Dec 2019; more recently, Special Situation Investments speculated on a Concentra bid 2 months early in Feb 2025
- **Trailing return to unaffected:** 3mo -73% · 6mo -61% · 12mo -83% · 2yr -94%

### Regulus Therapeutics Inc. (RGLS)
- **Acquirer:** Novartis AG
- **Announced / Closed:** 2025-04-30 / 2025-06-25
- **Deal size:** $529M  ·  $7.00/sh  + CVR
- **Premium (vs unaffected):** 305%
- **Stage:** Phase 1b lead asset
- **Value-inflecting events:** Positive Phase 1b MAD data; Positive interim analysis of fourth cohort; Successful End-of-Phase 1 meeting with FDA
- **Offer range (low→high):** $2.50 → $7.00
- **Interested parties:** 5
- **Interest direction:** outbound
- **Engagement → deal:** 3.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +12% · 6mo +7% · 12mo -40% · 2yr +23%

### Kronos Bio, Inc. (KRON)
- **Acquirer:** Concentra Biosciences, LLC
- **Announced / Closed:** 2025-05-01 / 2025-06-20
- **Deal size:** $35M  ·  $0.57/sh
- **Premium (vs unaffected):** -30%
- **Stage:** Pre-clinical lead + discontinued Phase 1/2
- **Value-inflecting events:** Discontinuation of Phase 1/2 istisociclib trial; Initiation of strategic review process; Failure of Party D reverse merger due to PIPE financing
- **Offer range (low→high):** $0.57 → $0.57
- **Interested parties:** 25
- **Interest direction:** outbound
- **Engagement → deal:** 1.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -13% · 6mo -16% · 12mo -37% · 2yr -57%

### Inozyme Pharma, Inc. (INZY)
- **Acquirer:** BioMarin Pharmaceutical Inc.
- **Announced / Closed:** 2025-05-16 / 2025-07-01
- **Deal size:** $260M  ·  $4.00/sh
- **Premium (vs unaffected):** 335%
- **Stage:** Phase 3 lead asset
- **Value-inflecting events:** Positive interim clinical data for INZ-701 (May 2025)
- **Offer range (low→high):** $1.75 → $4.00
- **Interested parties:** 2
- **Interest direction:** both
- **Engagement → deal:** 12.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -32% · 6mo -82% · 12mo -82% · 2yr -86%

### Blueprint Medicines Corporation (BPMC)
- **Acquirer:** SANOFI
- **Announced / Closed:** 2025-06-02 / 2025-07-17
- **Deal size:** $8.4B  ·  $129.00/sh  + CVR
- **Premium (vs unaffected):** 23%
- **Stage:** Approved drug + Phase 2/3 lead
- **Value-inflecting events:** —
- **Offer range (low→high):** $124.00 → $129.00
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 12.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -7% · 6mo +15% · 12mo -2% · 2yr +79%

### Elevation Oncology, Inc. (ELEV)
- **Acquirer:** Concentra Biosciences, LLC
- **Announced / Closed:** 2025-06-09 / 2025-07-23
- **Deal size:** $21M  ·  $0.36/sh
- **Premium (vs unaffected):** 6%
- **Stage:** Preclinical/Early Clinical, lead asset discontinued
- **Value-inflecting events:** Discontinuation of lead program EO-3021; Initiation of strategic options evaluation; Activist pressure from BML Capital Management
- **Offer range (low→high):** $0.36 → $0.36
- **Interested parties:** 23
- **Interest direction:** outbound
- **Engagement → deal:** 1.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -46% · 6mo -48% · 12mo -90% · 2yr -77%

### CureVac N.V. (CVAC)
- **Acquirer:** BioNTech SE
- **Announced / Closed:** 2025-06-12 / —
- **Deal size:** $1.2B  ·  $5.46/sh  + CVR
- **Premium (vs unaffected):** 57%
- **Stage:** Clinical/Pre-clinical oncology and infectious disease
- **Value-inflecting events:** Patent litigation settlement; GSK restructuring of infectious disease programs; BioNTech exchange ratio increase; Fixed-value collar structure proposal
- **Offer range (low→high):** — → $1,250,000,000.00
- **Interested parties:** 1
- **Interest direction:** both
- **Engagement → deal:** 4.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -3% · 6mo +22% · 12mo +19% · 2yr -66%

### Verve Therapeutics, Inc. (VERV)
- **Acquirer:** Eli Lilly and Company
- **Announced / Closed:** 2025-06-17 / 2025-07-25
- **Deal size:** $938M  ·  $10.50/sh  + CVR
- **Premium (vs unaffected):** 127%
- **Stage:** Phase 1b lead asset
- **Value-inflecting events:** —
- **Offer range (low→high):** $10.00 → $10.50
- **Interested parties:** 8
- **Interest direction:** both
- **Engagement → deal:** 7.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -46% · 6mo -3% · 12mo -23% · 2yr -75%

### Turnstone Biologics Corp. (TSBX)
- **Acquirer:** XOMA Royalty Corporation
- **Announced / Closed:** 2025-06-27 / 2025-08-11
- **Deal size:** $8M  ·  $0.34/sh  + CVR
- **Premium (vs unaffected):** 3%
- **Stage:** Phase 1 (Discontinued), Pre-revenue
- **Value-inflecting events:** Phase 1 data for TIDAL-01; 60% workforce reduction; Discontinuation of TIDAL-01 clinical studies; Company D withdrawal from reverse merger
- **Offer range (low→high):** $0.34 → $0.34
- **Interested parties:** 43
- **Interest direction:** outbound
- **Engagement → deal:** 2.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -15% · 6mo -31% · 12mo -87% · 2yr -97%

### IGM Biosciences, Inc. (IGMS)
- **Acquirer:** Tang Capital Partners, LP
- **Announced / Closed:** 2025-07-01 / 2025-08-14
- **Deal size:** $75M  ·  $1.25/sh
- **Premium (vs unaffected):** -2%
- **Stage:** Pre-revenue, Phase 1b (discontinued lead)
- **Value-inflecting events:** Strategic pivot to autoimmune diseases; Imvotamab data failure and development termination; Strategic alternatives process initiation; 73% workforce reduction
- **Offer range (low→high):** $1.20 → $1.25
- **Interested parties:** 10
- **Interest direction:** outbound
- **Engagement → deal:** 1.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -7% · 6mo -87% · 12mo -85% · 2yr -87%

### CARGO Therapeutics, Inc. (CRGX)
- **Acquirer:** Tang Capital Partners, LP
- **Announced / Closed:** 2025-07-08 / 2025-08-19
- **Deal size:** $204M  ·  $4.38/sh  + CVR
- **Premium (vs unaffected):** -8%
- **Stage:** Phase 2 (Discontinued) + Preclinical
- **Value-inflecting events:** Discontinuation of FIRCE-1 Phase 2 study; Evaluation of strategic options and 90% workforce reduction
- **Offer range (low→high):** $4.38 → $4.55
- **Interested parties:** 157
- **Interest direction:** outbound
- **Engagement → deal:** 3.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +20% · 6mo -74% · 12mo -74% · 2yr —

### iTeos Therapeutics, Inc. (ITOS)
- **Acquirer:** Tang Capital Partners, LP
- **Announced / Closed:** 2025-07-21 / 2025-08-29
- **Deal size:** $444M  ·  $10.05/sh
- **Premium (vs unaffected):** 1%
- **Stage:** Phase 2 lead (terminated) + clinical assets
- **Value-inflecting events:** GSK termination of belrestotug program; Announcement of clinical/operational wind down
- **Offer range (low→high):** $8.50 → $10.05
- **Interested parties:** 20
- **Interest direction:** both
- **Engagement → deal:** 1.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +45% · 6mo +34% · 12mo -33% · 2yr -29%

### DURECT CORPORATION (DRRX)
- **Acquirer:** Bausch Health Companies Inc.
- **Announced / Closed:** 2025-07-29 / 2025-09-11
- **Deal size:** $54M  ·  $1.75/sh  + CVR
- **Premium (vs unaffected):** 178%
- **Stage:** Phase 3 ready lead asset
- **Value-inflecting events:** AHFIRM trial failed to meet primary endpoints; FDA Breakthrough Therapy designation for larsucosterol; Going concern warning and liquidity concerns
- **Offer range (low→high):** $1.75 → $1.75
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 18.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -21% · 6mo -34% · 12mo -51% · 2yr -81%

### HilleVax, Inc. (HLVX)
- **Acquirer:** XOMA Royalty Corporation
- **Announced / Closed:** 2025-08-04 / 2025-09-17
- **Deal size:** $98M  ·  $1.95/sh
- **Premium (vs unaffected):** -5%
- **Stage:** Phase 2b lead (discontinued) + clinical-stage pipeline
- **Value-inflecting events:** NEST-IN1 Phase 2b study failure (HIL-214); Strategic review and 40% workforce reduction; Termination of Takeda license agreement
- **Offer range (low→high):** $1.95 → $1.95
- **Interested parties:** 33
- **Interest direction:** outbound
- **Engagement → deal:** 5.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +45% · 6mo -1% · 12mo -85% · 2yr -86%

### LAVA Therapeutics N.V. (LVTX)
- **Acquirer:** XOMA Royalty Corporation
- **Announced / Closed:** 2025-08-04 / 2025-11-13
- **Deal size:** $27M  ·  $1.04/sh
- **Premium (vs unaffected):** -21%
- **Stage:** Clinical stage + partnered programs
- **Value-inflecting events:** Discontinuation of LAVA-1207; Initiation of strategic review process; Public announcement of strategic options evaluation; Wind-down of LAVA-1266
- **Offer range (low→high):** $1.04 → $1.16
- **Interested parties:** 100
- **Interest direction:** outbound
- **Engagement → deal:** 5.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +14% · 6mo +25% · 12mo -30% · 2yr -20%

### Y-mAbs Therapeutics, Inc. (YMAB)
- **Acquirer:** SERB Pharmaceuticals (Stark International Lux)
- **Announced / Closed:** 2025-08-05 / 2025-09-16
- **Deal size:** $391M  ·  $8.60/sh
- **Premium (vs unaffected):** 100%
- **Stage:** Marketed lead asset + Clinical platform
- **Value-inflecting events:** —
- **Offer range (low→high):** $7.80 → $8.60
- **Interested parties:** 30
- **Interest direction:** both
- **Engagement → deal:** 6.0 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -5% · 6mo -47% · 12mo -62% · 2yr -23%

### scPharmaceuticals Inc. (SCPH)
- **Acquirer:** MannKind Corporation
- **Announced / Closed:** 2025-08-25 / 2025-10-07
- **Deal size:** $288M  ·  $5.35/sh  + CVR
- **Premium (vs unaffected):** -4%
- **Stage:** Commercial (FUROSCIX) + Phase 3 (SCP-111)
- **Value-inflecting events:** FUROSCIX device supplier price increase; Renegotiation of West Pharmaceutical supply agreement; Need for near-term capital/financing
- **Offer range (low→high):** $4.50 → $5.35
- **Interested parties:** 26
- **Interest direction:** both
- **Engagement → deal:** 3.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +123% · 6mo +70% · 12mo +13% · 2yr -25%

### Tourmaline Bio, Inc. (TRML)
- **Acquirer:** Novartis AG
- **Announced / Closed:** 2025-09-09 / 2025-10-28
- **Deal size:** $1.2B  ·  $48.00/sh
- **Premium (vs unaffected):** 132%
- **Stage:** Phase 2 lead asset
- **Value-inflecting events:** Positive topline results from Phase 2 TRANQUILITY trial
- **Offer range (low→high):** $25.00 → $48.00
- **Interested parties:** 12
- **Interest direction:** both
- **Engagement → deal:** 1.6 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +37% · 6mo +45% · 12mo +48% · 2yr +653%

### 89bio, Inc. (ETNB)
- **Acquirer:** Roche Holdings, Inc.
- **Announced / Closed:** 2025-09-18 / 2025-10-30
- **Deal size:** $2.3B  ·  $14.50/sh  + CVR
- **Premium (vs unaffected):** 57%
- **Stage:** Phase 3 lead asset
- **Value-inflecting events:** Positive clinical data from competitor Akero Therapeutics; Phase 3 pegozafermin program progress
- **Offer range (low→high):** $13.00 → $14.50
- **Interested parties:** 1
- **Interest direction:** outbound
- **Engagement → deal:** 29.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +19% · 6mo -13% · 12mo +15% · 2yr -42%

### Merus N.V. (MRUS)
- **Acquirer:** Genmab A/S
- **Announced / Closed:** 2025-09-29 / 2025-12-29
- **Deal size:** $7.4B  ·  $97.00/sh
- **Premium (vs unaffected):** 47%
- **Stage:** Phase 2, clinical-stage oncology
- **Value-inflecting events:** Phase 2 petosemtamab data (May 2025)
- **Offer range (low→high):** $81.00 → $97.00
- **Interested parties:** 5
- **Interest direction:** both
- **Engagement → deal:** 1.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +17% · 6mo +40% · 12mo +29% · 2yr +201%

### Adverum Biotechnologies, Inc. (ADVM)
- **Acquirer:** Eli Lilly and Company
- **Announced / Closed:** 2025-10-24 / 2025-12-09
- **Deal size:** $79M  ·  $3.56/sh  + CVR
- **Premium (vs unaffected):** -21%
- **Stage:** Phase 3 lead, pre-revenue
- **Value-inflecting events:** —
- **Offer range (low→high):** $3.24 → $3.56
- **Interested parties:** 30
- **Interest direction:** outbound
- **Engagement → deal:** 24.5 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +94% · 6mo -12% · 12mo -40% · 2yr +375%

### Evoke Pharma, Inc. (EVOK)
- **Acquirer:** QOL Medical, LLC
- **Announced / Closed:** 2025-11-04 / 2025-12-17
- **Deal size:** $19M  ·  $11.00/sh
- **Premium (vs unaffected):** 141%
- **Stage:** FDA-approved / Commercial
- **Value-inflecting events:** —
- **Offer range (low→high):** $7.50 → $11.00
- **Interested parties:** 3
- **Interest direction:** outbound
- **Engagement → deal:** 6.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +68% · 6mo +103% · 12mo -13% · 2yr +266%

### Mersana Therapeutics, Inc. (MRSN)
- **Acquirer:** Day One Biopharmaceuticals, Inc.
- **Announced / Closed:** 2025-11-13 / 2026-01-06
- **Deal size:** $125M  ·  $25.00/sh  + CVR
- **Premium (vs unaffected):** 171%
- **Stage:** Phase 1 lead, pre-revenue
- **Value-inflecting events:** Positive initial clinical data for Emi-Le; FDA Fast Track designation; Nasdaq deficiency notice; Strategic restructuring and 55% workforce reduction
- **Offer range (low→high):** $12.00 → $25.00
- **Interested parties:** 33
- **Interest direction:** outbound
- **Engagement → deal:** 8.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +2618% · 6mo +2881% · 12mo +369% · 2yr +496%

### Cidara Therapeutics, Inc. (CDTX)
- **Acquirer:** Merck & Co., Inc.
- **Announced / Closed:** 2025-11-14 / 2026-01-07
- **Deal size:** $7.0B  ·  $221.50/sh
- **Premium (vs unaffected):** 118%
- **Stage:** Phase 3 lead, Pre-revenue
- **Value-inflecting events:** Positive topline Phase 2b NAVIGATE results; End-of-Phase 2 (EOP2) meeting with FDA; BARDA contract award up to $339 million; Phase 3 ANCHOR Trial initiation
- **Offer range (low→high):** $118.00 → $221.50
- **Interested parties:** 7
- **Interest direction:** both
- **Engagement → deal:** 12.1 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +69% · 6mo +458% · 12mo +857% · 2yr +12915%

### Applied Therapeutics, Inc. (APLT)
- **Acquirer:** Cycle Group Holdings Limited
- **Announced / Closed:** 2025-12-11 / 2026-02-03
- **Deal size:** $14M  ·  $0.09/sh  + CVR
- **Premium (vs unaffected):** -90%
- **Stage:** NDA / Phase 3 lead, pre-revenue
- **Value-inflecting events:** FDA issues Complete Response Letter for govorestat; CEO Shoshana Shendelman resigns; Workforce reduction and strategic alternative review; Liquidity crisis and risk of bankruptcy
- **Offer range (low→high):** $0.09 → $0.09
- **Interested parties:** 9
- **Interest direction:** both
- **Engagement → deal:** 10.4 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +98% · 6mo +112% · 12mo -92% · 2yr -71%

### Generation Bio Co. (GBIO)
- **Acquirer:** XOMA Royalty Corporation
- **Announced / Closed:** 2025-12-15 / 2026-02-09
- **Deal size:** $29M  ·  $4.29/sh  + CVR
- **Premium (vs unaffected):** -21%
- **Stage:** Preclinical lead + Moderna research collaboration
- **Value-inflecting events:** ctLNP system T cell data announcement; Evaluation of strategic alternatives announcement
- **Offer range (low→high):** $2.15 → $4.29
- **Interested parties:** 71
- **Interest direction:** outbound
- **Engagement → deal:** 1.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -14% · 6mo +1326% · 12mo +252% · 2yr +184%

### Dynavax Technologies Corporation (DVAX)
- **Acquirer:** Sanofi
- **Announced / Closed:** 2025-12-24 / 2026-02-10
- **Deal size:** $1.8B  ·  $15.50/sh
- **Premium (vs unaffected):** 39%
- **Stage:** Commercial + Phase 1/2 lead pipeline
- **Value-inflecting events:** Positive Phase 1/2 shingles vaccine data; Deep Track Capital proxy contest; Adoption of stockholder rights plan
- **Offer range (low→high):** $14.40 → $15.50
- **Interested parties:** 3
- **Interest direction:** both
- **Engagement → deal:** 12.4 months
- **Reported early (1mo+):** yes — PR Newswire/Reuters + 14 months early (poison pill/activist pressure)
- **Trailing return to unaffected:** 3mo +6% · 6mo +14% · 12mo -10% · 2yr -20%

### RAPT Therapeutics, Inc. (RAPT)
- **Acquirer:** GSK plc
- **Announced / Closed:** 2026-01-20 / 2026-03-03
- **Deal size:** $1.8B  ·  $58.00/sh
- **Premium (vs unaffected):** 72%
- **Stage:** Phase 2b lead asset, pre-revenue
- **Value-inflecting events:** Release of Phase 2 data for ozureprubart; Positive Phase 2 data in CSU
- **Offer range (low→high):** $50.00 → $58.00
- **Interested parties:** 10
- **Interest direction:** both
- **Engagement → deal:** 3.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +70% · 6mo +355% · 12mo +4023% · 2yr +34%

### Arcellx, Inc. (ACLX)
- **Acquirer:** Gilead Sciences, Inc.
- **Announced / Closed:** 2026-02-23 / 2026-04-28
- **Deal size:** $6.7B  ·  $115.00/sh  + CVR
- **Premium (vs unaffected):** 70%
- **Stage:** Phase 3 lead + clinical stage assets
- **Value-inflecting events:** Collaboration and License Agreement with Kite Pharma; Expansion of collaboration to include lymphomas; Potential launch of anito-cel in 2026
- **Offer range (low→high):** $98.00 → $115.00
- **Interested parties:** 2
- **Interest direction:** inbound
- **Engagement → deal:** 0.3 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -20% · 6mo -5% · 12mo +7% · 2yr +1%

### Day One Biopharmaceuticals, Inc. (DAWN)
- **Acquirer:** Servier S.A.S.
- **Announced / Closed:** 2026-03-06 / 2026-04-23
- **Deal size:** $2.2B  ·  $21.50/sh
- **Premium (vs unaffected):** 88%
- **Stage:** Commercial / Phase 3 lead
- **Value-inflecting events:** OJEMDA (tovorafenib) commercial launch; FIREFLY-2 Phase 3 trial; Emi-Le (XMT-1660) Phase 1 entry
- **Offer range (low→high):** $13.00 → $21.50
- **Interested parties:** 3
- **Interest direction:** inbound
- **Engagement → deal:** 1.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +17% · 6mo +72% · 12mo -8% · 2yr -27%

### Lisata Therapeutics, Inc. (LSTA)
- **Acquirer:** Kuva Labs Inc.
- **Announced / Closed:** 2026-03-06 / —
- **Deal size:** $36M  ·  $4.00/sh  + CVR
- **Premium (vs unaffected):** -12%
- **Stage:** Phase 2a lead asset
- **Value-inflecting events:** License and collaboration agreement with Kuva; Binding term sheet for acquisition; Execution of definitive merger agreement
- **Offer range (low→high):** $4.00 → $4.00
- **Interested parties:** 1
- **Interest direction:** inbound
- **Engagement → deal:** 15.2 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +120% · 6mo +82% · 12mo +82% · 2yr +43%

### Terns Pharmaceuticals, Inc. (TERN)
- **Acquirer:** Merck & Co., Inc.
- **Announced / Closed:** 2026-03-25 / 2026-05-05
- **Deal size:** $6.1B  ·  $53.00/sh
- **Premium (vs unaffected):** 35%
- **Stage:** Phase 1/2 lead asset
- **Value-inflecting events:** CARDINAL study abstract publication; Updated CARDINAL trial data at ASH Meeting; FDA Breakthrough Therapy Designation for TERN-701
- **Offer range (low→high):** $50.00 → $53.00
- **Interested parties:** 2
- **Interest direction:** both
- **Engagement → deal:** 1.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +49% · 6mo +466% · 12mo +881% · 2yr +498%

### Kezar Life Sciences, Inc. (KZR)
- **Acquirer:** Aurinia Pharmaceuticals Inc.
- **Announced / Closed:** 2026-03-30 / 2026-05-11
- **Deal size:** $51M  ·  $6.96/sh
- **Premium (vs unaffected):** 4%
- **Stage:** Phase 2 lead (discontinued) + Phase 1 oncology
- **Value-inflecting events:** PALIZADE trial enrollment cessation; Unsolicited bid from Concentra; Strategic review initiation; FDA registrational path failure in AIH
- **Offer range (low→high):** $1.10 → $6.96
- **Interested parties:** 77
- **Interest direction:** both
- **Engagement → deal:** 17.7 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +8% · 6mo +70% · 12mo +17% · 2yr +738%

### Apellis Pharmaceuticals, Inc. (APLS)
- **Acquirer:** Biogen Inc.
- **Announced / Closed:** 2026-03-31 / 2026-05-14
- **Deal size:** $5.2B  ·  $41.00/sh  + CVR
- **Premium (vs unaffected):** 96%
- **Stage:** 2 approved drugs (SYFOVRE and EMPAVELI)
- **Value-inflecting events:** FDA approval of Syfovre; Acquisition of rival Iveric Bio by Astellas; VALIANT study clinical data
- **Offer range (low→high):** $26.00 → $41.00
- **Interested parties:** 8
- **Interest direction:** both
- **Engagement → deal:** 18.3 months
- **Reported early (1mo+):** yes — Bloomberg reported takeover interest nearly 3 years early (April 2023)
- **Trailing return to unaffected:** 3mo -2% · 6mo -24% · 12mo -17% · 2yr -63%

### Soleno Therapeutics, Inc. (SLNO)
- **Acquirer:** Neurocrine Biosciences, Inc.
- **Announced / Closed:** 2026-04-06 / 2026-05-18
- **Deal size:** $2.7B  ·  $53.00/sh
- **Premium (vs unaffected):** 34%
- **Stage:** Commercial-stage, 1 approved drug
- **Value-inflecting events:** FDA approval of VYKAT XR (March 2025); U.S. commercial launch of VYKAT XR (April 2025); EMA validation of MAA for diazoxide choline (May 2025); EMA communication raising concerns about EU approval (February 2026)
- **Offer range (low→high):** $50.00 → $53.00
- **Interested parties:** 11
- **Interest direction:** both
- **Engagement → deal:** 1.8 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo -23% · 6mo -43% · 12mo -11% · 2yr +5%

### KalVista Pharmaceuticals, Inc. (KALV)
- **Acquirer:** Chiesi Farmaceutici S.p.A.
- **Announced / Closed:** 2026-04-29 / 2026-06-11
- **Deal size:** $1.4B  ·  $27.00/sh
- **Premium (vs unaffected):** 40%
- **Stage:** Approved / Commercial
- **Value-inflecting events:** Positive Phase 3 KONFIDENT data; FDA approval of EKTERLY (sebetralstat)
- **Offer range (low→high):** $21.00 → $27.00
- **Interested parties:** 4
- **Interest direction:** both
- **Engagement → deal:** 3.5 months
- **Reported early (1mo+):** yes — Bloomberg +15 months early; Betaville +19 months early
- **Trailing return to unaffected:** 3mo +27% · 6mo +56% · 12mo +62% · 2yr +59%

### Assertio Holdings, Inc. (ASRT)
- **Acquirer:** Zydus Worldwide DMCC
- **Announced / Closed:** 2026-05-13 / 2026-06-16
- **Deal size:** $152M  ·  $23.50/sh
- **Premium (vs unaffected):** 30%
- **Stage:** Commercial (Rolvedon) + Divested mature assets
- **Value-inflecting events:** —
- **Offer range (low→high):** $13.50 → $23.50
- **Interested parties:** 30
- **Interest direction:** outbound
- **Engagement → deal:** 0.9 months
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo +96% · 6mo +2071% · 12mo +2806% · 2yr +1584%

### Pfizer Acquisition of King Pharmaceuticals, Inc. (—)
- **Acquirer:** —
- **Announced / Closed:** — / —
- **Deal size:** —
- **Premium (vs unaffected):** —
- **Stage:** Commercial stage with specialty portfolio and EpiPen franchise
- **Value-inflecting events:** —
- **Offer range (low→high):** $12.00 → $14.25
- **Interested parties:** 5
- **Interest direction:** inbound
- **Engagement → deal:** —
- **Reported early (1mo+):** no
- **Trailing return to unaffected:** 3mo — · 6mo — · 12mo — · 2yr —
