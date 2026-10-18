# Reproduction queue

State file for resuming the factory after an interruption. `manifest.csv` (column
`Reproduction status`) is the persistent queue: every row with an empty status is unprocessed.
`REPRODUCTION_LOG.md` holds the published record. This file lists what is in flight so a resumed
session can check for half-built notebooks before re-dispatching.

## Policy

- One agent per paper, briefed with `tools/AGENT_BRIEF.md`; four to six agents at a time, on
  the `sonnet` model (`haiku` for feasibility-only checks); the dispatcher only verifies
  (`tools/verify_notebook.py`, `tools/notebook_summary.py`), publishes and dispatches.
- Order (user decision 2026-10-18): coverage first. Every topic folder gets at least two
  implemented notebooks (one where the folder has a single paper) before the remaining papers are
  filled in QC-ID order. Pick with `tools/next_papers.py --coverage 2 --index paper_index.csv`,
  topics with 0 notebooks first. Multi-topic papers may be filed in a later, uncovered folder
  (coverage exception in CLAUDE.md).
- Every paper ends with exactly one status: reproduced, partially reproduced, implemented but
  unvalidated, or blocked (reason in the manifest Notes, recorded with `--no-notebook`).
- Resume after an interruption: check each in-flight paper's notebook file and
  `<scratch>\build_<QC-ID>\*.log`; if a full run finished (`RESULT : all code cells executed
  without error`), verify and publish directly from the notebook outputs; otherwise re-dispatch
  the paper telling the new agent to reuse `<scratch>\build_<QC-ID>` and `run_<QC-ID>`.

## In progress

| QC-ID | Paper | Target folder | Started |
|---|---|---|---|
| QC-108 | QCBM zero-day intrusion detection (2026) | 02_Zero_Day_Attack_Detection | 2026-10-18 |
| QC-092 | Noise-aware hybrid QSVM Android malware (2026) | 06_Android_Malware_Detection | 2026-10-18 |
| QC-035 | Ransomware detection with QNNs (2024) | 07_Ransomware_Detection | 2026-10-18 |
| QC-199 | Eze 2025, QSVM/QCNN malicious URL detection | 09_Malicious_URL_Detection | 2026-10-18 |
| QC-032 | Quant-Jack cryptojacking in IIoT (2024) | 12_Cryptojacking_Detection | 2026-10-18 |
| QC-070 | Encrypted traffic analysis with QML (2026) | 13_Encrypted_Malicious_Traffic_Detection | 2026-10-18 |

## Final statuses so far (details in REPRODUCTION_LOG.md)

| QC-ID | Notebook | Status | Commit |
|---|---|---|---|
| QC-033 | 03_DDoS_DoS_Detection/QSVM_DDoS_Said2023.ipynb | partially reproduced | 721b84d |
| QC-182 | 08_Phishing_Detection/VQC_PhishingURL_Shahriyar2025.ipynb | partially reproduced | e2972aa |
| QC-087 | 01_Network_Intrusion_Detection/QSVM_IntrusionDetection_Tiwari2026.ipynb | partially reproduced | 41fa446 |
| QC-034 | 01_Network_Intrusion_Detection/QNN_DDoS_Kucukkara2024.ipynb | partially reproduced | 1aa2479 |
| QC-216 | 01_Network_Intrusion_Detection/VQC_IntrusionDetection_deAbreu2025.ipynb | partially reproduced | 1e8722c |
| QC-001 | 05_Malware_Detection/HybridQNN_QFGSM_Akter2024.ipynb | partially reproduced | 7965b59 |
| QC-003 | 01_Network_Intrusion_Detection/QAE_AnomalyDetection_Hdaib2024.ipynb | partially reproduced | b10b3be |
| QC-004 | 19_Cybersecurity_Anomaly_Detection/QRBM_AnomalyDetection_Moro2023.ipynb | partially reproduced | d751092 |
| QC-005 | (none) | blocked: perspective paper, no experiment | 2c43aa8 |
| QC-002 | 04_Botnet_DGA_Detection/QHTC_BotnetDGA_Tehrani2024.ipynb | partially reproduced | 2e0b2cd |
| QC-008 | 11_Vulnerability_Software_Supply_Chain_Attacks/QKMeans_CISAVulnerabilities_ElMaouaki2024.ipynb | partially reproduced | 4147bdf |
| QC-007 | 08_Phishing_Detection/QNN_PhishingURL_Bangroo2023.ipynb | partially reproduced | 802e3d3 |
| QC-009 | 05_Malware_Detection/QNN_SupplyChainClaMP_Akter2022.ipynb | partially reproduced | dc5ac3a |
| QC-006 | 03_DDoS_DoS_Detection/QAE_DDoSHivePlots_Rivas2024.ipynb | partially reproduced | 8f9af86 |

## Coverage (implemented notebooks per folder)

01: 4 | 03: 2 | 05: 2 | 08: 2 | 04, 11, 19: 1 | all other folders: 0 (agents above target 02, 06,
07, 09, 12, 13). Next empty folders to dispatch: 10 (QC-151, coverage exception), 14 (QC-105 or
QC-171), 15 (QC-119), 16 (QC-238), 17 (QC-328), 18 (QC-194), 20 (QC-259), 21 (QC-220), 22
(QC-219), 23 (QC-234), 24 (QC-014), 25 (QC-300), 26 (QC-150), 27 (QC-197), 28 (QC-121), 29
(QC-117), 30 (QC-077).

## Notes

- `paper_index.csv` (repo root) is the feasibility index built by `tools/paper_index.py`;
  45 PDFs yield almost no text.
- The session usage cap terminates agents mid-run; their detached notebook executions keep going.
