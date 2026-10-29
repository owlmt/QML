"""Regenerate README.md from manifest.csv so the repository front page stays current.

Usage: python tools/update_readme.py
The static introduction lives in this file; every count, the per-folder tables, the list of
papers without code and the list of blocked papers are computed from the manifest, so the
README can never disagree with it.

Counting rules (2026-10-27 consistency audit):
- A catalogue entry is one manifest row (one QC-ID). Repository-wide totals count each entry
  once. A paper assigned to several topic folders appears in each folder's catalogue count but
  its notebook is listed only under the folder that holds it; the other folders cross-reference
  it. Folder catalogue counts therefore add up to more than the repository-wide total.
- "with code": the row has a notebook (status reproduced, partially reproduced or implemented
  but unvalidated).
- "paper without code": no notebook because the publication itself has no rerunnable
  experiment (survey, review, taxonomy, perspective, extended abstract, architecture-only paper).
- "blocked": no notebook although the paper has an experiment, because its data or the article
  itself is inaccessible (reason in the manifest Notes).
- DUPLICATES lists entries that are another version of an entry already in the catalogue; they
  are kept (never removed) and counted once in the number of distinct publications.
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
NO_CODE = "paper without code"
BLOCKED = "blocked"
UNRESOLVED = "Topic assignment unresolved"
# entry -> the entry it duplicates (same publication, another arXiv version); both are kept
DUPLICATES = {"QC-215": "QC-051"}

INTRO = """# QML × Cybersecurity Colab Reproduction Factory

This repository reproduces published **quantum machine learning (QML) papers in cybersecurity**
as teaching notebooks: one Google Colab notebook per paper, filed into 30 cybersecurity topic
folders. Every notebook downloads its own public data, rebuilds the paper's method step by step
with plain-language explanations, trains a classical baseline on the same inputs, compares its
own numbers with the paper's claim by claim, and ends with a critical reading and exercises.

The paper catalogue (`manifest.csv`, {n_rows} entries) comes from the bibliography in
`original_bibliography.md` plus six papers added in October 2026. Reproductions are produced by
an automated pipeline (see `CLAUDE.md`), executed end to end on a CPU before publication, and
recorded with a truthful status:

| Status | Meaning |
|---|---|
| reproduced | notebook executes end to end and every checkable claim is within tolerance |
| partially reproduced | executes end to end; some claims not reached, exceeded or uncheckable |
| implemented but unvalidated | complete Colab-ready notebook that could not be executed locally |
| paper without code | no notebook: the publication is a survey, review, taxonomy, perspective, extended abstract or architecture-only paper with no rerunnable experiment of its own |
| blocked | no notebook: the paper has an experiment, but its data or the article itself is inaccessible (reason in the manifest) |

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
REPRODUCTION_QUEUE.md        dispatch policy and the state of the (completed) queue
paper_index.csv              feasibility index (datasets, frameworks, models) per paper
CLAUDE.md                    conventions, validation requirements, publication workflow
tools/                       execution, verification, publication and queue scripts
01_... to 30_...             topic folders; each holds the notebooks of its papers
```

Paper PDFs are not distributed. Two early reference notebooks remain at the repository root
(`QSVM_DDoS_Said2023.ipynb`, `QuantumNetSec_VQC_DDoS_CICIDS2017.ipynb`); their reproductions
live in the topic folders.
"""

ATLAS = """
## Cybersecurity Dataset Atlas (folder 00)

`00_Cybersecurity_Dataset_Atlas/QML_Cybersecurity_Dataset_Atlas.ipynb`
([open in Colab](https://colab.research.google.com/github/owlmt/QML/blob/main/00_Cybersecurity_Dataset_Atlas/QML_Cybersecurity_Dataset_Atlas.ipynb))
is a companion notebook that documents every dataset the reproductions use, plus the standard
cybersecurity collections of the original catalogue: more than one hundred datasets across
network intrusion, DDoS, botnets and DGA, IoT/IIoT, smart grid and ICS, malware, Android, phishing,
URLs and spam, vehicle CAN bus, host and cloud logs, audio deepfakes and the benchmark sets used by
the QML-attack papers. For each dataset it shows real observations coloured by their ground-truth
labels (raw PCA and the same coordinates as qubit angles in [0, π]), the class distribution, the
feature table, the original reference and licence, the download source, and the use cases: which
topic folders and which reproduced papers (QC-IDs with notebook links) use it. The access status of
every dataset is verified by an actual download (`public`, `large` for FULL mode only, `gated` or
`page_only` when a registration form stands in the way, `simulated` when a paper generates its own
data). `00_Cybersecurity_Dataset_Atlas/atlas_inventory.csv` is the machine-readable inventory and
`atlas_usage.csv` (regenerated by `tools/atlas_usage.py`) the dataset-to-notebook map.
"""

CITE = """
## How to cite

If you use a notebook, the dataset atlas or the manifest, please cite the repository
(`CITATION.cff` carries the same metadata for GitHub's "Cite this repository" button):

> Madjid G. Tehrani (2026). *QML × Cybersecurity: reproducible notebooks of quantum machine
> learning papers and a cybersecurity dataset atlas.* Edinburgh Napier University.
> https://github.com/owlmt/QML

```bibtex
@misc{tehrani2026qmlcyber,
  author       = {Tehrani, Madjid G.},
  title        = {QML x Cybersecurity: reproducible notebooks of quantum machine learning papers and a cybersecurity dataset atlas},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\\url{https://github.com/owlmt/QML}},
  note         = {Edinburgh Napier University. Cite the dataset atlas as folder 00\\_Cybersecurity\\_Dataset\\_Atlas and an implemented paper as its notebook path.}
}
```

When citing a single reproduction, add the notebook path (for example
`03_DDoS_DoS_Detection/QSVM_DDoS_Said2023.ipynb`) and cite the original paper as well; when citing a
dataset shown in the atlas, cite the dataset's own reference given on its atlas card in addition to
this repository.
"""

LICENSING = """
## Licensing

This repository combines material under three licences; `LICENSING.md` gives the full scope,
`COPYRIGHT.md` the ownership and `CONTRIBUTING.md` the terms for contributions. In short:

| Material | Licence | SPDX |
|---|---|---|
| Source code: `tools/`, helper scripts and the **code cells** of every notebook | GNU Affero General Public License v3.0 only (`LICENSE`) | `AGPL-3.0-only` |
| Original educational content: notebook **markdown cells**, explanations, documentation, original figures | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (`LICENSES/CC-BY-NC-SA-4.0.txt`) | `CC-BY-NC-SA-4.0` |
| The owner's original contributions to the catalogue (`manifest.csv`, `paper_index.csv`, the atlas CSVs) | Creative Commons Attribution 4.0 (`LICENSES/CC-BY-4.0.txt`) | `CC-BY-4.0` |

The root `LICENSE` file covers the source code only, not the whole repository. The papers, datasets
and software libraries the notebooks use are third-party works under their own terms and are not
covered by any of these licences (details in `LICENSING.md`, section 5). AGPL permits commercial use
of the code subject to its conditions; CC BY-NC-SA does not permit commercial use of the
educational content, for which separate commercial licences are available from the copyright holder.
Citation (above) and licensing are separate matters: the licences set the legal terms of reuse,
the citation request is academic practice.
"""


def folders_of(row):
    return [t.strip() for t in row["Assigned cybersecurity topic folder(s)"].split(";") if t.strip()]


def folder_label(folder):
    return folder.replace("_", " ")


def link_title(row):
    title = row["Full paper title"].replace("|", "/")
    url = row.get("DOI/arXiv URL", "").strip()
    return f"[{title}]({url})" if url.startswith("http") else title


def plural(n, word):
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def main() -> int:
    with MANIFEST.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    by_id = {r["QC-ID"]: r for r in rows}
    counts = Counter((r.get("Reproduction status") or "unprocessed") for r in rows)
    with_code = [r for r in rows if r["Reproduction status"] in IMPLEMENTED and r["Notebook path"]]
    no_code = [r for r in rows if r["Reproduction status"] == NO_CODE]
    blocked = [r for r in rows if r["Reproduction status"] == BLOCKED]
    unprocessed = counts.get("unprocessed", 0)
    inconsistent = [r["QC-ID"] for r in rows
                    if (r["Reproduction status"] in IMPLEMENTED) != bool(r["Notebook path"])]
    if inconsistent:
        raise SystemExit(f"status/notebook mismatch for {inconsistent}")
    missing_links = [r["QC-ID"] for r in no_code + blocked if not r["DOI/arXiv URL"].strip().startswith("http")]
    if missing_links:
        raise SystemExit(f"papers without code must link to their publication: {missing_links}")
    n_distinct = len(rows) - sum(1 for q in DUPLICATES if q in by_id)

    by_folder = defaultdict(list)
    for r in with_code:
        by_folder[r["Notebook path"].split("/")[0]].append(r)
    for r in with_code:
        if r["Notebook path"].split("/")[0] not in folders_of(r):
            raise SystemExit(f"{r['QC-ID']} notebook folder not in its assigned folders")
    folders = sorted({t for r in rows for t in folders_of(r) if t != UNRESOLVED})

    out = [INTRO.format(n_rows=len(rows)), ATLAS, CITE, LICENSING]

    # ---- collection status -------------------------------------------------------------
    out.append(f"\n## Collection status ({dt.date.today().isoformat()})\n\n")
    if unprocessed:
        out.append(f"{unprocessed} entries are still being processed.\n\n")
    else:
        out.append("Processing of the catalogue is complete: every entry has a final status.\n\n")
    dup_note = ""
    if DUPLICATES:
        pairs = ", ".join(f"{a} is another version of {b}" for a, b in DUPLICATES.items() if a in by_id)
        dup_note = f" ({pairs}; both entries and their notebooks are kept)"
    out.append(f"- **{len(rows)} catalogue entries**, describing {n_distinct} distinct publications{dup_note}.\n")
    status_bits = ", ".join(f"{counts[k]} {k}" for k in ("reproduced", "partially reproduced",
                                                        "implemented but unvalidated") if counts[k])
    out.append(f"- **{len(with_code)} papers with code**: one executed notebook each ({status_bits}), "
               f"filed across {len(by_folder)} of the 30 topic folders.\n")
    out.append(f"- **{len(no_code)} papers without code**: surveys, reviews, taxonomies, perspectives, "
               f"extended abstracts or architecture-only papers with no rerunnable experiment "
               f"(listed with links below).\n")
    out.append(f"- **{len(blocked)} papers blocked** by inaccessible data or an inaccessible article "
               f"(listed with links below).\n")
    out.append("\nCounting rule: every entry is counted once in the totals above. A paper assigned to "
               "several topic folders is counted in each folder's catalogue figure below, but its "
               "notebook is listed only under the folder that holds it; the other folders "
               "cross-reference it. Folder figures therefore add up to more than the totals above.\n")

    # ---- per-folder tables -------------------------------------------------------------
    out.append("\n## Notebooks by topic\n")
    for folder in folders:
        items = sorted(by_folder.get(folder, []), key=lambda x: x["QC-ID"])
        assigned = [r for r in rows if folder in folders_of(r)]
        elsewhere = sorted((r for r in assigned if r["Notebook path"]
                            and not r["Notebook path"].startswith(folder + "/")), key=lambda x: x["QC-ID"])
        f_nocode = [r for r in assigned if r["Reproduction status"] == NO_CODE]
        f_blocked = [r for r in assigned if r["Reproduction status"] == BLOCKED]
        out.append(f"\n### {folder_label(folder)}\n\n")
        parts = [f"{plural(len(items), 'notebook')} filed here"]
        if elsewhere:
            refs = ", ".join(f"{r['QC-ID']} (in {r['Notebook path'].split('/')[0][:2]})" for r in elsewhere)
            parts.append(f"{len(elsewhere)} with the notebook filed in another folder: {refs}")
        if f_nocode:
            parts.append(f"{plural(len(f_nocode), 'paper')} without code ({', '.join(r['QC-ID'] for r in f_nocode)})")
        if f_blocked:
            parts.append(f"{plural(len(f_blocked), 'paper')} blocked ({', '.join(r['QC-ID'] for r in f_blocked)})")
        out.append(f"{plural(len(assigned), 'paper')} catalogued in this topic: " + "; ".join(parts) + ".\n")
        if not items:
            continue
        out.append("\n| QC-ID | Paper | Year | Notebook | Status |\n|---|---|---|---|---|\n")
        for r in items:
            nb = r["Notebook path"]
            name = nb.split("/")[-1].replace(".ipynb", "")
            out.append(f"| {r['QC-ID']} | {link_title(r)} | {r['Year']} | "
                       f"[{name}]({WEB}{nb}) · [Colab]({COLAB}{nb}) | {r['Reproduction status']} |\n")

    unresolved = [r for r in rows if UNRESOLVED in folders_of(r)]
    if unresolved:
        out.append(f"\n### {UNRESOLVED}\n\n")
        u_nocode = sum(1 for r in unresolved if r["Reproduction status"] == NO_CODE)
        u_blocked = sum(1 for r in unresolved if r["Reproduction status"] == BLOCKED)
        u_code = [r for r in unresolved if r["Notebook path"]]
        bits = []
        if u_nocode:
            bits.append(f"{u_nocode} without code")
        if u_blocked:
            bits.append(f"{u_blocked} blocked")
        if u_code:
            bits.append("with code: " + ", ".join(f"{r['QC-ID']} (in {r['Notebook path'].split('/')[0][:2]})" for r in u_code))
        out.append(f"{plural(len(unresolved), 'paper')} catalogued without a final topic folder "
                   f"(surveys and reviews spanning several topics): " + "; ".join(bits) + ".\n")

    # ---- papers without code / blocked ---------------------------------------------------
    def table(title, intro, items):
        out.append(f"\n## {title}\n\n{intro}\n\n| QC-ID | Paper | Year | Topic folder(s) | Reason |\n|---|---|---|---|---|\n")
        for r in sorted(items, key=lambda x: x["QC-ID"]):
            reason = re.sub(r"\s+", " ", r.get("Notes", "")).replace("|", "/")
            if len(reason) > 220:
                reason = reason[:217].rstrip() + "..."
            topics = "; ".join(t[:2] if t != UNRESOLVED else "unresolved" for t in folders_of(r))
            out.append(f"| {r['QC-ID']} | {link_title(r)} | {r['Year']} | {topics} | {reason} |\n")

    if no_code:
        table(f"Papers without code ({len(no_code)})",
              "These publications are part of the catalogue but provide no experiment that can be "
              "implemented: surveys, systematic reviews, taxonomies, perspectives, an extended abstract "
              "and an architecture-only paper. Each links to its original publication (DOI, arXiv or "
              "publisher page); the manifest keeps its full bibliographic row. They are catalogued, not "
              "unfinished work.", no_code)
    if blocked:
        table(f"Papers blocked by inaccessible data or source ({len(blocked)})",
              "These papers describe an experiment, but it cannot be rerun here: the dataset needs a "
              "login with no public mirror, the data are private, or the article itself could not be "
              "obtained. Each can be built if the missing file is supplied (details in the manifest).",
              blocked)

    out.append("\n## Rules for adding a notebook\n\n"
               "See `CLAUDE.md`: one notebook per paper in its topic folder, public data downloaded\n"
               "inside the notebook, every transform fitted on the training split only, a classical\n"
               "baseline on identical inputs, a claim-by-claim comparison with the paper, the two\n"
               "mandatory visualisation sections, and a manifest row updated in the same commit.\n")
    README.write_text("".join(out), encoding="utf-8")
    print(f"README.md regenerated: {len(rows)} entries, {n_distinct} distinct publications, "
          f"{len(with_code)} with code ({len(by_folder)} folders), {len(no_code)} without code, "
          f"{len(blocked)} blocked, {unprocessed} unprocessed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
