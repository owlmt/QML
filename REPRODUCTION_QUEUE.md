# Reproduction queue

State file for resuming the factory after an interruption. `manifest.csv` (column
`Reproduction status`) is the persistent queue: every row with an empty status is unprocessed and
papers are taken in QC-ID order (`tools/next_papers.py --status`). `REPRODUCTION_LOG.md` holds the
published record. This file lists what is in flight so a resumed session can check for half-built
notebooks before re-dispatching.

## Policy

- One agent per paper, briefed with `tools/AGENT_BRIEF.md`; about four agents at a time.
- Every paper ends with exactly one status: reproduced, partially reproduced, implemented but
  unvalidated, or blocked (reason in the manifest Notes).
- The dispatcher re-verifies each notebook with `tools/verify_notebook.py` and publishes with
  `tools/publish_notebook.py`; blocked papers are recorded with `--no-notebook`.

## In progress

| QC-ID | Paper | Notebook (planned folder) | Started |
|---|---|---|---|
| QC-002 | Tehrani 2024, quantum-enhanced SIEM with Hoeffding trees (botnet) | 04_Botnet_DGA_Detection/QHTC_BotnetDGA_Tehrani2024.ipynb (draft on disk) | 2026-10-17 |
| QC-006 | Rivas 2024, quanvolutional autoencoder vs DDoS | 03_DDoS_DoS_Detection | 2026-10-18 |
| QC-007 | Bangroo 2023, Zerosdetect quantum zero-shot phishing URLs | 08_Phishing_Detection | 2026-10-18 |
| QC-008 | Maouaki 2024, quantum clustering for cybersecurity | 11_Vulnerability_Software_Supply_Chain_Attacks | 2026-10-18 |

## Final statuses so far (see REPRODUCTION_LOG.md for details)

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

## Notes

- `paper_index.csv` (repo root) is the feasibility index built by `tools/paper_index.py`
  (datasets, frameworks, models, metric snippets per paper); 45 PDFs yield almost no text.
- Out-of-order picks (QC-182, QC-087, QC-216, QC-034) were chosen for public data and clear
  methods; the queue otherwise runs in QC-ID order.
- Known interruption cause: the session usage cap terminates agents mid-run; their detached
  notebook executions keep going. On resume, message each agent to check its run log.
