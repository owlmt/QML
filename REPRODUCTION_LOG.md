# Reproduction log

One line per published notebook (newest last).

- 2026-10-17 | QC-033 | partially reproduced | [03_DDoS_DoS_Detection/QSVM_DDoS_Said2023.ipynb](03_DDoS_DoS_Detection/QSVM_DDoS_Said2023.ipynb) | Quantum computing and machine learning for cybersecurity: Distributed denial of service (DDoS) attack detection on smart micro-grid | paper: QSVM accuracy/precision/recall 99.91-99.94% (Fig.1); QSVM far ahead of SVM (Fig.2, SVM ~24% acc); QSVM 93% faster than SVM (Fig.3) | notebook: QSVM 99.90% acc / 99.89% prec / 99.91% rec (mean of 10 splits); RBF SVM 99.91% / 99.82% / 100%; QSVM 513x slower than SVM on simulator | Executed locally 2026-10-17 (Qiskit 2.5.2, 7.5 min, CICDDoS2019 SSDP via HF mirror). Accuracy level reproduced within 0.01-0.04 pt; QSVM-vs-SVM gap and 93% speed-up not reproduced; paper omits qubit count, feature map, encoding scale (4 qubits, ZZ map reps=2, tuned bandwidth chosen here). HHL claimed by paper, quantum-kernel SVM implemented.
