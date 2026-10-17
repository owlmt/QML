# Reproduction queue

State file for resuming the factory after an interruption. `manifest.csv` (columns
`Notebook path`, `Reproduction status`, ...) and `REPRODUCTION_LOG.md` hold the published record;
this file holds what is in flight and what comes next. Update it whenever a paper starts or finishes.

## In progress (notebook being written / validated, not yet published)

| QC-ID | Paper | Notebook (planned path) | Owner | Started |
|---|---|---|---|---|
| QC-033 | Said 2023, QSVM DDoS smart micro-grid | 03_DDoS_DoS_Detection/QSVM_DDoS_Said2023.ipynb | main session | 2026-10-17 |
| QC-182 | Shahriyar 2025, PhishVQC | 08_Phishing_Detection/VQC_PhishingURL_Shahriyar2025.ipynb | agent | 2026-10-17 |
| QC-216 | de Abreu 2025, QuantumNetSec (completing the existing root notebook) | 01_Network_Intrusion_Detection/VQC_IntrusionDetection_deAbreu2025.ipynb | agent | 2026-10-17 |

## Next batch (public dataset + Qiskit/PennyLane method, no survey)

| QC-ID | Paper | Why feasible |
|---|---|---|
| QC-034 | 2024, Quantum-Neural Network model for platform independent DDoS classification | Qiskit QNN/QSVM on CICDDoS2019 / NSL-KDD |
| QC-087 | 2026, Leveraging quantum kernel methods for enhanced intrusion detection | PennyLane quantum kernels on NSL-KDD / UNSW-NB15, 4-16 qubits |
| QC-041 | 2026, Lightweight hybrid QNN for binary intrusion detection | PennyLane hybrid QNN on NSL-KDD / UNSW-NB15 / CIC-IDS2017 |
| QC-076 | 2026, How quantum is the advantage? Benchmark of QML for NIDS | public code github.com/Orqly-AI/quantum-ids, 4-8 qubits |
| QC-285 | 2023, Can feature engineering help QML for malware detection? | Drebin-215 (public), Qiskit VQC/QSVM, XGBoost feature selection |
| QC-018 | 2024, QML-IDS (conference version of QC-216) | share code with the QC-216 notebook; separate notebook on UNSW-NB15 |
| QC-199 | 2025, Eze et al., QSVM/QCNN vs SVM/CNN for malicious URLs | Qiskit; needs the Mendeley "Malicious and Benign Webpages" dataset (1.2 M rows) |
| QC-053 | 2026, Hridi et al., batch-wise QSVM vs SVM for email phishing | Qiskit ZZFeatureMap, 6 qubits; needs CEAS_08 + webpage dataset (Kaggle) |

## Selection notes

- Feasibility index (datasets, frameworks, models, metric snippets per paper) is rebuilt with
  `tools/paper_index.py --cache <scratch>/paper_text --out <scratch>/paper_index.csv`
  (45 PDFs yield almost no text and need OCR or manual reading).
- Dataset frequency across the corpus: MNIST 112, KDD99 44, UNSW-NB15 43, NSL-KDD 43,
  CIC-IDS2017 36, CICDDoS2019 18, TON_IoT 15, CICIoT2023 14, Bot-IoT 14, IoT-23 14.
- Frameworks: PennyLane 138 papers, Qiskit 137, TensorFlow Quantum 28, D-Wave 33.
- Surveys/reviews (incl. the 12 PDFs in `_Topic_assignment_unresolved`) are not reproduction targets.
