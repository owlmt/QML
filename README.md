# QML × Cybersecurity Colab Reproduction Factory

This repository reproduces published **quantum machine learning (QML) papers in cybersecurity**
as teaching notebooks: one Google Colab notebook per paper, filed into 30 cybersecurity topic
folders. Every notebook downloads its own public data, rebuilds the paper's method step by step
with plain-language explanations, trains a classical baseline on the same inputs, compares its
own numbers with the paper's claim by claim, and ends with a critical reading and exercises.

The paper list (327 papers, `manifest.csv`) comes from the bibliography in
`original_bibliography.md`. Reproductions are produced by an automated pipeline (see
`CLAUDE.md`), executed end to end on a CPU before publication, and recorded with a truthful
status:

| Status | Meaning |
|---|---|
| reproduced | executes end to end and every checkable claim is within tolerance |
| partially reproduced | executes end to end; some claims not reached, exceeded or uncheckable |
| implemented but unvalidated | complete Colab-ready notebook that could not be executed locally |
| blocked | no notebook: survey/review, no public data, hardware-only, or unreadable PDF |

Each notebook also carries a **Dataset Exploration and Visualisation** section (real
observations coloured by ground-truth label) and a **Quantum Circuit Architecture** section
(the circuit actually executed). Notebooks published before 2026-10-19 receive these sections in
a retrospective audit; the manifest's QA columns say which have been done.

## How to run a notebook

Open the Colab link, keep the free CPU runtime, and choose **Runtime → Run all**. Every
notebook has a `FAST_MODE` switch in its configuration cell: `True` gives a class demo in
about 10 minutes, `False` runs the paper-scale experiment (runtime stated in the notebook).
Gated Hugging Face datasets expect your own token in Colab **Settings → Secrets** as
`HF_TOKEN`; nothing in this repository contains credentials.

To run locally: Python 3.12, then `pip install -r` the pins printed in each notebook's install
cell (Qiskit 2.5, qiskit-machine-learning 0.9, PennyLane 0.45, scikit-learn, pandas,
matplotlib). The pipeline's own tools are in `tools/` (`execute_notebook.py`,
`verify_notebook.py`, `publish_notebook.py`, `next_papers.py`).

## Repository layout

```
manifest.csv                 one row per paper: title, DOI, topic folder(s), notebook path,
                             reproduction status, paper vs notebook metrics, notes, QA columns
REPRODUCTION_LOG.md          one line per published notebook, newest last
REPRODUCTION_QUEUE.md        what is in flight and the dispatch policy
paper_index.csv              feasibility index (datasets, frameworks, models) per paper
CLAUDE.md                    conventions, validation requirements, publication workflow
tools/                       execution, verification, publication and queue scripts
01_... to 30_...             topic folders; each holds the notebooks of its papers
```

Paper PDFs are not distributed. Two early reference notebooks remain at the repository root
(`QSVM_DDoS_Said2023.ipynb`, `QuantumNetSec_VQC_DDoS_CICIDS2017.ipynb`); their reproductions
live in the topic folders.

## Progress (2026-10-21)
109 of 327 papers have a final status: 101 partially reproduced, 8 blocked; 218 still to process. 101 notebooks are published across 30 of the 30 topic folders.

## Notebooks by topic

### 01 Network Intrusion Detection  (16 of 79 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-003 | [Quantum deep learning-based anomaly detection for enhanced network security](https://doi.org/10.1007/s42484-024-00163-2) | 2024 | [QAE_AnomalyDetection_Hdaib2024](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/QAE_AnomalyDetection_Hdaib2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/QAE_AnomalyDetection_Hdaib2024.ipynb) | partially reproduced |
| QC-016 | [Network attack detection scheme based on variational quantum neural network](https://doi.org/10.1007/s11227-022-04542-z) | 2022 | [VQNN_NetworkAttack_Gong2022](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQNN_NetworkAttack_Gong2022.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQNN_NetworkAttack_Gong2022.ipynb) | partially reproduced |
| QC-017 | [Security intrusion detection using quantum machine learning techniques](https://doi.org/10.1007/s11416-022-00435-0) | 2023 | [QSVM_QCNN_StreamIDS_Kalinin2023](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/QSVM_QCNN_StreamIDS_Kalinin2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/QSVM_QCNN_StreamIDS_Kalinin2023.ipynb) | partially reproduced |
| QC-018 | [QML-IDS: Quantum Machine Learning Intrusion Detection System](https://doi.org/10.1109/ISCC61673.2024.10733655) | 2024 | [VQC_IntrusionDetectionUNSW_deAbreu2024](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQC_IntrusionDetectionUNSW_deAbreu2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQC_IntrusionDetectionUNSW_deAbreu2024.ipynb) | partially reproduced |
| QC-020 | [An In-Depth Comparative Study of Quantum-Classical Encoding Methods for Network Intrusion Detection](https://doi.org/10.1109/OJCOMS.2025.3537957) | 2025 | [HybridQNN_EncodingComparison_Kadi2025](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/HybridQNN_EncodingComparison_Kadi2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/HybridQNN_EncodingComparison_Kadi2025.ipynb) | partially reproduced |
| QC-022 | [Fine-tuned Variational Quantum Classifiers for Cyber Attacks Detection based on Parameterized Quantum Circuits and Optimizers](https://doi.org/10.1109/COMPSAC61105.2024.00144) | 2024 | [VQC_IntrusionDetection_Rahman2024](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQC_IntrusionDetection_Rahman2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQC_IntrusionDetection_Rahman2024.ipynb) | partially reproduced |
| QC-034 | [Quantum-Neural Network Model for Platform Independent Ddos Attack Classification in Cyber Security](https://doi.org/10.1002/qute.202400084) | 2024 | [QNN_DDoS_Kucukkara2024](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/QNN_DDoS_Kucukkara2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/QNN_DDoS_Kucukkara2024.ipynb) | partially reproduced |
| QC-039 | [A Hybrid Quantum Framework for Ultra-Secure Communication and Anomaly Detection in IoT Systems](https://doi.org/10.1007/978-981-95-5136-1_30) | 2026 | [HybridQSVMQNN_IoTAnomalyDetection_Deepa2026](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/HybridQSVMQNN_IoTAnomalyDetection_Deepa2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/HybridQSVMQNN_IoTAnomalyDetection_Deepa2026.ipynb) | partially reproduced |
| QC-041 | [A Lightweight Hybrid Quantum Neural Network for Binary Intrusion Detection](https://doi.org/10.1109/COMPSYSTECH69798.2026.11683102) | 2026 | [HybridQNN_IntrusionDetection_Kerkatou2026](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/HybridQNN_IntrusionDetection_Kerkatou2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/HybridQNN_IntrusionDetection_Kerkatou2026.ipynb) | partially reproduced |
| QC-055 | [Benchmarking quantum machine learning methods for intrusion detection on noisy quantum computers](https://doi.org/10.1007/s42484-026-00379-4) | 2026 | [QML_NoisyIDSBenchmark_Cirillo2026](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/QML_NoisyIDSBenchmark_Cirillo2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/QML_NoisyIDSBenchmark_Cirillo2026.ipynb) | partially reproduced |
| QC-065 | [DEHOA-optimized deep intrusion detection with quantum neural network extensions for IoT network security](https://doi.org/10.1016/j.array.2026.101085) | 2026 | [DEHOAQNN_IoTIntrusion_Mohammad2026](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/DEHOAQNN_IoTIntrusion_Mohammad2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/DEHOAQNN_IoTIntrusion_Mohammad2026.ipynb) | partially reproduced |
| QC-069 | [Embedding-Dependent Performance of Variational Quantum Reinforcement Learning for Intrusion Detection Under Dimensionality Constraints](https://doi.org/10.3390/electronics15132853) | 2026 | [VQRL_IntrusionDetection_Kerkatou2026](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQRL_IntrusionDetection_Kerkatou2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQRL_IntrusionDetection_Kerkatou2026.ipynb) | partially reproduced |
| QC-071 | [Evaluation of Variational Quantum Classifiers (VQC) for Cyberattack Detection in the NISQ Era](https://doi.org/10.3390/jsan15040067) | 2026 | [VQC_IntrusionDetection_Thomos2026](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQC_IntrusionDetection_Thomos2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQC_IntrusionDetection_Thomos2026.ipynb) | partially reproduced |
| QC-073 | [Federated Variational Quantum Neural Networks for Privacy-Preserving Anomaly Detection in IoT](https://doi.org/10.1109/SMARTCOMP-Companion70724.2026.00033) | 2026 | [FedVQC_IoTAnomalyDetection_Delhibabu2026](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/FedVQC_IoTAnomalyDetection_Delhibabu2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/FedVQC_IoTAnomalyDetection_Delhibabu2026.ipynb) | partially reproduced |
| QC-087 | [Leveraging Quantum Kernel Methods for Enhanced Intrusion Detection](https://doi.org/10.1109/COMSNETS67989.2026.11418222) | 2026 | [QSVM_IntrusionDetection_Tiwari2026](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/QSVM_IntrusionDetection_Tiwari2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/QSVM_IntrusionDetection_Tiwari2026.ipynb) | partially reproduced |
| QC-216 | [QuantumNetSec: Quantum Machine Learning for Network Security](https://doi.org/10.1002/nem.70018) | 2025 | [VQC_IntrusionDetection_deAbreu2025](https://github.com/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQC_IntrusionDetection_deAbreu2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/01_Network_Intrusion_Detection/VQC_IntrusionDetection_deAbreu2025.ipynb) | partially reproduced |

### 02 Zero Day Attack Detection  (2 of 8 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-108 | [Quantum-Enhanced Intrusion Detection Using Quantum Circuit Born Machines for Zero-Day Attack Detection](https://doi.org/10.32604/cmc.2026.075326) | 2026 | [QCBM_ZeroDay_AlMalwi2026](https://github.com/owlmt/QML/blob/main/02_Zero_Day_Attack_Detection/QCBM_ZeroDay_AlMalwi2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/02_Zero_Day_Attack_Detection/QCBM_ZeroDay_AlMalwi2026.ipynb) | partially reproduced |
| QC-136 | [A Non-Monotonic Relationship: An Empirical Analysis of Hybrid Quantum Classifiers for Unseen Ransomware Detection](https://arxiv.org/abs/2509.07924) | 2025 | [HybridVQC_UnseenRansomware_Le2025](https://github.com/owlmt/QML/blob/main/02_Zero_Day_Attack_Detection/HybridVQC_UnseenRansomware_Le2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/02_Zero_Day_Attack_Detection/HybridVQC_UnseenRansomware_Le2025.ipynb) | partially reproduced |

### 03 DDoS DoS Detection  (4 of 14 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-006 | [Quantum-enhanced representation learning: A quanvolutional autoencoder approach against ddos threats](https://doi.org/10.3390/make6020044) | 2024 | [QAE_DDoSHivePlots_Rivas2024](https://github.com/owlmt/QML/blob/main/03_DDoS_DoS_Detection/QAE_DDoSHivePlots_Rivas2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/03_DDoS_DoS_Detection/QAE_DDoSHivePlots_Rivas2024.ipynb) | partially reproduced |
| QC-030 | [Quantum machine learning for security assessment in the internet of medical things (IoMT)](https://doi.org/10.3390/fi15080271) | 2023 | [HybridQNN_IoMTSecurity_Rajawat2023](https://github.com/owlmt/QML/blob/main/03_DDoS_DoS_Detection/HybridQNN_IoMTSecurity_Rajawat2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/03_DDoS_DoS_Detection/HybridQNN_IoMTSecurity_Rajawat2023.ipynb) | partially reproduced |
| QC-033 | [Quantum computing and machine learning for cybersecurity: Distributed denial of service (DDoS) attack detection on smart micro-grid](https://doi.org/10.3390/en16083572) | 2023 | [QSVM_DDoS_Said2023](https://github.com/owlmt/QML/blob/main/03_DDoS_DoS_Detection/QSVM_DDoS_Said2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/03_DDoS_DoS_Detection/QSVM_DDoS_Said2023.ipynb) | partially reproduced |
| QC-068 | [Early Detection of Distributed Denial of Service in Cloud Computing Using Quantum-Enhanced Knowledge Distillation Framework](https://doi.org/10.3390/electronics15112327) | 2026 | [QNN_KnowledgeDistillationDDoS_Krishnamurthy2026](https://github.com/owlmt/QML/blob/main/03_DDoS_DoS_Detection/QNN_KnowledgeDistillationDDoS_Krishnamurthy2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/03_DDoS_DoS_Detection/QNN_KnowledgeDistillationDDoS_Krishnamurthy2026.ipynb) | partially reproduced |

### 04 Botnet DGA Detection  (2 of 4 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-002 | [Stabilized quantum-enhanced SIEM architecture and speed-up through Hoeffding tree algorithms enable quantum cybersecurity analytics in botnet detection](https://doi.org/10.1038/s41598-024-51941-8) | 2024 | [QHTC_BotnetDGA_Tehrani2024](https://github.com/owlmt/QML/blob/main/04_Botnet_DGA_Detection/QHTC_BotnetDGA_Tehrani2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/04_Botnet_DGA_Detection/QHTC_BotnetDGA_Tehrani2024.ipynb) | partially reproduced |
| QC-024 | [Evaluating hybrid quantum-classical deep learning for cybersecurity botnet DGA detection](https://doi.org/10.1016/j.procs.2021.12.135) | 2022 | [HybridQNN_BotnetDGA_Suryotrisongko2022](https://github.com/owlmt/QML/blob/main/04_Botnet_DGA_Detection/HybridQNN_BotnetDGA_Suryotrisongko2022.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/04_Botnet_DGA_Detection/HybridQNN_BotnetDGA_Suryotrisongko2022.ipynb) | partially reproduced |

### 05 Malware Detection  (6 of 16 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-001 | [Quantum Adversarial Attacks: Developing Quantum FGSM Algorithm](https://doi.org/10.1109/COMPSAC61105.2024.00145) | 2024 | [HybridQNN_QFGSM_Akter2024](https://github.com/owlmt/QML/blob/main/05_Malware_Detection/HybridQNN_QFGSM_Akter2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/05_Malware_Detection/HybridQNN_QFGSM_Akter2024.ipynb) | partially reproduced |
| QC-009 | [Software supply chain vulnerabilities detection in source code: Performance comparison between traditional and quantum machine learning algorithms](https://doi.org/10.1109/BigData55660.2022.10020813) | 2022 | [QNN_SupplyChainClaMP_Akter2022](https://github.com/owlmt/QML/blob/main/05_Malware_Detection/QNN_SupplyChainClaMP_Akter2022.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/05_Malware_Detection/QNN_SupplyChainClaMP_Akter2022.ipynb) | partially reproduced |
| QC-010 | [Exploring the vulnerabilities of machine learning and quantum machine learning to adversarial attacks using a malware dataset: a comparative analysis](https://doi.org/10.1109/SSE60056.2023.00037) | 2023 | [HybridQNN_AdversarialNoise_Akter2023](https://github.com/owlmt/QML/blob/main/05_Malware_Detection/HybridQNN_AdversarialNoise_Akter2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/05_Malware_Detection/HybridQNN_AdversarialNoise_Akter2023.ipynb) | partially reproduced |
| QC-011 | [Quantum Convolutional Neural Network-based Online Malware File Detection for Smart Grid Devices](https://doi.org/10.1109/DMC58182.2023.10412597) | 2023 | [QCNN_MalwareImageDTL_Akash2023](https://github.com/owlmt/QML/blob/main/05_Malware_Detection/QCNN_MalwareImageDTL_Akash2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/05_Malware_Detection/QCNN_MalwareImageDTL_Akash2023.ipynb) | partially reproduced |
| QC-013 | [Towards an In-Depth Detection of Malware Using Multi-QCNN](https://doi.org/10.1007/978-3-031-63778-0_29) | 2024 | [QCNN_MalwareMultiSection_Quertier2024](https://github.com/owlmt/QML/blob/main/05_Malware_Detection/QCNN_MalwareMultiSection_Quertier2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/05_Malware_Detection/QCNN_MalwareMultiSection_Quertier2024.ipynb) | partially reproduced |
| QC-049 | [Adversarially Robust Quantum-Classical Neural Network for Malware Detection](https://doi.org/10.1145/3807501.3808237) | 2026 | [HybridQNN_MalwareAdversarial_Vyas2026](https://github.com/owlmt/QML/blob/main/05_Malware_Detection/HybridQNN_MalwareAdversarial_Vyas2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/05_Malware_Detection/HybridQNN_MalwareAdversarial_Vyas2026.ipynb) | partially reproduced |

### 06 Android Malware Detection  (3 of 7 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-025 | [Optimizing quantum machine learning for proactive cybersecurity](https://doi.org/10.1007/s11081-024-09934-z) | 2024 | [VQC_PhishingMalwareSpam_RosaRemedios2024](https://github.com/owlmt/QML/blob/main/06_Android_Malware_Detection/VQC_PhishingMalwareSpam_RosaRemedios2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/06_Android_Malware_Detection/VQC_PhishingMalwareSpam_RosaRemedios2024.ipynb) | partially reproduced |
| QC-092 | [Noise-Aware Hybrid Classical-Quantum Framework for Android Malware Detection](https://doi.org/10.1109/ICESIC67389.2026.11496523) | 2026 | [QSVM_AndroidMalware_Mohandass2026](https://github.com/owlmt/QML/blob/main/06_Android_Malware_Detection/QSVM_AndroidMalware_Mohandass2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/06_Android_Malware_Detection/QSVM_AndroidMalware_Mohandass2026.ipynb) | partially reproduced |
| QC-316 | [Introducing Quantum Computing in Mobile Malware Detection](https://doi.org/10.1145/3538969.3543816) | 2022 | [HybridQCNN_AndroidMalwareImages_Ciaramella2022](https://github.com/owlmt/QML/blob/main/06_Android_Malware_Detection/HybridQCNN_AndroidMalwareImages_Ciaramella2022.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/06_Android_Malware_Detection/HybridQCNN_AndroidMalwareImages_Ciaramella2022.ipynb) | partially reproduced |

### 07 Ransomware Detection  (2 of 4 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-021 | [Quantum Exploration in Ransomware Detection with Conventional Machine Learning Approaches](https://doi.org/10.1109/InC460750.2024.10649082) | 2024 | [QSVM_RansomwareDetection_Kaur2024](https://github.com/owlmt/QML/blob/main/07_Ransomware_Detection/QSVM_RansomwareDetection_Kaur2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/07_Ransomware_Detection/QSVM_RansomwareDetection_Kaur2024.ipynb) | partially reproduced |
| QC-035 | [Ransomware Detection Using Quantum Neural Networks](https://doi.org/10.1109/ICSCAN62807.2024.10894015) | 2024 | [QNN_Ransomware_Varalakshmi2024](https://github.com/owlmt/QML/blob/main/07_Ransomware_Detection/QNN_Ransomware_Varalakshmi2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/07_Ransomware_Detection/QNN_Ransomware_Varalakshmi2024.ipynb) | partially reproduced |

### 08 Phishing Detection  (4 of 12 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-007 | [Zérosdetect: Phishing URL Detection with Quantum-Driven Zero-shot Learning](https://doi.org/10.1109/ICSC60394.2023.10440725) | 2023 | [QNN_PhishingURL_Bangroo2023](https://github.com/owlmt/QML/blob/main/08_Phishing_Detection/QNN_PhishingURL_Bangroo2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/08_Phishing_Detection/QNN_PhishingURL_Bangroo2023.ipynb) | partially reproduced |
| QC-053 | [Batch-Wise Ensemble Evaluation of Classical SVM and Quantum SVM for Email Phishing Detection](https://doi.org/10.1109/QPAIN69676.2026.11546403) | 2026 | [QSVM_EmailPhishing_Hridi2026](https://github.com/owlmt/QML/blob/main/08_Phishing_Detection/QSVM_EmailPhishing_Hridi2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/08_Phishing_Detection/QSVM_EmailPhishing_Hridi2026.ipynb) | partially reproduced |
| QC-066 | [Detecting Phishing in Ethereum Networks using Quantum Machine Learning](https://arxiv.org/abs/2607.12828) | 2026 | [QRAC_EthereumPhishing_Guddanti2026](https://github.com/owlmt/QML/blob/main/08_Phishing_Detection/QRAC_EthereumPhishing_Guddanti2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/08_Phishing_Detection/QRAC_EthereumPhishing_Guddanti2026.ipynb) | partially reproduced |
| QC-182 | [PhishVQC: Optimizing Phishing URL Detection with Correlation Based Feature Selection and Variational Quantum Classifier](https://doi.org/10.1109/ISACC65211.2025.10969366) | 2025 | [VQC_PhishingURL_Shahriyar2025](https://github.com/owlmt/QML/blob/main/08_Phishing_Detection/VQC_PhishingURL_Shahriyar2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/08_Phishing_Detection/VQC_PhishingURL_Shahriyar2025.ipynb) | partially reproduced |

### 09 Malicious URL Detection  (2 of 5 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-026 | [Detection of malicious URLs using machine learning](https://doi.org/10.1007/s11276-024-03700-w) | 2024 | [VQC_MaliciousURL_ReyesDorta2024](https://github.com/owlmt/QML/blob/main/09_Malicious_URL_Detection/VQC_MaliciousURL_ReyesDorta2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/09_Malicious_URL_Detection/VQC_MaliciousURL_ReyesDorta2024.ipynb) | partially reproduced |
| QC-199 | [Quantum-Enhanced Machine Learning for Cybersecurity: Evaluating Malicious URL Detection](https://doi.org/10.3390/electronics14091827) | 2025 | [QSVM_MaliciousURL_Eze2025](https://github.com/owlmt/QML/blob/main/09_Malicious_URL_Detection/QSVM_MaliciousURL_Eze2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/09_Malicious_URL_Detection/QSVM_MaliciousURL_Eze2025.ipynb) | partially reproduced |

### 10 Spam Detection  (1 of 1 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-151 | [Cyber Threat Detection Enabled by Quantum Computing](https://arxiv.org/abs/2512.18493) | 2025 | [HybridQSVM_SpamIDS_Chen2025](https://github.com/owlmt/QML/blob/main/10_Spam_Detection/HybridQSVM_SpamIDS_Chen2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/10_Spam_Detection/HybridQSVM_SpamIDS_Chen2025.ipynb) | partially reproduced |

### 11 Vulnerability Software Supply Chain Attacks  (2 of 9 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-008 | [Quantum clustering for cybersecurity](https://arxiv.org/abs/2408.02314) | 2024 | [QKMeans_CISAVulnerabilities_ElMaouaki2024](https://github.com/owlmt/QML/blob/main/11_Vulnerability_Software_Supply_Chain_Attacks/QKMeans_CISAVulnerabilities_ElMaouaki2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/11_Vulnerability_Software_Supply_Chain_Attacks/QKMeans_CISAVulnerabilities_ElMaouaki2024.ipynb) | partially reproduced |
| QC-168 | [Hybrid Quantum–Classical Deep Neural Networks Based Smart Contract Vulnerability Detection](https://doi.org/10.3390/app15074037) | 2025 | [HybridQNN_SmartContractVuln_Durgut2025](https://github.com/owlmt/QML/blob/main/11_Vulnerability_Software_Supply_Chain_Attacks/HybridQNN_SmartContractVuln_Durgut2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/11_Vulnerability_Software_Supply_Chain_Attacks/HybridQNN_SmartContractVuln_Durgut2025.ipynb) | partially reproduced |

### 12 Cryptojacking Detection  (1 of 1 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-032 | [Quant-Jack: Quantum Machine Learning to Detect Cryptojacking Attacks in IIoT Networks](https://doi.org/10.1109/ICCWorkshops59551.2024.10615371) | 2024 | [QNN_Cryptojacking_Bhattacharya2024](https://github.com/owlmt/QML/blob/main/12_Cryptojacking_Detection/QNN_Cryptojacking_Bhattacharya2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/12_Cryptojacking_Detection/QNN_Cryptojacking_Bhattacharya2024.ipynb) | partially reproduced |

### 13 Encrypted Malicious Traffic Detection  (2 of 2 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-070 | [Encrypted network traffic analysis using quantum machine learning](https://doi.org/10.1140/epjqt/s40507-025-00459-7) | 2026 | [HybridQML_EncryptedTraffic_Sodar2026](https://github.com/owlmt/QML/blob/main/13_Encrypted_Malicious_Traffic_Detection/HybridQML_EncryptedTraffic_Sodar2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/13_Encrypted_Malicious_Traffic_Detection/HybridQML_EncryptedTraffic_Sodar2026.ipynb) | partially reproduced |
| QC-198 | [Quantum deep learning for encrypted malicious traffic detection: a hybrid approach for secure network analysis](https://doi.org/10.31705/ADScAI.2025.56) | 2025 | [HybridQNN_EncryptedTraffic_Hariharan2025](https://github.com/owlmt/QML/blob/main/13_Encrypted_Malicious_Traffic_Detection/HybridQNN_EncryptedTraffic_Hariharan2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/13_Encrypted_Malicious_Traffic_Detection/HybridQNN_EncryptedTraffic_Hariharan2025.ipynb) | partially reproduced |

### 14 IoT IIoT Attack Detection  (5 of 32 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-023 | [Securing smart cities: Unraveling quantum as a service](https://doi.org/10.1145/3617570.3617865) | 2023 | [QBoost_VQC_PegasosQSVC_SmartCityIDS_Caivano2023](https://github.com/owlmt/QML/blob/main/14_IoT_IIoT_Attack_Detection/QBoost_VQC_PegasosQSVC_SmartCityIDS_Caivano2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/14_IoT_IIoT_Attack_Detection/QBoost_VQC_PegasosQSVC_SmartCityIDS_Caivano2023.ipynb) | partially reproduced |
| QC-031 | [Hybrid quantum architecture for smart city security](https://doi.org/10.1016/j.jss.2024.112161) | 2024 | [QBoost_SmartCitySIEM_CICIoT2023_Barletta2024](https://github.com/owlmt/QML/blob/main/14_IoT_IIoT_Attack_Detection/QBoost_SmartCitySIEM_CICIoT2023_Barletta2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/14_IoT_IIoT_Attack_Detection/QBoost_SmartCitySIEM_CICIoT2023_Barletta2024.ipynb) | partially reproduced |
| QC-042 | [A novel metaheuristic-enhanced quantum-classical neural network for attack detection in agriculture IoT systems](https://doi.org/10.1007/s11227-025-08118-5) | 2026 | [HybridQNN_AgIoTIntrusion_Gul2026](https://github.com/owlmt/QML/blob/main/14_IoT_IIoT_Attack_Detection/HybridQNN_AgIoTIntrusion_Gul2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/14_IoT_IIoT_Attack_Detection/HybridQNN_AgIoTIntrusion_Gul2026.ipynb) | partially reproduced |
| QC-105 | [Quantum-driven enhanced machine learning algorithm for intrusion detection in Internet of things environment](https://doi.org/10.1140/epjqt/s40507-026-00463-5) | 2026 | [HybridQNN_IoTIntrusion_Bharathi2026](https://github.com/owlmt/QML/blob/main/14_IoT_IIoT_Attack_Detection/HybridQNN_IoTIntrusion_Bharathi2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/14_IoT_IIoT_Attack_Detection/HybridQNN_IoTIntrusion_Bharathi2026.ipynb) | partially reproduced |
| QC-171 | [Intrusion Detection in IoT Networks using a Hybrid Quantum-Classical Graph Neural Network](https://doi.org/10.1109/VCRIS68011.2025.11250552) | 2025 | [HybridQNN_IoTIntrusion_Hoang2025](https://github.com/owlmt/QML/blob/main/14_IoT_IIoT_Attack_Detection/HybridQNN_IoTIntrusion_Hoang2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/14_IoT_IIoT_Attack_Detection/HybridQNN_IoTIntrusion_Hoang2025.ipynb) | partially reproduced |

### 15 Smart Grid Power System Attacks  (4 of 12 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-028 | [Exploring quantum learning in the smart grid through the evolution of noisy finite fourier series](https://doi.org/10.3389/fenrg.2023.1061602) | 2023 | [QNN_FDIQuantumData_Nader2023](https://github.com/owlmt/QML/blob/main/15_Smart_Grid_Power_System_Attacks/QNN_FDIQuantumData_Nader2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/15_Smart_Grid_Power_System_Attacks/QNN_FDIQuantumData_Nader2023.ipynb) | partially reproduced |
| QC-054 | [Benchmarking Quantum Machine Learning for Power-System Attack Detection: Evaluation Choices Decide the Outcome Before the Models Do](https://arxiv.org/abs/2608.15617) | 2026 | [QSVM_PowerGridAttack_Islam2026](https://github.com/owlmt/QML/blob/main/15_Smart_Grid_Power_System_Attacks/QSVM_PowerGridAttack_Islam2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/15_Smart_Grid_Power_System_Attacks/QSVM_PowerGridAttack_Islam2026.ipynb) | partially reproduced |
| QC-119 | [QUPID: A Partitioned Quantum Neural Network for Anomaly Detection in Smart Grid](https://arxiv.org/abs/2601.11500) | 2026 | [QUPID_SmartGridAnomaly_Ngo2026](https://github.com/owlmt/QML/blob/main/15_Smart_Grid_Power_System_Attacks/QUPID_SmartGridAnomaly_Ngo2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/15_Smart_Grid_Power_System_Attacks/QUPID_SmartGridAnomaly_Ngo2026.ipynb) | partially reproduced |
| QC-183 | [Power Theft Detection in Smart Grids Using Quantum Machine Learning](https://doi.org/10.1109/ACCESS.2025.3558143) | 2025 | [HybridQNN_PowerTheft_Blazakis2025](https://github.com/owlmt/QML/blob/main/15_Smart_Grid_Power_System_Attacks/HybridQNN_PowerTheft_Blazakis2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/15_Smart_Grid_Power_System_Attacks/HybridQNN_PowerTheft_Blazakis2025.ipynb) | partially reproduced |

### 16 ICS SCADA Cyber Physical Attacks  (2 of 4 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-202 | [Quantum-Hybrid Support Vector Machines for Anomaly Detection in Industrial Control Systems](https://arxiv.org/abs/2506.17824) | 2025 | [QSVM_AnomalyDetectionICS_Cultice2025](https://github.com/owlmt/QML/blob/main/16_ICS_SCADA_Cyber_Physical_Attacks/QSVM_AnomalyDetectionICS_Cultice2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/16_ICS_SCADA_Cyber_Physical_Attacks/QSVM_AnomalyDetectionICS_Cultice2025.ipynb) | partially reproduced |
| QC-238 | [Anomaly Detection for Real-World Cyber-Physical Security using Quantum Hybrid Support Vector Machines](https://doi.org/10.1109/ISVLSI61997.2024.00117) | 2024 | [QSVM_AnomalyDetection_Cultice2024](https://github.com/owlmt/QML/blob/main/16_ICS_SCADA_Cyber_Physical_Attacks/QSVM_AnomalyDetection_Cultice2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/16_ICS_SCADA_Cyber_Physical_Attacks/QSVM_AnomalyDetection_Cultice2024.ipynb) | partially reproduced |

### 17 Vehicle CAN Bus Attacks  (2 of 6 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-320 | [Quantum optimization for fast CAN bus intrusion detection](https://doi.org/10.1145/3549036.3562058) | 2022 | [QBoost_CANBusIntrusion_Caivano2022](https://github.com/owlmt/QML/blob/main/17_Vehicle_CAN_Bus_Attacks/QBoost_CANBusIntrusion_Caivano2022.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/17_Vehicle_CAN_Bus_Attacks/QBoost_CANBusIntrusion_Caivano2022.ipynb) | partially reproduced |
| QC-328 | [Hybrid Quantum-Classical Neural Network for Cloud-supported In-Vehicle Cyberattack Detection](https://arxiv.org/abs/2110.07467) | 2021 | [HybridQNN_CANAttack_Islam2021](https://github.com/owlmt/QML/blob/main/17_Vehicle_CAN_Bus_Attacks/HybridQNN_CANAttack_Islam2021.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/17_Vehicle_CAN_Bus_Attacks/HybridQNN_CANAttack_Islam2021.ipynb) | partially reproduced |

### 18 Cloud Virtual Environment Threats  (3 of 4 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-012 | [A Quantum LSTM-based approach to cyber threat detection in virtual environment](https://doi.org/10.1007/s11227-024-06615-7) | 2025 | [QLSTM_SyscallThreat_Tripathi2025](https://github.com/owlmt/QML/blob/main/18_Cloud_Virtual_Environment_Threats/QLSTM_SyscallThreat_Tripathi2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/18_Cloud_Virtual_Environment_Threats/QLSTM_SyscallThreat_Tripathi2025.ipynb) | partially reproduced |
| QC-036 | [Quantum Neural Network Classification-Based Cyber Threat Detection in Virtual Environment](https://doi.org/10.1109/CSCI62032.2023.00070) | 2023 | [HybridQNN_VMIThreatDetection_Tripathi2023](https://github.com/owlmt/QML/blob/main/18_Cloud_Virtual_Environment_Threats/HybridQNN_VMIThreatDetection_Tripathi2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/18_Cloud_Virtual_Environment_Threats/HybridQNN_VMIThreatDetection_Tripathi2023.ipynb) | partially reproduced |
| QC-194 | [Quantum Autoencoders for Anomaly Detection in Cybersecurity](https://arxiv.org/abs/2510.21837) | 2025 | [QAE_AnomalyDetection_Senthil2025](https://github.com/owlmt/QML/blob/main/18_Cloud_Virtual_Environment_Threats/QAE_AnomalyDetection_Senthil2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/18_Cloud_Virtual_Environment_Threats/QAE_AnomalyDetection_Senthil2025.ipynb) | partially reproduced |

### 19 Cybersecurity Anomaly Detection  (1 of 1 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-004 | [Anomaly detection speed-up by quantum restricted Boltzmann machines](https://doi.org/10.1038/s42005-023-01390-y) | 2023 | [QRBM_AnomalyDetection_Moro2023](https://github.com/owlmt/QML/blob/main/19_Cybersecurity_Anomaly_Detection/QRBM_AnomalyDetection_Moro2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/19_Cybersecurity_Anomaly_Detection/QRBM_AnomalyDetection_Moro2023.ipynb) | partially reproduced |

### 20 Blockchain Attack Detection  (1 of 1 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-259 | [Quantum Deep Neural Network Based Classification of Attack Vectors on the Ethereum Blockchain](https://doi.org/10.4108/eetsis.5572) | 2024 | [QRBM_EthereumAttack_Rajawat2024](https://github.com/owlmt/QML/blob/main/20_Blockchain_Attack_Detection/QRBM_EthereumAttack_Rajawat2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/20_Blockchain_Attack_Detection/QRBM_EthereumAttack_Rajawat2024.ipynb) | partially reproduced |

### 21 QKD Attack Detection  (3 of 3 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-040 | [A Hybrid Quantum–Classical Neural Network Framework for the Detection of Quantum Hacking Attacks in CVQKD](https://doi.org/10.3390/app16062793) | 2026 | [HybridQNN_CVQKDAttackDetection_He2026](https://github.com/owlmt/QML/blob/main/21_QKD_Attack_Detection/HybridQNN_CVQKDAttackDetection_He2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/21_QKD_Attack_Detection/HybridQNN_CVQKDAttackDetection_He2026.ipynb) | partially reproduced |
| QC-093 | [Noise-Resistant Feature-Aware Attack Detection Using Quantum Machine Learning](https://arxiv.org/abs/2601.06762) | 2026 | [QSVM_CVQKDAttackDetection_Ding2026](https://github.com/owlmt/QML/blob/main/21_QKD_Attack_Detection/QSVM_CVQKDAttackDetection_Ding2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/21_QKD_Attack_Detection/QSVM_CVQKDAttackDetection_Ding2026.ipynb) | partially reproduced |
| QC-220 | [Resisting Quantum Key Distribution Attacks Using Quantum Machine Learning](https://arxiv.org/abs/2509.14282) | 2025 | [QLSTM_QKDAttack_AlKuwari2025](https://github.com/owlmt/QML/blob/main/21_QKD_Attack_Detection/QLSTM_QKDAttack_AlKuwari2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/21_QKD_Attack_Detection/QLSTM_QKDAttack_AlKuwari2025.ipynb) | partially reproduced |

### 22 Deepfake Spoofing Detection  (2 of 4 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-219 | [Reliable Audio Deepfake Detection in Variable Conditions via Quantum-Kernel SVMs](https://arxiv.org/abs/2512.18797) | 2025 | [QSVM_AudioDeepfake_Amin2025](https://github.com/owlmt/QML/blob/main/22_Deepfake_Spoofing_Detection/QSVM_AudioDeepfake_Amin2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/22_Deepfake_Spoofing_Detection/QSVM_AudioDeepfake_Amin2025.ipynb) | partially reproduced |
| QC-235 | [A Hybrid Quantum-Classical AI-Based Detection Strategy for Generative Adversarial Network-Based Deepfake Attacks on an Autonomous Vehicle Traffic Sign Classification System](https://arxiv.org/abs/2409.17311) | 2024 | [HybridQNN_DeepfakeTrafficSign_Salek2024](https://github.com/owlmt/QML/blob/main/22_Deepfake_Spoofing_Detection/HybridQNN_DeepfakeTrafficSign_Salek2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/22_Deepfake_Spoofing_Detection/HybridQNN_DeepfakeTrafficSign_Salek2024.ipynb) | partially reproduced |

### 23 Adversarial Attacks Against QML  (8 of 44 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-037 | [A Comprehensive Analysis of Accuracy and Robustness in Quantum Neural Networks](https://doi.org/10.48550/arxiv.2604.26110) | 2026 | [HybridQNN_AccuracyRobustness_Tran2026](https://github.com/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/HybridQNN_AccuracyRobustness_Tran2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/HybridQNN_AccuracyRobustness_Tran2026.ipynb) | partially reproduced |
| QC-045 | [Adversarial Robustness in Fake Quantum Simulators](https://doi.org/10.48550/arxiv.2610.01574) | 2026 | [QNN_AdversarialRobustness_Maussner2026](https://github.com/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QNN_AdversarialRobustness_Maussner2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QNN_AdversarialRobustness_Maussner2026.ipynb) | partially reproduced |
| QC-050 | [An End-to-End Multi-Stage Kill-Chain Attack on Quantum Neural Networks: Demonstration on Trapped-Ion Hardware](https://arxiv.org/abs/2607.03337) | 2026 | [QNN_KillChainAttack_Brugmann2026](https://github.com/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QNN_KillChainAttack_Brugmann2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QNN_KillChainAttack_Brugmann2026.ipynb) | partially reproduced |
| QC-051 | [Anomaly Detection with Quantum SVR in the NISQ Era: Limits of Robustness to Noise and Adversarial Attacks](https://doi.org/10.5220/0014218600004052) | 2026 | [QSVR_AnomalyDetection_Tscharke2026](https://github.com/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QSVR_AnomalyDetection_Tscharke2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QSVR_AnomalyDetection_Tscharke2026.ipynb) | partially reproduced |
| QC-063 | [Decoupling the Dual Impact of NISQ Noise on Quantum Adversarial Robustness](https://doi.org/10.3390/e28070719) | 2026 | [VQC_NoiseAdversarial_Wang2026](https://github.com/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/VQC_NoiseAdversarial_Wang2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/VQC_NoiseAdversarial_Wang2026.ipynb) | partially reproduced |
| QC-072 | [Feature-level analysis and adversarial transfer in rotationally equivariant quantum machine learning](https://doi.org/10.48550/arxiv.2604.15552) | 2026 | [QNN_EquivariantAdversarialTransfer_Krumtunger2026](https://github.com/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QNN_EquivariantAdversarialTransfer_Krumtunger2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QNN_EquivariantAdversarialTransfer_Krumtunger2026.ipynb) | partially reproduced |
| QC-234 | [A Comparative Analysis of Adversarial Robustness for Quantum and Classical Machine Learning Models](https://arxiv.org/abs/2404.16154) | 2024 | [QNN_AdversarialRobustness_Wendlinger2024](https://github.com/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QNN_AdversarialRobustness_Wendlinger2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QNN_AdversarialRobustness_Wendlinger2024.ipynb) | partially reproduced |
| QC-305 | [Quantum Neural Networks under Depolarization Noise: Exploring White-Box Attacks and Defenses](https://arxiv.org/abs/2311.17458) | 2023 | [QNN_DepolarizationNoiseRobustness_Winderl2023](https://github.com/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QNN_DepolarizationNoiseRobustness_Winderl2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/23_Adversarial_Attacks_Against_QML/QNN_DepolarizationNoiseRobustness_Winderl2023.ipynb) | partially reproduced |

### 24 Poisoning Attacks Against QML  (2 of 12 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-014 | [Adversarial poisoning attack on quantum machine learning models](https://arxiv.org/abs/2411.14412) | 2024 | [HybridQNN_LabelPoisoning_Kundu2024](https://github.com/owlmt/QML/blob/main/24_Poisoning_Attacks_Against_QML/HybridQNN_LabelPoisoning_Kundu2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/24_Poisoning_Attacks_Against_QML/HybridQNN_LabelPoisoning_Kundu2024.ipynb) | partially reproduced |
| QC-015 | [Quantum error propagation](https://arxiv.org/abs/2410.05145) | 2024 | [QSVM_ErrorPropagationPoisoning_Sultanow2024](https://github.com/owlmt/QML/blob/main/24_Poisoning_Attacks_Against_QML/QSVM_ErrorPropagationPoisoning_Sultanow2024.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/24_Poisoning_Attacks_Against_QML/QSVM_ErrorPropagationPoisoning_Sultanow2024.ipynb) | partially reproduced |

### 25 Backdoor Trojan Attacks Against QML  (5 of 19 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-043 | [A Quantum State Backdoor Attack Against Quantum Neural Networks](https://doi.org/10.1002/qute.202500791) | 2026 | [QNN_QuantumStateBackdoor_Zhao2026](https://github.com/owlmt/QML/blob/main/25_Backdoor_Trojan_Attacks_Against_QML/QNN_QuantumStateBackdoor_Zhao2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/25_Backdoor_Trojan_Attacks_Against_QML/QNN_QuantumStateBackdoor_Zhao2026.ipynb) | partially reproduced |
| QC-056 | [Black-box backdoor detection in quantum neural networks via dose-response Monte Carlo testing](https://doi.org/10.1088/2058-9565/ae7b80) | 2026 | [QNN_BackdoorDetection_Zhang2026](https://github.com/owlmt/QML/blob/main/25_Backdoor_Trojan_Attacks_Against_QML/QNN_BackdoorDetection_Zhang2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/25_Backdoor_Trojan_Attacks_Against_QML/QNN_BackdoorDetection_Zhang2026.ipynb) | partially reproduced |
| QC-057 | [Can Quantum Federated Learning Withstand Circuit-Level Backdoors?](https://doi.org/10.24963/ijcai.2026/518) | 2026 | [QFL_CircuitBackdoor_Mathur2026](https://github.com/owlmt/QML/blob/main/25_Backdoor_Trojan_Attacks_Against_QML/QFL_CircuitBackdoor_Mathur2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/25_Backdoor_Trojan_Attacks_Against_QML/QFL_CircuitBackdoor_Mathur2026.ipynb) | partially reproduced |
| QC-213 | [Quantum Properties Trojans (QuPTs) for Attacking Quantum Neural Networks](https://doi.org/10.1109/isvlsi65124.2025.11130199) | 2025 | [HybridQNN_QuPTTrojan_Bhowmik2025](https://github.com/owlmt/QML/blob/main/25_Backdoor_Trojan_Attacks_Against_QML/HybridQNN_QuPTTrojan_Bhowmik2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/25_Backdoor_Trojan_Attacks_Against_QML/HybridQNN_QuPTTrojan_Bhowmik2025.ipynb) | partially reproduced |
| QC-300 | [QDoor: Exploiting Approximate Synthesis for Backdoor Attacks in Quantum Neural Networks](https://doi.org/10.1109/QCE57702.2023.00124) | 2023 | [QNN_Backdoor_QDoor_Chu2023](https://github.com/owlmt/QML/blob/main/25_Backdoor_Trojan_Attacks_Against_QML/QNN_Backdoor_QDoor_Chu2023.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/25_Backdoor_Trojan_Attacks_Against_QML/QNN_Backdoor_QDoor_Chu2023.ipynb) | partially reproduced |

### 26 QML Model Extraction Theft  (2 of 14 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-150 | [CopyQNN: Quantum Neural Network Extraction Attack under Varying Quantum Noise](https://arxiv.org/abs/2504.00366) | 2025 | [QNN_ModelExtraction_Fu2025](https://github.com/owlmt/QML/blob/main/26_QML_Model_Extraction_Theft/QNN_ModelExtraction_Fu2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/26_QML_Model_Extraction_Theft/QNN_ModelExtraction_Fu2025.ipynb) | partially reproduced |
| QC-164 | [Guardians of the Quantum GAN](https://doi.org/10.1109/isqed65160.2025.11014340) | 2025 | [QGAN_HardwareWatermark_Ghosh2025](https://github.com/owlmt/QML/blob/main/26_QML_Model_Extraction_Theft/QGAN_HardwareWatermark_Ghosh2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/26_QML_Model_Extraction_Theft/QGAN_HardwareWatermark_Ghosh2025.ipynb) | partially reproduced |

### 27 QML Privacy Data Leakage  (3 of 20 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-059 | [Characterizing Privacy Risks of Quantum Machine Learning with Emergent Quantum-Native Access](https://doi.org/10.48550/arxiv.2609.05702) | 2026 | [QNN_MembershipInference_Tang2026](https://github.com/owlmt/QML/blob/main/27_QML_Privacy_Data_Leakage/QNN_MembershipInference_Tang2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/27_QML_Privacy_Data_Leakage/QNN_MembershipInference_Tang2026.ipynb) | partially reproduced |
| QC-197 | [Quantum Data Breach: Reusing Training Dataset by Untrusted Quantum Clouds](https://doi.org/10.1109/ISQED65160.2025.11014467) | 2025 | [QNN_DataBreach_Upadhyay2025](https://github.com/owlmt/QML/blob/main/27_QML_Privacy_Data_Leakage/QNN_DataBreach_Upadhyay2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/27_QML_Privacy_Data_Leakage/QNN_DataBreach_Upadhyay2025.ipynb) | partially reproduced |
| QC-214 | [Quantum Quandaries: Unraveling Encoding Vulnerabilities in Quantum Neural Networks](https://arxiv.org/abs/2502.01486) | 2025 | [QNN_EncodingLeakage_Upadhyay2025](https://github.com/owlmt/QML/blob/main/27_QML_Privacy_Data_Leakage/QNN_EncodingLeakage_Upadhyay2025.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/27_QML_Privacy_Data_Leakage/QNN_EncodingLeakage_Upadhyay2025.ipynb) | partially reproduced |

### 28 QML Hardware Side Channel Crosstalk Attacks  (2 of 2 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-099 | [QML-PipeGuard: Drift-Aware Behavioral Fingerprinting for Quantum Machine Learning Pipeline Integrity](https://doi.org/10.48550/arxiv.2605.25066) | 2026 | [QSVM_PipelineIntegrity_Yeniaras2026](https://github.com/owlmt/QML/blob/main/28_QML_Hardware_Side_Channel_Crosstalk_Attacks/QSVM_PipelineIntegrity_Yeniaras2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/28_QML_Hardware_Side_Channel_Crosstalk_Attacks/QSVM_PipelineIntegrity_Yeniaras2026.ipynb) | partially reproduced |
| QC-121 | [Security Aspects of Quantum Machine Learning (SecQML)](https://doi.org/10.24406/h-508719) | 2026 | [QNN_CrosstalkAttacks_Franco2026](https://github.com/owlmt/QML/blob/main/28_QML_Hardware_Side_Channel_Crosstalk_Attacks/QNN_CrosstalkAttacks_Franco2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/28_QML_Hardware_Side_Channel_Crosstalk_Attacks/QNN_CrosstalkAttacks_Franco2026.ipynb) | partially reproduced |

### 29 Adversarial Robustness Defences for QML  (6 of 72 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-058 | [Certifying Adversarial Robustness of Quantum Classifiers under Known-Readout Query Access](https://doi.org/10.48550/arxiv.2609.11637) | 2026 | [QNN_CertifiedRobustness_Guan2026](https://github.com/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/QNN_CertifiedRobustness_Guan2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/QNN_CertifiedRobustness_Guan2026.ipynb) | partially reproduced |
| QC-061 | [Controlled Steering-Based State Preparation for Adversarial-Robust Quantum Machine Learning](https://doi.org/10.48550/arxiv.2605.10954) | 2026 | [QNN_SteeringDefence_Sanjaya2026](https://github.com/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/QNN_SteeringDefence_Sanjaya2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/QNN_SteeringDefence_Sanjaya2026.ipynb) | partially reproduced |
| QC-062 | [Decoherence as Defence and the Magnitude of Noise Regularisation: A Rigorous N-Qubit Theory of Stochastic Quantum Neural Networks for Adversarially Robust Network Intrusion Detection](https://doi.org/10.48550/arxiv.2606.24219) | 2026 | [SQNN_AdversarialRobustIDS_Filardo2026](https://github.com/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/SQNN_AdversarialRobustIDS_Filardo2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/SQNN_AdversarialRobustIDS_Filardo2026.ipynb) | partially reproduced |
| QC-064 | [Defending Quantum Classifiers against Adversarial Perturbations through Quantum Autoencoders](https://arxiv.org/abs/2604.28176) | 2026 | [QAE_AdversarialDefence_Andrews2026](https://github.com/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/QAE_AdversarialDefence_Andrews2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/QAE_AdversarialDefence_Andrews2026.ipynb) | partially reproduced |
| QC-095 | [PQ-IDPS: Adversarially Robust Intrusion Detection for Post-Quantum Encrypted Traffic with Hybrid Classical-Quantum Machine Learning](https://doi.org/10.36227/techrxiv.176836457.72974723/v1) | 2026 | [HybridQNN_AdversarialRobustIDS_Anaedevha2026](https://github.com/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/HybridQNN_AdversarialRobustIDS_Anaedevha2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/HybridQNN_AdversarialRobustIDS_Anaedevha2026.ipynb) | partially reproduced |
| QC-117 | [Quantum Patches: Enhancing Robustness of Quantum Machine Learning Models](https://doi.org/10.48550/arxiv.2604.08827) | 2026 | [QNN_AdversarialRobustness_Tran2026](https://github.com/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/QNN_AdversarialRobustness_Tran2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/29_Adversarial_Robustness_Defences_for_QML/QNN_AdversarialRobustness_Tran2026.ipynb) | partially reproduced |

### 30 QML Defences Against ML Attacks  (3 of 7 papers)

| QC-ID | Paper | Year | Notebook | Status |
|---|---|---|---|---|
| QC-044 | [Adversarial Attack Detection in Federated Learning Using Quantum Recurrent Neural Network](https://doi.org/10.1155/acis/1176614) | 2026 | [QRNN_AdversarialAttackFL_Venkat2026](https://github.com/owlmt/QML/blob/main/30_QML_Defences_Against_ML_Attacks/QRNN_AdversarialAttackFL_Venkat2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/30_QML_Defences_Against_ML_Attacks/QRNN_AdversarialAttackFL_Venkat2026.ipynb) | partially reproduced |
| QC-077 | [HQMSGAN: Enhancing Adversarial Robustness Using Hybrid Quantum-Classical Multi-Scale Generative Adversarial Network](https://doi.org/10.3390/e28101089) | 2026 | [QGAN_AdversarialPurification_Stanly2026](https://github.com/owlmt/QML/blob/main/30_QML_Defences_Against_ML_Attacks/QGAN_AdversarialPurification_Stanly2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/30_QML_Defences_Against_ML_Attacks/QGAN_AdversarialPurification_Stanly2026.ipynb) | partially reproduced |
| QC-078 | [HQSU: Hybrid Quantum Selective Unlearning for Backdoor Mitigation in Federated Learning](https://doi.org/10.1109/qcnc69040.2026.00128) | 2026 | [HybridQNN_BackdoorUnlearning_Don2026](https://github.com/owlmt/QML/blob/main/30_QML_Defences_Against_ML_Attacks/HybridQNN_BackdoorUnlearning_Don2026.ipynb) · [Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/30_QML_Defences_Against_ML_Attacks/HybridQNN_BackdoorUnlearning_Don2026.ipynb) | partially reproduced |

### Topic assignment unresolved  (0 of 12 papers)

_No notebook yet._

## Papers without a notebook (blocked)

| QC-ID | Paper | Reason |
|---|---|---|
| QC-005 | Quantum Machine Learning: Perspectives in Cybersecurity | Perspective/position paper (SAFECOMP 2024 workshop, 9 pp.): overview of classical-shadow QGAN training [arXiv:2309.08426] and an Ising-machine learning scheme [ |
| QC-019 | Quantum machine learning in intrusion detection systems: a systematic mapping study | Systematic mapping review of 21 primary studies (4 databases, Petersen et al. protocol): no dataset, no model trained, no metric of the authors' own; Table 7 co |
| QC-027 | Quantum machine learning for network intrusion detection systems, a systematic literature review | Systematic literature review (Kitchenham SLR, Scopus 2017-2022, five included papers): no original experiment, dataset, model or metric; quoted accuracies belon |
| QC-029 | Quantum Machine Learning for Anomaly Detection in Consumer Electronics | Survey/overview paper (Bhowmik & Thapliyal, ISVLSI 2024, arXiv:2409.00294): generic QML anomaly-detection framework and five case studies summarised from other  |
| QC-046 | Adversarial Robustness in Quantum Machine Learning: A Scoping Review | Scoping review (PRISMA-ScR) of 53 published studies on adversarial robustness in QML; sections are Introduction, Methodology (search, screening, data extraction |
| QC-048 | Adversarially Robust Federated Quantum Machine Learning for Healthcare | PDF is a one-page extended abstract (NYSDS 2026, AI for Science track): title and abstract only, 3,042 characters, no methods, dataset source, sample sizes, cir |
| QC-052 | Backdoor Threats in Variational Quantum Circuits: Taxonomy, Attacks, and Defenses | Survey/taxonomy of backdoor attacks on VQCs (GLSVLSI 2026): sections Introduction, Preliminaries, Backdoors on VQCs (classical-like, compilation-enabled, quantu |
| QC-060 | Comparative Analysis of Classical and Quantum Machine Learning Approaches for Anomaly Detection in IoT Security | Literature review (Turkish): the abstract states it reviews recent IoT intrusion-detection literature; Section IV describes the reviewed studies' methods and Ta |

## Rules for adding a notebook

See `CLAUDE.md`: one notebook per paper in its topic folder, public data downloaded
inside the notebook, every transform fitted on the training split only, a classical
baseline on identical inputs, a claim-by-claim comparison with the paper, the two
mandatory visualisation sections, and a manifest row updated in the same commit.
