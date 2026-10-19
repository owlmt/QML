# Reproduction queue

State file for resuming the factory after an interruption. `manifest.csv` (column
`Reproduction status`) is the persistent queue: every row with an empty status is unprocessed.
`REPRODUCTION_LOG.md` holds the published record (one line per paper, with metrics and notes).
This file lists what is in flight so a resumed session can check for half-built notebooks.

## Policy

- One agent per paper, briefed with `tools/AGENT_BRIEF.md`; four to six agents at a time, on
  the `sonnet` model (`haiku` for feasibility-only checks); the dispatcher only verifies
  (`tools/verify_notebook.py`, `tools/notebook_summary.py`), publishes and dispatches.
- Order (user decision 2026-10-18): coverage first. Every topic folder gets at least two
  implemented notebooks (one where the folder has a single paper) before the remaining papers are
  filled in QC-ID order. Pick with `tools/next_papers.py --coverage 2 --index paper_index.csv`,
  topics with 0 notebooks first. Multi-topic papers may be filed in a later, uncovered folder
  (coverage exception in CLAUDE.md); the dispatcher names the target folder in the brief and
  moves/patches the badge if an agent files elsewhere.
- Every paper ends with exactly one status: reproduced, partially reproduced, implemented but
  unvalidated, or blocked (reason in the manifest Notes, recorded with `--no-notebook`).
- Since 2026-10-19 every notebook must contain the executed sections "Dataset Exploration and
  Visualisation" and "Quantum Circuit Architecture" (CLAUDE.md "Mandatory sections");
  `tools/verify_notebook.py` reports their status and the publisher records the five QA
  columns. Notebooks published before that date carry PENDING and are corrected in the
  retrospective audit that runs after the 327-paper queue is complete (add the missing sections,
  execute them, keep results, sync duplicate copies, update manifest/log, commit and push).
- Resume after an interruption: for each in-flight paper check the notebook file and
  `<scratch>\build_<QC-ID>\*.log` or `run_<QC-ID>\*.log`; if a full run finished (`RESULT : all
  code cells executed without error`), verify and publish straight from the notebook outputs
  (`tools/notebook_summary.py`); otherwise message the agent to resume (SendMessage) or re-dispatch
  telling the new agent to reuse the scratch folders.

## In progress (2026-10-19)

| QC-ID | Paper | Target folder | State |
|---|---|---|---|
| QC-121 | SecQML security aspects (2026) | 28_QML_Hardware_Side_Channel_Crosstalk_Attacks | FAST passed, full run to relaunch |
| QC-150 | CopyQNN extraction under noise (2025) | 26_QML_Model_Extraction_Theft | notebook drafted, experiments logged |
| QC-024 | Hybrid quantum-classical DL botnet DGA (2022) | 04_Botnet_DGA_Detection (2nd) | FAST passed, full run to relaunch |
| QC-316 | Quantum computing in mobile malware detection (2022) | 06_Android_Malware_Detection (2nd) | FAST passed, full run pending |
| QC-021 | Quantum exploration in ransomware detection (2024) | 07_Ransomware_Detection (2nd) | started |
| QC-026 | Reyes-Dorta 2024, malicious URL VQC | 09_Malicious_URL_Detection (2nd) | started |

## Final statuses: 36 papers (see REPRODUCTION_LOG.md; `tools/next_papers.py --status`)

35 partially reproduced, 1 blocked (QC-005).

## Coverage (implemented notebooks per folder)

01: 4 | 02, 03, 05, 08: 2 | 04, 06, 07, 09-25, 27, 29, 30: 1 | 26, 28: 0 (agents resumed) |
19: 1 (its only paper). Second-notebook picks after the current batch: 10 (none left: single
paper), 11 (QC-143/QC-168), 12 (none: single paper), 13 (QC-198), 14 (QC-105), 15 (QC-183),
16 (QC-202), 17 (QC-320), 18 (QC-012), 20 (none: single paper), 21 (QC-093), 22 (QC-235),
23 (QC-305), 24 (QC-015), 25 (QC-213), 26 (QC-164), 27 (QC-214), 28 (QC-099), 29 (QC-095),
30 (QC-078). Then fill in QC-ID order from QC-010.

## Notes

- `paper_index.csv` (repo root) is the feasibility index built by `tools/paper_index.py`;
  45 PDFs yield almost no text.
- The session usage cap terminates agents mid-run; their detached notebook executions keep going.
