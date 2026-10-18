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
- Resume after an interruption: for each in-flight paper check the notebook file and
  `<scratch>\build_<QC-ID>\*.log`; if a full run finished (`RESULT : all code cells executed
  without error`), verify and publish straight from the notebook outputs
  (`tools/notebook_summary.py`); otherwise re-dispatch, telling the new agent to reuse
  `<scratch>\build_<QC-ID>` and `run_<QC-ID>`.

## In progress (2026-10-18)

| QC-ID | Paper | Target folder |
|---|---|---|
| QC-119 | QUPID partitioned QNN smart grid (2026) | 15_Smart_Grid_Power_System_Attacks |
| QC-238 | Quantum hybrid SVM for cyber-physical anomaly detection (2024) | 16_ICS_SCADA_Cyber_Physical_Attacks |
| QC-328 | Hybrid QNN in-vehicle cyberattack detection (2021) | 17_Vehicle_CAN_Bus_Attacks |
| QC-194 | Quantum autoencoders for anomaly detection (2025) | 18_Cloud_Virtual_Environment_Threats |
| QC-259 | Quantum DNN Ethereum attack vectors (2024) | 20_Blockchain_Attack_Detection |
| QC-220 | Resisting QKD attacks with QML (2025) | 21_QKD_Attack_Detection |

## Final statuses: 22 papers (see REPRODUCTION_LOG.md and `tools/next_papers.py --status`)

21 partially reproduced (QC-001, 002, 003, 004, 006, 007, 008, 009, 032, 033, 034, 035, 070,
087, 092, 108, 151, 171, 182, 199, 216) and 1 blocked (QC-005).

## Coverage (implemented notebooks per folder)

01: 4 | 03, 05, 08: 2 | 02, 04, 06, 07, 09, 10, 11, 12, 13, 14, 19: 1 | 15-18, 20-30: 0 (agents
above target 15, 16, 17, 18, 20, 21). Next empty folders: 22 (QC-219 audio deepfake QSVM),
23 (QC-234), 24 (QC-014), 25 (QC-300), 26 (QC-150), 27 (QC-197), 28 (QC-121), 29 (QC-117),
30 (QC-077). Then second notebooks for folders with 1.

## Notes

- `paper_index.csv` (repo root) is the feasibility index built by `tools/paper_index.py`;
  45 PDFs yield almost no text.
- The session usage cap terminates agents mid-run; their detached notebook executions keep going.
