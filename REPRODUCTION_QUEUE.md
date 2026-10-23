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

## In flight 2026-10-23 (current state; the sections below are historical)

283 papers final (256 partially reproduced, 27 blocked), 44 unprocessed, last publication QC-284
(commit ad7eb2ec). Fifteen Sonnet builders are running, one per paper, in the session scratchpad
(`build_<QC-ID>` / `run_<QC-ID>`): QC-281, QC-287, QC-288, QC-292, QC-293, QC-295, QC-296,
QC-299, QC-301, QC-302, QC-303, QC-304, QC-306, QC-307, QC-308. Next unprocessed after these:
QC-310, QC-311, QC-312, QC-313, QC-314, QC-315, QC-318, QC-319, QC-321, ... (QC-ID order; all
coverage goals met). Since 2026-10-22 a published notebook must be the untouched output of one
`tools/execute_notebook.py` run (code cells identical to the executed copy kept in the build
folder; markdown-only edits allowed), checked by the dispatcher before publishing. Throttle:
at most 15 builders; pause the newest when C: has under 2 GB free (the Windows page file grows
to ~46 GB under load and shrinks only as agents finish). After the queue: user-supplied gated
datasets for the atlas, then a new task the user will describe.


## PAUSED 2026-10-20 (user decision; resume from here)

Pipeline paused on 2026-10-20 after the QC-064 publication (commit 510de620). 104 papers final
(96 partially reproduced, 8 blocked), 223 unprocessed. All nine builder agents were terminated by
an API/network error at the moment of the pause; none had reported. No notebook execution is
running. The 100-paper milestone was reached with QC-066.

In-flight papers at the pause, with what exists on disk. Draft notebooks in the repo are
UNTRACKED and UNVERIFIED (do not publish without re-verification). Scratch folders are
`<scratch>\build_<QC-ID>` and `<scratch>\run_<QC-ID>` under the session scratchpad.

| QC-ID | Folder | Draft notebook in repo | Scratch state |
|---|---|---|---|
| QC-067 | 29 | NQEDR_AdversarialRobustness_Li2026.ipynb | builder + data, no executed copy |
| QC-068 | 03 | QNN_KnowledgeDistillationDDoS_Krishnamurthy2026.ipynb | fast_exec.ipynb and full_exec.ipynb in build folder (agent said "passed in 10.7 min") |
| QC-069 | 01 | VQRL_IntrusionDetection_Kerkatou2026.ipynb | builder + data, no executed copy |
| QC-071 | 01 | VQC_IntrusionDetection_Thomos2026.ipynb | builder + data, no executed copy |
| QC-072 | 23 | QNN_EquivariantAdversarialTransfer_Krumtunger2026.ipynb | FAST_executed.ipynb in build folder |
| QC-073 | 01 | FedVQC_IoTAnomalyDetection_Delhibabu2026.ipynb | FAST_executed.ipynb in build folder |
| QC-074 | 27 | none | builder + repo clone only |
| QC-075 | 25 | none | nb_fast.ipynb in build folder |
| QC-076 | 01 | none | builder + repo clone only |

Resume procedure: for each row, re-dispatch a Sonnet agent with the standard brief and tell it to
reuse its `build_<QC-ID>` / `run_<QC-ID>` folders and the existing draft, re-execute (FAST then
full), run `tools/verify_notebook.py` and report; then publish with `tools/publish_notebook.py`.
Then continue in QC-ID order from `tools/next_papers.py --n 3 --index paper_index.csv`.
Full runs still pending after FAST publication (retrospective audit): QC-023, QC-031, QC-036,
QC-037, QC-043, QC-044, QC-045, QC-049, QC-054, QC-055, QC-061, QC-064, QC-164, QC-183.
Machine notes: C: has about 8 GB free (agent caches under the scratchpad); py7zr and python-pptx
were added to the venv on 2026-10-20.
## Final statuses: 104 papers (see REPRODUCTION_LOG.md; `tools/next_papers.py --status`)

96 partially reproduced, 8 blocked (QC-005, QC-019, QC-027, QC-029, QC-046, QC-048, QC-052, QC-060). 223 unprocessed; queue runs in QC-ID order (coverage goal met).
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
