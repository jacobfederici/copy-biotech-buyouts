# Buyout Reports

This folder stores one Markdown extraction document per SC 14D9 target packet.

Use the instruction in `buyouts/AGENT_INSTRUCTIONS.md`.

Keep only current accepted outputs here. When a report fails QC and the queue row is reset to `todo`, delete the stale Markdown file and rebuild the next version from SEC filings and deterministic API pulls.

File naming convention:

```text
{cik}_{safe_company_name}.md
```

Each file should summarize the target, buyer, acquisition status, deal terms, timeline, interaction history, pipeline classification, offer economics, rationale, source accessions, and evidence.

Use a factual reporter tone. State what happened, who acted, when, and what the filings say. Do not add judgment on each step unless the filing itself contains that characterization, and attribute rationales or concerns to the filing or disclosed actor. Keep enough detail to preserve the important dynamics of each interaction, including requests, responses, changed terms, diligence, conflicts, board process, and next steps.

The interaction history should explain the people and counterparties involved when filings disclose them: target management, directors, committees, buyer representatives, other bidders, bankers, counsel, regulators, meetings, calls, proposals, counterproposals, diligence, conflicts, recusals, board deliberations, and completion communications.

The pipeline section should classify each material drug, platform, or program by modality/type, target or mechanism, disease/indication, stage, rights/partner, and deal relevance. The offer economics section should show per-share consideration, CVR terms when present, deal-reference shares outstanding source/date, implied upfront equity value or market cap, and maximum value including CVRs when applicable. The stock-price table should compute market cap for each weekly price row from the latest SEC-sourced shares outstanding available on or before that week, with the share count and share source date shown in the row.

After a packet is finished, mark the matching row in `buyouts/queue.csv`:

- `status=done`, `status=rejected`, or `status=blocked`
- `done_date=YYYY-MM-DD`
- `done_notes=completed; report=buyouts/reports/<file>.md`
- `report_path=buyouts/reports/<file>.md`
