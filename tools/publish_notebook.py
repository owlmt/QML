"""Record a validated notebook in manifest.csv, commit it with the manifest, push, and verify.

Usage:
    python tools/publish_notebook.py --qc QC-033 --notebook 03_DDoS_DoS_Detection/QSVM_DDoS_Said2023.ipynb
        --status reproduced --paper-metrics "acc 99.9%" --notebook-metrics "acc 99.9%"
        --notes "..." [--extra PATH ...] [--no-push] [--dry-run]

Steps: update/add the manifest row (adding the reproduction columns if missing), append a line
to REPRODUCTION_LOG.md, `git add` only the notebook, manifest, log and any --extra paths,
commit, push to origin main, then `git fetch` and check that origin/main contains the commit.
Prints the commit hash and the GitHub/Colab URLs. Refuses to touch anything that git ignores.
"""
import argparse
import csv
import datetime as dt
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "manifest.csv"
LOG = REPO / "REPRODUCTION_LOG.md"
REMOTE_WEB = "https://github.com/owlmt/QML"
QA_COLUMNS = ["dataset_visualisation_status", "class_scatter_status",
              "quantum_circuit_visualisation_status", "visualisation_validation_status",
              "retrospective_audit_status"]
NEW_COLUMNS = ["Notebook path", "Reproduction status", "Paper metric(s)",
               "Notebook metric(s)", "Validated on", "Notes", *QA_COLUMNS]
QA_VALUES = {"PASS", "FAIL", "PENDING", "BLOCKED", "NOT_APPLICABLE"}
STATUSES = {"not started", "in progress", "reproduced", "partially reproduced",
            "implemented but unvalidated", "blocked", "not reproducible"}


def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True, encoding="utf-8")
    if check and r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed:\n{r.stdout}\n{r.stderr}")
    return r.stdout.strip()


def update_manifest(qc, nb_rel, status, paper_m, nb_m, notes, today, qa=None):
    raw = MANIFEST.read_bytes()
    newline = "\r\n" if b"\r\n" in raw else "\n"
    with MANIFEST.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)
    for col in NEW_COLUMNS:
        if col not in fieldnames:
            fieldnames.append(col)
    hit = None
    for row in rows:
        for col in NEW_COLUMNS:
            row.setdefault(col, "")
        if row["QC-ID"] == qc:
            hit = row
    if hit is None:
        raise SystemExit(f"{qc} not found in manifest.csv")
    hit["Notebook path"] = nb_rel
    hit["Reproduction status"] = status
    hit["Paper metric(s)"] = paper_m
    hit["Notebook metric(s)"] = nb_m
    hit["Validated on"] = today
    hit["Notes"] = notes
    for col, val in (qa or {}).items():
        hit[col] = val
    with MANIFEST.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator=newline)
        w.writeheader()
        w.writerows(rows)
    return hit


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--qc", required=True)
    ap.add_argument("--notebook", default="", help="repo-relative notebook path (omit with --no-notebook)")
    ap.add_argument("--no-notebook", action="store_true",
                    help="record a status (e.g. blocked) in the manifest without a notebook")
    ap.add_argument("--status", required=True, choices=sorted(STATUSES))
    ap.add_argument("--paper-metrics", default="")
    ap.add_argument("--notebook-metrics", default="")
    ap.add_argument("--notes", default="")
    ap.add_argument("--extra", nargs="*", default=[], help="additional repo-relative paths to commit")
    ap.add_argument("--viz", default=None, choices=sorted(QA_VALUES),
                    help="dataset_visualisation_status (default: NOT_APPLICABLE for blocked papers, else PENDING)")
    ap.add_argument("--scatter", default=None, choices=sorted(QA_VALUES), help="class_scatter_status")
    ap.add_argument("--circuit", default=None, choices=sorted(QA_VALUES), help="quantum_circuit_visualisation_status")
    ap.add_argument("--viz-validated", default=None, choices=sorted(QA_VALUES),
                    help="visualisation_validation_status (PASS only with execution evidence)")
    ap.add_argument("--audit", default=None, choices=sorted(QA_VALUES), help="retrospective_audit_status")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="update manifest/log only, no git")
    args = ap.parse_args()

    nb_rel = args.notebook.replace("\\", "/")
    if args.no_notebook:
        if nb_rel:
            raise SystemExit("--no-notebook cannot be combined with --notebook")
    else:
        if not nb_rel:
            raise SystemExit("--notebook is required unless --no-notebook is given")
        nb_abs = REPO / nb_rel
        if not nb_abs.is_file():
            raise SystemExit(f"notebook not found: {nb_abs}")
        size_mb = nb_abs.stat().st_size / 1e6
        if size_mb > 8:
            raise SystemExit(f"notebook is {size_mb:.1f} MB; clear large outputs first")

    today = dt.date.today().isoformat()
    default_qa = "NOT_APPLICABLE" if args.status == "blocked" else "PENDING"
    qa = {
        "dataset_visualisation_status": args.viz or default_qa,
        "class_scatter_status": args.scatter or default_qa,
        "quantum_circuit_visualisation_status": args.circuit or default_qa,
        "visualisation_validation_status": args.viz_validated or default_qa,
        "retrospective_audit_status": args.audit or ("NOT_APPLICABLE" if args.status == "blocked" else "PENDING"),
    }
    row = update_manifest(args.qc, nb_rel, args.status, args.paper_metrics,
                          args.notebook_metrics, args.notes, today, qa)
    title = row["Full paper title"]

    if not LOG.exists():
        LOG.write_text("# Reproduction log\n\nOne line per published notebook (newest last).\n\n", encoding="utf-8")
    link = f"[{nb_rel}]({nb_rel})" if nb_rel else "(no notebook)"
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"- {today} | {args.qc} | {args.status} | {link} | {title} | "
                f"paper: {args.paper_metrics} | notebook: {args.notebook_metrics} | {args.notes}\n")
    print(f"manifest row {args.qc} updated; log appended")
    if args.dry_run:
        return 0

    paths = ([nb_rel] if nb_rel else []) + ["manifest.csv", "REPRODUCTION_LOG.md", *args.extra]
    for p in paths:
        r = subprocess.run(["git", "check-ignore", "-q", p], cwd=REPO)
        if r.returncode == 0:
            raise SystemExit(f"refusing to add ignored path: {p}")
    git("add", "--", *paths)
    staged = git("diff", "--cached", "--name-only").splitlines()
    unexpected = [s for s in staged if s not in paths]
    if unexpected:
        raise SystemExit(f"unexpected staged files: {unexpected}")
    head = (f"Add {Path(nb_rel).stem} notebook for {args.qc} ({args.status})" if nb_rel
            else f"Record {args.qc} as {args.status}")
    msg = f"{head}\n\n{title}\n\nCo-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>\n"
    git("commit", "-q", "-m", msg)
    sha = git("rev-parse", "HEAD")
    print(f"committed {sha[:10]}")
    if args.no_push:
        return 0
    git("push", "origin", "main")
    git("fetch", "origin")
    remote_sha = git("rev-parse", "origin/main")
    if remote_sha != sha:
        raise SystemExit(f"push verification failed: HEAD {sha} vs origin/main {remote_sha}")
    contains = git("branch", "-r", "--contains", sha)
    print(f"verified on origin/main: {sha}")
    if nb_rel:
        print(f"github : {REMOTE_WEB}/blob/main/{nb_rel}")
        print(f"colab  : https://colab.research.google.com/github/owlmt/QML/blob/main/{nb_rel}")
    print(f"remote branches containing commit: {contains}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
