# Brief for a notebook-writing agent (one paper per agent)

You are building one reproduction notebook for the "QML × Cybersecurity Colab Reproduction
Factory" in the git repo `C:\Users\madji\Desktop\QML`. The dispatcher gives you a QC-ID. Read
`CLAUDE.md` first and follow its notebook conventions exactly. Do NOT commit, push, or touch
`manifest.csv`, `REPRODUCTION_LOG.md` or `REPRODUCTION_QUEUE.md`; create only your one notebook
(plus scratch files outside the repo). Do not touch `C:\Users\madji\Downloads\postq`.

## Environment

- The Bash tool fails to fork on this machine: use the PowerShell tool. A PowerShell
  `run_in_background` command is killed after 10 minutes, so launch long notebook executions as a
  detached process (`Start-Process ... -RedirectStandardOutput <log>`) and poll the log.
- Python: `C:\Users\madji\Desktop\QML\.venv\Scripts\python.exe` (qiskit 2.5.2,
  qiskit-machine-learning 0.9.1, qiskit-aer 0.17.2, qiskit-ibm-runtime 0.50.0, pennylane 0.45.1 +
  lightning, nbformat, nbclient, pandas, scikit-learn, matplotlib, seaborn, requests,
  huggingface_hub, ucimlrepo, xgboost, imbalanced-learn, pypdf). TensorFlow and PyTorch are not
  installed; install `tensorflow-cpu` or CPU `torch` into the venv with pip only if the paper's
  method needs it (the user approved necessary dependencies). Console is cp1252: run python with
  `-X utf8` and set `$env:PYTHONIOENCODING='utf-8'`.
- Scratch root: `C:\Users\madji\AppData\Local\Temp\claude\C--Users-madji-Desktop-QML\45437630-f2c2-4728-9da2-ce4bbdd7c4ba\scratchpad`.
  Put builder scripts in `<scratch>\build_<qcid>\` and all downloaded data in
  `<scratch>\run_<qcid>\` (pass it as `--cwd` when executing). Never write data inside the repo.
- Paper text (already extracted): `<scratch>\paper_text\<QC-ID>.txt`. If it is nearly empty
  (scanned PDF), try `tools/pdf_text.py` on the PDF; if still empty, the paper is blocked
  (unreadable) and you report that.
- Manifest row: `Import-Csv manifest.csv | Where-Object { $_.'QC-ID' -eq '<QC-ID>' } | Format-List`
  gives title, year, DOI, topic folder(s) and PDF filename (first author surname is in it).
- Other agents are executing notebooks at the same time; CPU is shared. Keep FAST_MODE small.
  Never stop or kill a python/ipykernel process you did not start yourself: record the PID that
  your own `Start-Process` returns and only ever act on that PID. Never use `Get-Process python |
  Stop-Process` or kill by name.
- Published examples to imitate (dump cells with a small python script, never Read the raw
  .ipynb): `03_DDoS_DoS_Detection/QSVM_DDoS_Said2023.ipynb`,
  `08_Phishing_Detection/VQC_PhishingURL_Shahriyar2025.ipynb`,
  `01_Network_Intrusion_Detection/QSVM_IntrusionDetection_Tiwari2026.ipynb`.

## Step 1: feasibility decision (report "blocked" instead of building when true)

- Survey, review, taxonomy, position or purely theoretical paper with no experiment to rerun.
- Experiment needs data that is not publicly downloadable (private captures, paid datasets,
  Kaggle-login-only data with no mirror) and no reasonable public substitute exists.
- Needs real quantum hardware, a D-Wave annealer, or proprietary software with no simulator path.
- PDF text unreadable.
For any of these, stop and report `blocked: <reason>` with one paragraph of evidence. Everything
else gets a notebook. A public substitute dataset is allowed and must be documented.

## Step 2: build the notebook

- Path: `<first topic folder from the manifest row>/<Method>_<Task>_<FirstAuthorYear>.ipynb`
  (ASCII, e.g. `VQC_Phishing_Shahriyar2025.ipynb`; Method = QSVM, VQC, QNN, QCNN, QLSTM, QGAN,
  QAE, QAOA, HybridQNN, ...; Task = short task word). Never create new folders.
- Build with `nbformat.v4.new_markdown_cell/new_code_cell` (cells get ids). Colab badge in cell 0
  must point at `https://colab.research.google.com/github/owlmt/QML/blob/main/<path>`.
- Follow CLAUDE.md: citation header; "The paper in one page"; "What follows the paper and what had
  to be chosen" table (`Item | Paper | This notebook`) with every unspecified item marked
  `# CHOICE:` in code; pinned Colab install cell guarded so it does not reinstall locally
  (`if IN_COLAB or <import fails>`); single config cell (`SEED = 42`, `FAST_MODE`, sizes, budgets,
  `DATA_DIR`, optional `IBM_TOKEN = ""`); imports with versions printed; seeds everywhere
  (`algorithm_globals.random_seed`, `np.random.default_rng`, sampler/transpiler seeds, framework
  seeds); data downloaded inside the notebook from public URLs with a fallback, cached in
  `DATA_DIR`; every transform fitted on the training split only; quantum model as the paper
  describes (Qiskit 2.x function-style circuit library or PennyLane as the paper uses); classical
  baselines (at least RandomForest and SVC(rbf)) on the identical reduced inputs, plus whatever the
  paper compares against; metrics as in the paper with confusion matrices and timings; mean ± std
  over several seeds where cheap; final comparison DataFrame paper-vs-notebook with a verdict per
  claim ("reproduced" within 2 accuracy points / 0.02 F1, otherwise "not reached" or "exceeded"
  with the gap, "cannot be checked" when unverifiable); "Reading the paper critically"; 5 exercises.
- `FAST_MODE=True` must finish in under 10 minutes locally; `FAST_MODE=False` follows the paper's
  budgets as far as a CPU simulator allows (state the budgets).
- MANDATORY (2026-10-19), see CLAUDE.md "Mandatory sections": a markdown heading
  `## Dataset Exploration and Visualisation` followed by code that prints shape / feature names /
  original labels and class counts, plots the real class distribution, and draws a 2-D scatter of
  real observations coloured by ground-truth label (raw PCA coordinates fitted on the training
  split, then the [0, π]-scaled angles when angle encoding is used; keep multiclass attack labels;
  labelled projections for images/audio/graphs/time series); and a markdown heading
  `## Quantum Circuit Architecture` followed by a drawing of the circuit actually executed
  (`circuit.draw("mpl")` in Qiskit, `qml.draw_mpl(qnode)` in PennyLane, or a drawing generated
  from the simulator's own gate list with an equivalence assertion), one per distinct
  architecture, plus printed qubit count, depth and trainable-parameter count. Where a section
  does not apply, put the single line `NOT_APPLICABLE: <reason>` under the heading. Both sections
  must have executed outputs; the dispatcher rejects notebooks without them.

## Step 3: execute and validate

- `& .venv\Scripts\python.exe tools\execute_notebook.py <path> --timeout 3600 --cwd <scratch>\run_<qcid>`
  with FAST_MODE=True; fix errors until it passes.
- Then set FAST_MODE=False in the source and execute again (detached). If the full run would
  exceed about 90 minutes or fails on resources, commit the FAST_MODE=True executed version and say
  so. The committed notebook must contain outputs from a complete, error-free run.
- Check: no error outputs, every code cell has an execution_count, image/png outputs present,
  file under 4 MB (strip bulky outputs if needed), badge path equals file name.
- If the notebook cannot be executed locally at all (e.g. it needs a library that cannot be
  installed here) but is complete and Colab-ready, report status `implemented but unvalidated`
  with the reason.

## Step 4: report back (concise, this exact structure)

```
QC-ID: ...
STATUS: reproduced | partially reproduced | implemented but unvalidated | blocked
NOTEBOOK: <repo-relative path or none>
MODE/TIME: FAST_MODE=<True/False> executed, <minutes> min
DATASET: <what was used, substitutions>
PAPER METRICS: <numbers with table/figure refs>
NOTEBOOK METRICS: <numbers>
VERDICTS: <per claim>
DEVIATIONS: <choices and problems>
VISUALISATION: dataset section <PASS|BLOCKED|NOT_APPLICABLE>, class scatter <PASS|...>, circuit section <PASS|NOT_APPLICABLE> (with the figure counts)
```
The dispatcher verifies the file and publishes it; you never commit.
