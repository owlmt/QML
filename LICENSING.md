# Licensing of this repository

Version 1.0, effective 2026-10-29. Applies to every revision of `owlmt/QML` published by the
copyright holder, including revisions earlier than the one that introduced this file.

This repository holds material of several kinds, owned by several parties and released under
several licences. This document says which licence applies to which file, what is **not** covered
by any licence granted here, and how the licences interact. `COPYRIGHT.md` states who owns what;
`CONTRIBUTING.md` states the terms under which contributions are accepted. The root `LICENSE` file
contains the GNU Affero General Public License v3.0 and **covers the source code only**, not the
whole repository.

Nothing in this document is legal advice. The licence texts themselves govern; this document only
says which text applies where.

## 1. Summary

| Category | What it covers | Licence | SPDX identifier | Licence text |
|---|---|---|---|---|
| A. Source code | original scripts, utilities, Qiskit/PennyLane implementations, the code cells of every notebook | GNU Affero General Public License, version 3.0 only | `AGPL-3.0-only` | `LICENSE` (same text as `LICENSES/AGPL-3.0-only.txt`) |
| B. Original educational content | explanations, tutorials, documentation, independently authored diagrams, the markdown cells of every notebook | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International | `CC-BY-NC-SA-4.0` | `LICENSES/CC-BY-NC-SA-4.0.txt` |
| C. Catalogue and bibliographic compilation | the copyright holder's original contributions to `manifest.csv`, `paper_index.csv`, `original_bibliography.md` and the dataset-atlas CSVs | Creative Commons Attribution 4.0 International | `CC-BY-4.0` | `LICENSES/CC-BY-4.0.txt` |
| D. Third-party material | published papers, their algorithms and methods, external datasets, third-party source code, open-source dependencies | **their own terms**; no licence is granted here | n/a | see section 5 |

The licences in categories A to C are granted by Madjid G. Tehrani for the material he owns
(see `COPYRIGHT.md`). They are not granted, and cannot be granted, for category D.

## 2. Category A: source code (`AGPL-3.0-only`)

Covered files:

- every file under `tools/` (`atlas_usage.py`, `backfill_qa_columns.py`, `execute_notebook.py`,
  `next_papers.py`, `notebook_summary.py`, `paper_index.py`, `pdf_text.py`, `publish_notebook.py`,
  `update_readme.py`, `verify_notebook.py`) and any other `.py` file the copyright holder adds;
- the **code cells** of every `.ipynb` notebook in the repository (root, `papers/`,
  `00_Cybersecurity_Dataset_Atlas/` and the topic folders `01_` to `30_`), including the
  configuration, import, data-loading, preprocessing, model, training, evaluation and plotting
  code written for this repository;
- build and helper scripts committed to the repository.

Terms: GNU AGPL-3.0-only, the full text of which is in `LICENSE`. In particular:

- you may use, study, modify and redistribute the code, including commercially, provided you comply
  with the licence, which requires that modified versions and derived works be released under the
  same licence with their complete corresponding source;
- section 13 of the AGPL extends the source-disclosure obligation to users who interact with a
  modified version over a network (for example a hosted service built on this code);
- all copyright notices and licence notices must be preserved (section 5 and section 7).

"Only" means version 3 of the AGPL applies and no later version is offered.

The code is provided **without any warranty**, as the licence states.

## 3. Category B: original educational content (`CC-BY-NC-SA-4.0`)

Covered material:

- the **markdown cells** of every notebook: the one-page paper summaries, the "What follows the
  paper and what had to be chosen" tables, the step-by-step explanations, the "Reading the paper
  critically" sections and the student exercises;
- the outputs stored in the notebooks that were produced by this repository's own code (figures,
  printed tables, circuit drawings), to the extent copyright subsists in them and subject to the
  terms of the dataset they depict (section 5.4);
- `README.md`, `CLAUDE.md`, `REPRODUCTION_LOG.md`, `REPRODUCTION_QUEUE.md`, `tools/AGENT_BRIEF.md`,
  `LICENSING.md`, `COPYRIGHT.md`, `CONTRIBUTING.md` and other documentation files, except for the
  licence texts themselves, which are reproduced verbatim under their own terms;
- independently authored diagrams and illustrations.

Terms: CC BY-NC-SA 4.0 (`LICENSES/CC-BY-NC-SA-4.0.txt`). You may share and adapt this material
for **non-commercial** purposes, with attribution (section 7), under the same licence. Commercial
use of category B material requires a separate licence from the copyright holder (section 8).

## 4. Category C: catalogue and bibliographic compilation (`CC-BY-4.0`)

Covered material: the copyright holder's original, copyrightable contributions to the compilation
in `manifest.csv`, `paper_index.csv`, `original_bibliography.md`,
`00_Cybersecurity_Dataset_Atlas/atlas_inventory.csv` and
`00_Cybersecurity_Dataset_Atlas/atlas_usage.csv`: the selection and arrangement of the entries,
the topic assignment, the reproduction status, the comparison of paper metrics with notebook
metrics, the notes, the feasibility assessments and the dataset-to-notebook mapping.

**Not covered, and not claimed:** bare bibliographic facts (titles, author names, years, venues,
DOIs, arXiv identifiers, URLs), which are facts and carry no copyright; the third-party papers
those entries describe; the external datasets the atlas documents; and any metric or number taken
from a paper, which remains that paper's content. Only the copyright holder's own contribution to
the compilation is licensed, and only to the extent it is copyrightable at all under the
applicable law.

Terms: CC BY 4.0 (`LICENSES/CC-BY-4.0.txt`): reuse, including commercial reuse, with attribution.

## 5. Category D: third-party material (no licence granted here)

The copyright holder does not own, does not claim and does not license the following. Reusing it
is subject to the terms of its own rights holders. Nothing in this repository replaces or removes a
third-party notice, and nothing here should be read as placing third-party material under the
licences of sections 2 to 4.

### 5.1 The published papers

Each notebook reproduces one paper listed in `manifest.csv`. The papers are the property of their
authors and publishers. They are **not distributed** in this repository: the PDFs are excluded by
`.gitignore` and are never committed. The notebooks cite each paper in full, quote at most short
passages for the purpose of comparison and criticism, and copy the paper's reported numbers only as
reference values in the claim-by-claim comparison tables. Citation of a paper does not imply
endorsement by its authors, and no licence to the paper is granted or implied.

### 5.2 Algorithms, concepts and methods

The algorithms, circuit designs, protocols and experimental methods described in the papers belong
to the scientific record. The repository's **implementations** of them are original code written
for this repository (category A), but the underlying ideas are not owned by the copyright holder,
and the licences here grant no rights in those ideas, nor in any patent that may cover them. The
AGPL's patent provisions (section 11 of the licence) apply only to the copyright holder's own
contributions.

### 5.3 Third-party source code

The audit of 2026-10-29 found no third-party source file copied into this repository. Several
notebooks nevertheless **depend on, download at run time, or were written with reference to** code
released by the papers' authors. In every such case the upstream code stays under its own licence,
its copyright belongs to its authors, and the attribution notice in the notebook must be kept. The
cases found are listed below; the upstream licence column records what the upstream repository
declared on 2026-10-29 and must be re-checked before any reuse that depends on it.

| Notebook | Upstream repository | Upstream licence (2026-10-29) | How the notebook uses it |
|---|---|---|---|
| `01_Network_Intrusion_Detection/HybridQNN_IntrusionAudit_Gillani2026.ipynb` | `Orqly-AI/quantum-ids-benchmark` | Orqly-AI Restricted Attribution License (ORAL) v1.0: personal, academic and non-commercial use only, attribution required | Downloads four of the authors' source files from a pinned commit at run time and imports them; the files are not stored in this repository. **Running this notebook is subject to ORAL; it may not be used commercially.** The copyright notice "Original Work by: Mirza Samad Ahmed Baig and Syeda Anshrah Gillani (Orqly-AI), Copyright (c) 2026" printed by the notebook must be preserved. |
| `04_Botnet_DGA_Detection/QHTC_BotnetDGA_Tehrani2024.ipynb` | `Sultanow/quantum-botnet-detection` and `owlmt/quantumHTC-repo` | no licence file in either repository (all rights reserved by default) | Downloads the paper authors' notebooks and the 2026 Author Correction code at pinned commits, verifies them against pinned SHA-256 hashes and runs them. The paper is co-authored by the copyright holder of this repository, but the upstream code has several authors and is **not** relicensed here. |
| `23_Adversarial_Attacks_Against_QML/HybridQNN_QPoisonAttack_Ergu2025.ipynb` | `Jaredabera/Q-Poisoning-Adversarial-Attack` | GPL-3.0 | Downloads the dataset archives from the repository and implements the paper's two attacks "exactly as in the authors' code". If any part of that implementation is a copy or close translation of the upstream code, that part remains GPL-3.0 code by its authors (compatible with AGPL-3.0 under section 13 of each licence) and keeps their copyright. |
| `23_Adversarial_Attacks_Against_QML/QNN_AdversarialRobustness_Maussner2026.ipynb` | `MarcMaussner/qml_cysec` | Unlicense (public domain dedication) | Downloads the authors' dataset file at a pinned commit and reuses their circuit definition. |
| `08_Phishing_Detection/EnsembleQML_EthereumPhishing_Ray2022.ipynb`, `QRAC_EthereumPhishing_Ray2023.ipynb`, `QRAC_EthereumPhishing_Guddanti2026.ipynb` | the papers' authors' repository (pinned commit `8e345c4`) | Apache-2.0 as stated in the notebooks | Downloads the authors' feature files (`.npy`) at run time; the models are re-implemented. |
| `19_Cybersecurity_Anomaly_Detection/VQC_AdaptiveShotAnomaly_Sudipto2026.ipynb` | `msudipto/AdaptiveShot_HybridQAD_Framework` | MIT | Settings that the paper leaves open were taken from the authors' code; marked `# CHOICE:` in the notebook. |
| `01_Network_Intrusion_Detection/QNNvsQSVM_IntrusionDetection_Kerkatou2026.ipynb`, `VQRL_IntrusionDetection_Kerkatou2026.ipynb` | `raidanis/QML-IDS-NSLKDD`, `raidanis/QRL_IDS` | MIT | Data mirror at a pinned commit; settings read from the authors' code. |
| `01_Network_Intrusion_Detection/QKSVM_OpenRAN_IntrusionDetection_Abreu2026.ipynb` | `DiegoAbreuSWB/qml_ids_wqusec_extended` | no licence file | Parameter values and the reduced O-RAN dataset CSV taken from the authors' public script and repository. |
| `02_Zero_Day_Attack_Detection/HybridVQC_UnseenRansomware_Le2025.ipynb` | `ailabteam/qml-ransomware-project` | no licence file | Dataset CSV downloaded from the repository; train/test identifier ranges read from the authors' code. |
| `01_Network_Intrusion_Detection/HybridQNN_EncodingComparison_Kadi2025.ipynb` | `ReSEC-Laboratory/QIDS` | no licence file | Written from the paper and from the authors' public Colab notebook, re-implemented in PyTorch; assumptions documented in the notebook. |
| `05_Malware_Detection/HybridQNN_MalwareAdversarial_Vyas2026.ipynb` | `KATHAN-VYAS/Quantum_MachineLearning` | no licence file | Hyper-parameters read from the authors' notebooks where the paper is silent. |
| `23_Adversarial_Attacks_Against_QML/QMLP_AdversarialRobustness_Nowmi2025.ipynb` | `IQSeC-Lab/SoK-QML` | no licence file | Dataset files downloaded from the repository. |
| `23_Adversarial_Attacks_Against_QML/QNN_AdversarialRobustness_Marchiori2025.ipynb` | authors' repository (pinned commit `b7b9818`) | not checked | Read to recover details the paper omits; the pipeline is the notebook's own. |
| `05_Malware_Detection/HybridQNN_AdversarialNoise_Akter2023.ipynb`, `QNN_SupplyChainClaMP_Akter2022.ipynb`, `HybridQNN_QFGSM_Akter2024.ipynb`; `11_Vulnerability_Software_Supply_Chain_Attacks/QSVM_SupplyChainClaMPReVeal_Masum2022.ipynb` | the ClaMP dataset authors' repository | see the repository | Dataset CSV downloaded at run time (data only). |
| `16_ICS_SCADA_Cyber_Physical_Attacks/QSVM_AnomalyDetectionICS_Cultice2025.ipynb`, `QSVM_AnomalyDetection_Cultice2024.ipynb` | `icsdataset/hai` | no licence file; the HAI dataset has its own terms | Dataset files downloaded at run time (data only). |
| `18_Cloud_Virtual_Environment_Threats/QBM_AnomalyDetection_Stein2024.ipynb` | `jonas-stein/QBM-Anomaly-Detection` | Apache-2.0 | Not used; the notebook is re-written from the paper. Listed for completeness. |
| `01_Network_Intrusion_Detection/HQCAE_UnsupervisedIDS_Rasyidi2025.ipynb`, `QGAN_FederatedIntrusionDetection_Cirillo2025.ipynb`, `QAE_TinyQL_IoTAnomalyDetection_Ngouen2026.ipynb` | authors' repositories named in the notebooks | various / none | Not used; the notebooks state they were written from the paper text only. |

Constructions that follow published **tutorials** of the quantum software vendors (the Qiskit
QCNN tutorial and the TensorFlow Quantum MNIST tutorial, both Apache-2.0; PennyLane's gate
decompositions, Apache-2.0) are re-implemented in the notebooks that name them. Apache-2.0 material
may be combined with AGPL-3.0 code; any Apache-2.0 notice that applies must be kept.

Where an upstream repository has **no licence file**, its code is all-rights-reserved by default.
The notebooks listed above read such code for facts (parameter values, split definitions, file
names) and download data files from it; they do not store its code. Anyone who wants to go further
than that must obtain permission from the upstream authors.

### 5.4 External datasets

The notebooks and the dataset atlas (`00_Cybersecurity_Dataset_Atlas/`) **download datasets at
run time**; no dataset is stored in this repository (`.gitignore` excludes them). Every dataset
belongs to its own rights holders and comes with its own terms, which the atlas records on each
dataset card and in the `license` column of `atlas_inventory.csv`. The terms range from public
domain and CC0 through CC BY 4.0, CC BY-SA, ODC-By and MIT to "research use only" (for example the
Canadian Institute for Cybersecurity, UNSW Canberra and university collections), registration-only
collections (iTrust SUTD, TU Braunschweig, Kaggle competitions, VirusShare) and at least one
non-commercial, no-derivatives set (the ADD 2023 development release, CC BY-NC-ND 4.0, used by
`22_Deepfake_Spoofing_Detection/QSVM_AudioDeepfake_Amin2025.ipynb`).

The user of a notebook is responsible for complying with the terms of every dataset it downloads.
A permissive licence on this repository's code does not extend to the data; in particular, a
"research use only" or non-commercial dataset cannot be used commercially merely because the code
that loads it is AGPL. Figures stored in the notebooks that depict such data are shared under
category B only to the extent the dataset's own terms allow.

### 5.5 Open-source dependencies

The notebooks install and import third-party libraries at run time; none is vendored in this
repository. Each keeps its own licence, for example Qiskit, qiskit-machine-learning, qiskit-aer,
qiskit-ibm-runtime, PennyLane, TensorFlow, TensorFlow Quantum and XGBoost (Apache-2.0);
scikit-learn, NumPy, pandas, SciPy, PyTorch and `river` (BSD-3-Clause); matplotlib (its own
PSF-based licence); `pypdf`, `nbformat`, `nbclient` and `huggingface_hub` (BSD or Apache-2.0).
These licences are compatible with distributing this repository's code under AGPL-3.0; using the
libraries creates no obligation beyond their own notices.

### 5.6 Licence documents

`LICENSE`, `LICENSES/AGPL-3.0-only.txt`, `LICENSES/CC-BY-NC-SA-4.0.txt` and
`LICENSES/CC-BY-4.0.txt` are verbatim copies of the official texts published by the Free Software
Foundation and Creative Commons, reproduced under the verbatim-copying permission each of them
states. The Developer Certificate of Origin quoted in `CONTRIBUTING.md` is reproduced verbatim under
its own permission.

## 6. Notebooks: one file, two licences

A Jupyter notebook is a single `.ipynb` file that holds code cells, markdown cells and stored
outputs. For every notebook in this repository:

- **code cells** are source code: `AGPL-3.0-only` (section 2);
- **markdown cells** are educational content: `CC-BY-NC-SA-4.0` (section 3);
- **stored outputs** produced by the code cells are treated as category B material subject to the
  underlying dataset's terms (sections 3 and 5.4);
- where a cell contains or depends on third-party material (section 5), that material keeps its own
  terms.

This statement applies to all notebooks, whether or not an individual notebook repeats it. The
notebooks themselves have deliberately not been edited to add a licensing cell, so that their
executed outputs and reproduction records remain exactly as validated.

Consequences:

- Redistributing a notebook unchanged for non-commercial purposes is permitted by both licences,
  with attribution.
- Commercial use of the **code** cells alone is permitted under the AGPL's terms (section 2).
  Commercial use of the **markdown** cells (for example in a paid course or a commercial book)
  needs a separate licence (section 8).
- A derived notebook must keep the code under AGPL-3.0-only and the educational text under
  CC BY-NC-SA 4.0 (the ShareAlike condition), with the attribution of section 7.

## 7. Attribution

Attribution required by all three licences is satisfied by stating:

> Madjid G. Tehrani, *QML × Cybersecurity: reproducible notebooks of quantum machine learning
> papers and a cybersecurity dataset atlas*, https://github.com/owlmt/QML, licensed under
> AGPL-3.0-only (code), CC BY-NC-SA 4.0 (educational content) and CC BY 4.0 (catalogue).

together with a link to this `LICENSING.md`, an indication of any changes made, and the name of
the notebook or file reused. The paper that a notebook reproduces must be cited as well; that is a
matter of academic integrity and of the paper's own rights, not of these licences.

**Citation and licensing are separate matters.** `CITATION.cff` and the "How to cite" section of
`README.md` ask users to cite this repository in academic work; that request reflects scholarly
practice and does not create or modify any legal condition. The licences above set the legal terms
of reuse and apply whether or not the work is cited in a publication. Conversely, citing the
repository does not by itself satisfy the attribution conditions of the licences, which require the
elements listed above.

## 8. Commercial licensing

Madjid G. Tehrani expressly reserves the right to license the material he owns (categories A, B
and C) under terms other than the public licences above, for example:

- proprietary deployments of the code without the AGPL's source-disclosure obligations;
- enterprise or commercial training built on the educational content;
- commercial educational products (courses, books, platforms) that include the educational content;
- licensed integrations of the implementations into commercial software or services.

Such licences are available only for material the copyright holder owns. They cannot cover
third-party material (section 5), and they cannot cover contributions by other people except to the
extent those contributors have agreed (see `CONTRIBUTING.md`). Offering a separate commercial
licence does not withdraw or narrow the public licences, which remain available to everyone on
their own terms. To enquire, open an issue on the repository or contact the copyright holder
directly.

Any separately published textbook or other work by the copyright holder on quantum cybersecurity
analytics (QCA), whether or not it draws on material from this repository, is a distinct work. It
is **All Rights Reserved** unless its own licence states otherwise; nothing in this repository
licenses it.

## 9. How the licences interact

- **AGPL permits commercial use; CC BY-NC-SA does not.** The code may be used commercially provided
  the AGPL's copyleft and source-disclosure conditions are met. The educational content may not be
  used commercially without a separate licence. When a product combines both, the stricter
  condition governs the educational content and the AGPL governs the code; the two are not merged
  into one licence.
- **CC BY 4.0 is the most permissive** of the three and covers only the catalogue contribution.
  Combining catalogue data with the code or the educational content does not change the licence of
  either.
- **ShareAlike and copyleft operate separately.** A derivative of the educational content must be
  CC BY-NC-SA 4.0 (or a compatible licence as defined by Creative Commons); a derivative of the code
  must be AGPL-3.0-only. Neither licence pulls the other category under its own terms.
- **Third-party terms always prevail** for third-party material. A notebook that downloads
  non-commercial code (section 5.3) or research-use-only data (section 5.4) cannot be used beyond
  those terms, regardless of the licence of the notebook's own cells.
- **The root `LICENSE` file is not a repository-wide licence.** GitHub and other tools may display
  "AGPL-3.0" for the repository because the file is at the root; that display refers to the code
  only. This document, `COPYRIGHT.md` and the "Licensing" section of `README.md` give the scope.

## 10. SPDX identifiers

The licences used here are identified in the SPDX License List as `AGPL-3.0-only`,
`CC-BY-NC-SA-4.0` and `CC-BY-4.0`. Files in this repository do not carry per-file SPDX headers;
this document is the licence declaration for the repository. A contributor may add a header such as
`# SPDX-License-Identifier: AGPL-3.0-only` to a new script, and `tools/` scripts may receive one in
future, but the absence of a header does not change the licence stated here.

## 11. Changes to this document

The copyright holder may update this document, for instance to record new third-party cases or to
offer additional licences. A change never withdraws a licence already granted for an earlier
revision of the material; it may add options. The version and effective date at the top identify
each revision.
