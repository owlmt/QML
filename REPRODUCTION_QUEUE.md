# Reproduction queue

State file for resuming the factory after an interruption. `manifest.csv` (column
`Reproduction status`) is the persistent queue: every row with an empty status is unprocessed and
papers are taken in QC-ID order (`tools/next_papers.py --status`). `REPRODUCTION_LOG.md` holds the
published record. This file lists what is in flight so a resumed session can check for half-built
notebooks before re-dispatching.

## Policy

- One agent per paper, briefed with `tools/AGENT_BRIEF.md`; about three agents at a time.
- Every paper ends with exactly one status: reproduced, partially reproduced, implemented but
  unvalidated, or blocked (reason in the manifest Notes).
- The dispatcher re-verifies each notebook (no error outputs, all code cells executed, figures,
  size) and publishes with `tools/publish_notebook.py`; blocked papers are recorded with
  `--no-notebook`.

## In progress

| QC-ID | Paper | Notebook (planned path) | Started |
|---|---|---|---|
| QC-216 | de Abreu 2025, QuantumNetSec (completing the existing root notebook) | 01_Network_Intrusion_Detection/VQC_IntrusionDetection_deAbreu2025.ipynb | 2026-10-17 |
| QC-034 | Kucukkara 2024, QNN platform-independent DDoS classification | 01_Network_Intrusion_Detection/QNN_DDoS_Kucukkara2024.ipynb | 2026-10-17 |
| QC-001 | Akter 2024, Quantum FGSM adversarial attacks | 05_Malware_Detection/... | 2026-10-17 |
| QC-002 | Tehrani 2024, quantum-enhanced SIEM with Hoeffding trees (botnet) | 04_Botnet_DGA_Detection/... | 2026-10-17 |

## Published

| QC-ID | Notebook | Status | Commit |
|---|---|---|---|
| QC-033 | 03_DDoS_DoS_Detection/QSVM_DDoS_Said2023.ipynb | partially reproduced | 721b84d |
| QC-182 | 08_Phishing_Detection/VQC_PhishingURL_Shahriyar2025.ipynb | partially reproduced | e2972aa |
| QC-087 | 01_Network_Intrusion_Detection/QSVM_IntrusionDetection_Tiwari2026.ipynb | partially reproduced | 41fa446 |

## Notes

- `paper_index.csv` (repo root) is the feasibility index built by `tools/paper_index.py`
  (datasets, frameworks, models, metric snippets per paper); 45 PDFs yield almost no text.
- Out-of-order picks so far (QC-182, QC-087, QC-216, QC-034) were chosen for public data and
  clear methods; from here the queue runs in QC-ID order.
