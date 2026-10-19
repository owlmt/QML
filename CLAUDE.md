# QML × Cybersecurity Colab Reproduction Factory

This repository (`owlmt/QML`, local checkout `C:\Users\madji\Desktop\QML`) reproduces the
quantum-machine-learning (QML) cybersecurity papers listed in `manifest.csv` as Jupyter/Colab
notebooks: one notebook per paper, filed into the 30 existing cybersecurity topic folders.
Notebooks are written for teaching: every step has a plain-language explanation, the notebook
downloads or generates its own data, trains a classical baseline on the same inputs, and ends with
an honest comparison of its own numbers against the paper's.

## Workspace layout

```
C:\Users\madji\Desktop\QML\                 git repo, branch main -> origin/main
  manifest.csv                              327 rows, one per paper (QC-001 ... QC-327)
  original_bibliography.md                  source bibliography (problem -> algorithm -> papers)
  README.md                                 public repo README (from origin/main)
  CLAUDE.md                                 this file
  QSVM_DDoS_Said2023.ipynb                  reference notebook 1 (QSVM, Qiskit kernel)
  QuantumNetSec_VQC_DDoS_CICIDS2017.ipynb   reference notebook 2 (VQC/QCNN/QSVC, Qiskit)
  papers/2023_Said_QSVM_DDoS/               older layout from README; same code as root QSVM notebook
  01_Network_Intrusion_Detection/ ... 30_QML_Defences_Against_ML_Attacks/
  _Topic_assignment_unresolved/             12 PDFs (surveys/reviews) with no final topic
```

The 30 topic folders (01 to 30) and `_Topic_assignment_unresolved` already exist and each holds
the PDFs of the papers assigned to it (431 PDFs in total, 327 unique; a paper assigned to two
topics is present in both folders). PDFs are gitignored and must never be committed.
`C:\Users\madji\Desktop\QML.zip` (751 MB) is a backup copy of the same PDFs plus the manifest and
bibliography; do not extract it into the repo.

### Topic folders

| Folder | Folder | Folder |
|---|---|---|
| 01_Network_Intrusion_Detection | 11_Vulnerability_Software_Supply_Chain_Attacks | 21_QKD_Attack_Detection |
| 02_Zero_Day_Attack_Detection | 12_Cryptojacking_Detection | 22_Deepfake_Spoofing_Detection |
| 03_DDoS_DoS_Detection | 13_Encrypted_Malicious_Traffic_Detection | 23_Adversarial_Attacks_Against_QML |
| 04_Botnet_DGA_Detection | 14_IoT_IIoT_Attack_Detection | 24_Poisoning_Attacks_Against_QML |
| 05_Malware_Detection | 15_Smart_Grid_Power_System_Attacks | 25_Backdoor_Trojan_Attacks_Against_QML |
| 06_Android_Malware_Detection | 16_ICS_SCADA_Cyber_Physical_Attacks | 26_QML_Model_Extraction_Theft |
| 07_Ransomware_Detection | 17_Vehicle_CAN_Bus_Attacks | 27_QML_Privacy_Data_Leakage |
| 08_Phishing_Detection | 18_Cloud_Virtual_Environment_Threats | 28_QML_Hardware_Side_Channel_Crosstalk_Attacks |
| 09_Malicious_URL_Detection | 19_Cybersecurity_Anomaly_Detection | 29_Adversarial_Robustness_Defences_for_QML |
| 10_Spam_Detection | 20_Blockchain_Attack_Detection | 30_QML_Defences_Against_ML_Attacks |

### manifest.csv

Columns: `QC-ID`, `Full paper title`, `Year`, `DOI/arXiv URL`,
`Assigned cybersecurity topic folder(s)` (semicolon-separated when more than one),
`PDF filename`, `Download source`, `Download status`.

Reproduction columns (added by `tools/publish_notebook.py`): `Notebook path` (repo-relative),
`Reproduction status`, `Paper metric(s)`, `Notebook metric(s)`, `Validated on` (ISO date),
`Notes` (deviations, data substitutions, open issues). Final statuses, one per paper:
- `reproduced`: notebook executes end to end and every checkable claim is within tolerance.
- `partially reproduced`: executes end to end; some claims not reached / exceeded / uncheckable.
- `implemented but unvalidated`: complete Colab-ready notebook that could not be executed here.
- `blocked`: no notebook (survey/review, no public data or substitute, hardware-only, unreadable
  PDF); the reason is in `Notes`, recorded with `publish_notebook.py --no-notebook`.
An empty status means unprocessed. Queue order (user decision, 2026-10-18): coverage first,
i.e. every topic folder gets at least two implemented notebooks (one where the folder holds a
single paper) before the rest are filled in QC-ID order. `tools/next_papers.py --coverage 2
--index paper_index.csv` lists the folders still short and their best candidates (readable text,
known framework and dataset, not a survey); `tools/next_papers.py` without flags gives QC-ID
order. `REPRODUCTION_QUEUE.md` lists what is in flight. Papers in
`_Topic_assignment_unresolved` are mostly surveys and end up `blocked` unless they contain a
rerunnable experiment.

## Filing rule for every notebook

- One notebook per paper, saved in the paper's **existing** topic folder. For a paper with several
  topics, file it in the **first** folder listed in its manifest row; never duplicate a notebook.
  Coverage exception (2026-10-18): while a later folder in the row still has fewer than two
  implemented notebooks and the first folder already has two or more, file it in that later
  folder (the dispatcher states the target folder in the agent brief).
- File name: `<Method>_<Task>_<FirstAuthorYear>.ipynb`, e.g. `QSVM_DDoS_Said2023.ipynb`,
  `VQC_IntrusionDetection_deAbreu2025.ipynb`. ASCII only, no spaces.
- Update the paper's `manifest.csv` row (notebook path, status, metrics, date, notes) in the
  same commit as the notebook.
- Never create new topic folders. If no folder fits, stop and ask the user.
- The README's `papers/<year>_<author>_<topic>/` layout predates this rule; the topic folders are
  canonical for new work. Reconciling the README is a separate task.

## Reference-notebook conventions (extracted from the two existing notebooks)

Both reference notebooks were created in Google Colab (`nbformat 4.5`, kernel `python3`,
Colab metadata) and follow the same structure. Match it.

**Cell structure**
1. Markdown: Colab badge linking to `https://colab.research.google.com/github/owlmt/QML/blob/main/<path>`.
2. Markdown: title `# <Method> for <task>: <paper> step by step`, full citation (authors, title,
   venue, year, DOI/arXiv), what the notebook does, how to run it (Colab, CPU runtime, Run all), and
   what the reader gets at the end.
3. Markdown: "The paper in one page" (problem, decision, method, data, preprocessing, claims) and,
   where the paper is silent, a table "What follows the paper and what had to be chosen" with
   columns `Item | Paper | This notebook`. Choices are marked `# CHOICE:` in code comments.
4. Code: installs, pinned to tested versions, e.g.
   `!pip -q install "qiskit==2.5.2" "qiskit-machine-learning==0.9.1" "qiskit-aer==0.17.2" "qiskit-ibm-runtime==0.50.0" pylatexenc`
   (Colab already ships numpy, pandas, scikit-learn, matplotlib, tensorflow). Note that a session
   restart may be required.
5. Code: one **configuration cell** with every tunable constant: `SEED = 42`, `N_QUBITS`,
   sample sizes, `TEST_SIZE`, iteration budgets, `SHOTS`, `FAST_MODE` (small budgets for a
   sub-10-minute class demo vs. full run), `DATA_SOURCE` / `DATA_DIR`, optional `IBM_TOKEN = ""`.
6. Code: imports in one cell; `algorithm_globals.random_seed = SEED`,
   `np.random.default_rng(SEED)`, `tf.random.set_seed(SEED)` where relevant; print library versions.
7. Numbered sections that mirror the paper's pipeline, each a markdown explanation followed by a
   short code cell. Sections used so far: data, cleaning/labels, preprocessing, classical baseline,
   quantum feature map, quantum kernel / ansatz, training, metrics (confusion matrix), re-drawing
   the paper's figures/tables, side-by-side comparison with the paper, critical reading, exercises.

**Data loading**
- Public datasets are downloaded inside the notebook (Hugging Face mirrors via `huggingface_hub`
  or `requests`, with a GitHub fallback), cached in `DATA_DIR`, with an `upload`/`path` option.
  Large CSVs are read in chunks (`chunksize=200_000`).
- CICDDoS2019: HF repo `baalajimaestro/CICDDoS2019`; CIC-IDS-2017: HF
  `c01dsnap/CIC-IDS2017` with fallback `StarterArcher/CICIDS2017` (reduced columns).

**Preprocessing**
- Strip column names; drop identifier columns (Flow ID, IPs, ports, timestamps); coerce to
  numeric; replace ±inf with NaN and drop; drop duplicates and constant columns.
- Class-balanced sampling with `random_state=SEED` (quantum simulation limits samples to
  hundreds or a few thousand flows).
- Stratified `train_test_split(..., random_state=SEED)`.
- **Every transform is fitted on the training split only** (`SelectKBest(f_classif)` ->
  `StandardScaler` -> `PCA(n_components=N_QUBITS, random_state=SEED)` ->
  `MinMaxScaler((0, np.pi))`, test angles clipped to `[0, π]`); one feature per qubit.

**Quantum setup (Qiskit 2.x + qiskit-machine-learning 0.9.x, function-style circuit library)**
- Feature maps: `zz_feature_map(n, reps=2, entanglement="linear")`, `z_feature_map`,
  `pauli_feature_map`, `raw_feature_vector`.
- Kernel methods: `FidelityStatevectorKernel(feature_map=...)` with `QSVC`, and the same kernel
  computed by hand (`|<φ(a)|φ(b)>|²` from `Statevector`) fed to `SVC(kernel="precomputed")`,
  checked with `np.allclose`. A kernel **bandwidth** (angle scale) is tuned on a validation split
  of the training data only.
- Variational models: `VQC(feature_map, ansatz, optimizer, sampler, callback)` with
  `real_amplitudes` / `efficient_su2` / `excitation_preserving` / `n_local`, optimisers
  `COBYLA`, `SPSA`, `ADAM`, `GradientDescent`; `AerSampler(default_shots=SHOTS, seed=SEED)`
  (or `StatevectorSampler` for `raw_feature_vector`). QCNN via `EstimatorQNN` +
  `NeuralNetworkClassifier` with conv/pool blocks after the Qiskit QCNN tutorial.
- Noise studies use `qiskit_ibm_runtime.fake_provider` devices; real-hardware cells run only if
  `IBM_TOKEN` is set and are skipped otherwise.
- Live loss plots via a callback that redraws every few evaluations.

**Baselines and metrics**
- Classical baselines (`SVC` linear/RBF with the paper's `C`, `RandomForestClassifier`, small
  Keras CNN) trained on exactly the same inputs as the quantum model, and additionally on all
  features when the paper's input is unknown.
- Metrics as in the paper (accuracy, precision, recall, F1, per-class F1), confusion matrices with
  attack as the positive class, wall-clock training+prediction time, repeated runs over different
  seeds with mean ± std.
- A final code cell prints the paper's numbers next to the notebook's and states per claim
  "reproduced" / "not reached here" / "cannot be checked", followed by a markdown "Reading the
  paper critically" section and student exercises.

## Mandatory sections (user decision, 2026-10-19; apply to every notebook, old and new)

**A. "Dataset Exploration and Visualisation"** (markdown heading with exactly this title, then
code cells whose outputs are kept). For every dataset the notebook actually uses:
- print dataset shape, feature names and the original label values / class counts;
- plot the distribution of the real classes (bar chart);
- a 2-D scatter plot in which every point is a real observation coloured by its ground-truth
  label, modelled on "Training flows, first two angles" in
  `QuantumNetSec_VQC_DDoS_CICIDS2017.ipynb`: first the raw PCA coordinates (fitted on the
  training split), then, where the model uses angle encoding, the same coordinates scaled to
  [0, π];
- keep multiclass attack labels when the data has them (colour by attack family, not just
  binary);
- for images, audio, graphs or time series use a labelled 2-D projection of the real samples
  (PCA/t-SNE of pixels or embeddings, spectrogram-feature PCA, node/edge feature PCA, window
  feature PCA);
- never fabricated data, invented labels or an unrelated dataset.
If the dataset is inaccessible, the section states the blocker (status BLOCKED). For papers with
no dataset at all (theory), the section contains the single line `NOT_APPLICABLE: <reason>`.

**B. "Quantum Circuit Architecture"** (markdown heading with exactly this title). For every
gate-based quantum model that the notebook trains or evaluates:
- draw the circuit object that is actually executed (Qiskit: `circuit.draw("mpl")` or
  `decompose().draw("mpl")` of the executed circuit; PennyLane: `qml.draw_mpl(qnode)(...)` of
  the real QNode; other simulators: a drawing produced from the same gate list the simulator
  runs, with a cell asserting equivalence), showing encoding, parametrised gates, entanglement
  and measurements;
- print qubit count, circuit depth and trainable-parameter count;
- one drawing per distinct architecture when several are compared;
- document every assumption where the paper omits circuit details.
No generic or illustrative circuits. For non-circuit quantum methods (annealing/QUBO, quantum
Boltzmann machines on exact Gibbs states, kernels computed in closed form without a circuit) the
section contains `NOT_APPLICABLE: <reason>`.

Both sections must be executed (outputs present) before a notebook is published; the
verifier (`tools/verify_notebook.py`) checks for the headings and for figure outputs beneath
them. Notebooks lacking real dataset visualisations or actual circuit diagrams are rejected.

**Tracking.** `tools/publish_notebook.py` writes five manifest columns, each PASS / FAIL /
PENDING / BLOCKED / NOT_APPLICABLE: `dataset_visualisation_status`, `class_scatter_status`,
`quantum_circuit_visualisation_status`, `visualisation_validation_status` (PASS only with
execution evidence) and `retrospective_audit_status`. Notebooks published before 2026-10-19
carry PENDING until the retrospective audit (below) upgrades them.

**Retrospective audit.** After the 327-paper queue is complete, every earlier notebook is
inspected: missing sections are added, the new cells executed, previous results and methodology
preserved, identical copies across folders synchronised, manifest/log updated, and the correction
committed and pushed. Compliance is verified by content (real observations, ground-truth labels,
executable circuit), never assumed from the presence of a plot.

## Scientific validation requirements (a notebook is "validated" only when all hold)

1. Executes top to bottom from a clean Colab CPU session (Runtime -> Run all) without errors;
   `FAST_MODE` path finishes in about 10 minutes, full path is documented with its runtime.
2. Random seeds fixed everywhere (`SEED`, scikit-learn `random_state`, `algorithm_globals`,
   sampler/transpiler seeds, TensorFlow).
3. Installs are Colab-compatible and pinned to versions actually tested; no local-only paths.
4. Every reported metric of the paper that the notebook can test is computed and shown side by
   side with the paper's value; each claim gets an explicit verdict.
5. Every deviation from the paper (dataset substitute, qubit count, sample size, missing
   hyper-parameters) is documented in the "Paper vs this notebook" table and in `# CHOICE:` comments.
6. No test-set leakage: all fitting on training data only; bandwidth/hyper-parameters chosen on a
   validation split.
7. A classical baseline on identical inputs is included.
8. Outputs are kept in the committed notebook only if they are small (figures OK, no multi-MB
   dumps); large outputs are cleared.

## Tools (in `tools/`, run with the project venv `.venv\Scripts\python.exe`)

- `tools/pdf_text.py <pdf> [--pages a-b] [--out file]` extracts paper text (PDF page rendering
  is not available on this machine).
- `tools/execute_notebook.py <nb> --timeout S --cwd <scratch dir>` runs every code cell with
  nbclient, prints per-cell timing, writes outputs back into the notebook, exits 1 on any error.
  Always point `--cwd` at a scratch directory outside the repo so downloaded data never lands
  in the working tree.
- `tools/publish_notebook.py --qc QC-xxx --notebook <repo path> --status <status>
  --paper-metrics "..." --notebook-metrics "..." --notes "..."` updates the manifest row (adding
  the reproduction columns on first use), appends to `REPRODUCTION_LOG.md`, stages only those
  files, commits, pushes to origin main, fetches and verifies the commit is on origin/main, and
  prints the GitHub and Colab URLs. Use `--dry-run` to only update manifest/log.
- Progress is persisted in `manifest.csv` (columns `Notebook path`, `Reproduction status`, ...)
  and `REPRODUCTION_LOG.md`; a new session resumes by reading those.

## Publication workflow (one commit and push per validated notebook)

1. Execute the notebook with `tools/execute_notebook.py` until it passes; check the metrics
   against the paper; confirm the validation list above.
2. `git status` must show only the notebook (plus manifest/log). Never stage PDFs, datasets,
   `*.zip`, credentials, checkpoints or experiment outputs (see `.gitignore`).
3. Run `tools/publish_notebook.py` (it adds, commits, pushes and verifies). Publication is
   claimed only when the script reports `verified on origin/main`.
4. Do not rewrite history, force-push, change branch permissions, or overwrite files that exist on
   origin with different content. If any of these would be needed, stop and ask the user.
5. Several notebooks may be written in parallel (one agent per paper, briefed with
   `tools/AGENT_BRIEF.md`; about three at a time on this machine), but publishing runs one at a
   time from this checkout. The dispatcher re-verifies every notebook (no error outputs, all code
   cells executed, figures present, size) before publishing.
6. Resume after an interruption: `tools/next_papers.py --status` shows counts and the next
   unprocessed QC-IDs; `REPRODUCTION_QUEUE.md` shows which papers were in flight (check whether
   their notebook files exist and re-validate them before publishing).

## Tooling notes (as of 2026-10-17)

- `git 2.54` with Git Credential Manager; `gh` CLI is **not installed**. A GitHub credential for
  `owlmt` is stored, so `git push origin main` works non-interactively. If a push ever fails with
  "Cannot prompt", run it from an interactive terminal so the credential manager can sign in again.
- Default `python` is 3.12.10 with numpy, pandas, scikit-learn, scipy, matplotlib, but **no**
  jupyter/nbformat/nbconvert/qiskit/pennylane. Python 3.10 (`py -3.10`) has an old qiskit 0.38
  and nbformat/nbconvert; it is not suitable for Qiskit 2.x notebooks. Local execution needs a
  dedicated environment (ask before installing). Colab remains the reference execution target.
- On this machine the Git Bash tool may fail to fork; prefer PowerShell for commands. Use
  `python -X utf8` when printing notebook text (console is cp1252).

## Cost policy (user decision, 2026-10-18)

- The user runs on a fixed subscription allowance: never enable pay-as-you-go, buy credits or
  upgrade. If a model's limit is hit, switch new work to an included model or pause until the
  allowance resets; running notebook executions keep going and are picked up on resume.
- Notebook-writing agents run on the cheapest suitable model (`sonnet`); pure feasibility checks
  (likely surveys) on `haiku`. The dispatcher (Fable) only verifies, publishes, dispatches and
  decides genuinely hard scientific questions.
- Checks are deterministic code (`tools/verify_notebook.py`, `tools/next_papers.py`), not extra
  model calls. Never re-run or regenerate a notebook that already has a final status.

## Hard rules

- Do not touch `C:\Users\madji\Downloads\postq` or any other repository.
- Never commit PDFs, datasets, archives, credentials, temp files or large outputs.
- Never run `git reset --hard`, `git clean`, `git push --force`, or a checkout that replaces an
  existing local file.
- Ask before installing packages, changing repo permissions, or altering the folder structure.
