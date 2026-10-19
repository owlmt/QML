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

## In progress (2026-10-19, after QC-025)

| QC-ID | Paper | Target folder | State |
|---|---|---|---|
| QC-020 | Kadi 2025, encoding comparison hybrid QNN | 01_Network_Intrusion_Detection | notebook drafted (HybridQNN_EncodingComparison_Kadi2025.ipynb), executing |
| QC-030 | QML security assessment in the IoT | 03_DDoS_DoS_Detection | agent running (HybridQNN_IoMTSecurity_Rajawat2023.ipynb drafted) |
| QC-036 | QNN cyber threat detection, VMI | 18_Cloud_Virtual_Environment_Threats | agent running (HybridQNN_VMIThreatDetection_Tripathi2023.ipynb drafted) |
| QC-037 | Accuracy and robustness in QML | 23_Adversarial_Attacks_Against_QML | agent running |
| QC-039 | Hybrid quantum framework, ultra-secure communication | 01_Network_Intrusion_Detection | agent running |
| QC-040 | Hybrid QNN for CV-QKD hacking detection | 21_QKD_Attack_Detection | agent running |
| QC-041 | Lightweight hybrid QNN binary IDS | 01_Network_Intrusion_Detection | agent running |
| QC-042 | Metaheuristic-enhanced quantum-classical NN | 14_IoT_IIoT_Attack_Detection | agent running |
| QC-002 | Tehrani 2024 QHTC (revision with authors' azure code and corrected QHTC repo) | 04_Botnet_DGA_Detection | revision agent running, republish on same path |

Full runs still pending after FAST publication: QC-023, QC-031, QC-164, QC-183 (retrospective audit).

## Final statuses: 73 papers (see REPRODUCTION_LOG.md; `tools/next_papers.py --status`)

69 partially reproduced, 4 blocked (QC-005, QC-019, QC-027, QC-029). 254 unprocessed; queue runs in QC-ID order (coverage goal met).
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
