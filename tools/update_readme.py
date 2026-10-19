"""Regenerate README.md from manifest.csv so the repository front page stays current.

Usage: python tools/update_readme.py
The static introduction lives in this file; the per-folder tables are built from the manifest
(every row with a notebook path) and the blocked list from rows with status "blocked".
"""
import csv
import datetime as dt
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "manifest.csv"
README = REPO / "README.md"
WEB = "https://github.com/owlmt/QML/blob/main/"
COLAB = "https://colab.research.google.com/github/owlmt/QML/blob/main/"
IMPLEMENTED = {"reproduced", "partially reproduced", "implemented but unvalidated"}

INTRO = """# QML × Cybersecurity Colab Reproduction Factory

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
"""


def main() -> int:
    with MANIFEST.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    by_folder = defaultdict(list)
    blocked = []
    counts = Counter()
    for r in rows:
        status = r.get("Reproduction status", "")
        counts[status or "unprocessed"] += 1
        nb = r.get("Notebook path", "")
        if status in IMPLEMENTED and nb:
            by_folder[nb.split("/")[0]].append(r)
        elif status == "blocked":
            blocked.append(r)
    folders = sorted({t.strip() for r in rows for t in r["Assigned cybersecurity topic folder(s)"].split(";")})

    out = [INTRO]
    done = sum(v for k, v in counts.items() if k != "unprocessed")
    out.append(f"\n## Progress ({dt.date.today().isoformat()})\n")
    out.append(f"{done} of {len(rows)} papers have a final status: "
               + ", ".join(f"{counts[k]} {k}" for k in ("reproduced", "partially reproduced",
                                                        "implemented but unvalidated", "blocked") if counts[k])
               + f"; {counts['unprocessed']} still to process. "
               f"{sum(len(v) for v in by_folder.values())} notebooks are published across "
               f"{len(by_folder)} of the 30 topic folders.\n")

    out.append("\n## Notebooks by topic\n")
    for folder in folders:
        if folder.startswith("_"):
            continue
        items = by_folder.get(folder, [])
        n_papers = sum(1 for r in rows if folder in [t.strip() for t in r["Assigned cybersecurity topic folder(s)"].split(";")])
        out.append(f"\n### {folder.replace('_', ' ')}  ({len(items)} of {n_papers} papers)\n")
        if not items:
            out.append("\n_No notebook yet._\n")
            continue
        out.append("\n| QC-ID | Paper | Year | Notebook | Status |\n|---|---|---|---|---|\n")
        for r in sorted(items, key=lambda x: x["QC-ID"]):
            nb = r["Notebook path"]
            name = nb.split("/")[-1].replace(".ipynb", "")
            title = r["Full paper title"].replace("|", "/")
            doi = r.get("DOI/arXiv URL", "")
            title_md = f"[{title}]({doi})" if doi.startswith("http") else title
            out.append(f"| {r['QC-ID']} | {title_md} | {r['Year']} | "
                       f"[{name}]({WEB}{nb}) · [Colab]({COLAB}{nb}) | {r['Reproduction status']} |\n")
    if blocked:
        out.append("\n## Papers without a notebook (blocked)\n\n| QC-ID | Paper | Reason |\n|---|---|---|\n")
        for r in sorted(blocked, key=lambda x: x["QC-ID"]):
            reason = re.sub(r"\s+", " ", r.get("Notes", ""))[:160]
            out.append(f"| {r['QC-ID']} | {r['Full paper title'].replace('|', '/')} | {reason} |\n")
    out.append("\n## Rules for adding a notebook\n\n"
               "See `CLAUDE.md`: one notebook per paper in its topic folder, public data downloaded\n"
               "inside the notebook, every transform fitted on the training split only, a classical\n"
               "baseline on identical inputs, a claim-by-claim comparison with the paper, the two\n"
               "mandatory visualisation sections, and a manifest row updated in the same commit.\n")
    README.write_text("".join(out), encoding="utf-8")
    print(f"README.md regenerated: {done} final, {sum(len(v) for v in by_folder.values())} notebooks listed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
