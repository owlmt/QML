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
NEW_COLUMNS = ["Notebook path", "Reproduction status", "Paper metric(s)",
               "Notebook metric(s)", "Validated on", "Notes"]
STATUSES = {"not started", "in progress", "reproduced", "partially reproduced", "not reproducible"}


def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True, encoding="utf-8")
    if check and r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed:\n{r.stdout}\n{r.stderr}")
    return r.stdout.strip()


def update_manifest(qc, nb_rel, status, paper_m, nb_m, notes, today):
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
    with MANIFEST.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator=newline)
        w.writeheader()
        w.writerows(rows)
    return hit


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--qc", required=True)
    ap.add_argument("--notebook", required=True, help="repo-relative notebook path")
    ap.add_argument("--status", required=True, choices=sorted(STATUSES))
    ap.add_argument("--paper-metrics", default="")
    ap.add_argument("--notebook-metrics", default="")
    ap.add_argument("--notes", default="")
    ap.add_argument("--extra", nargs="*", default=[], help="additional repo-relative paths to commit")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="update manifest/log only, no git")
    args = ap.parse_args()

    nb_rel = args.notebook.replace("\\", "/")
    nb_abs = REPO / nb_rel
    if not nb_abs.is_file():
        raise SystemExit(f"notebook not found: {nb_abs}")
    size_mb = nb_abs.stat().st_size / 1e6
    if size_mb > 8:
        raise SystemExit(f"notebook is {size_mb:.1f} MB; clear large outputs first")

    today = dt.date.today().isoformat()
    row = update_manifest(args.qc, nb_rel, args.status, args.paper_metrics,
                          args.notebook_metrics, args.notes, today)
    title = row["Full paper title"]

    if not LOG.exists():
        LOG.write_text("# Reproduction log\n\nOne line per published notebook (newest last).\n\n", encoding="utf-8")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"- {today} | {args.qc} | {args.status} | [{nb_rel}]({nb_rel}) | {title} | "
                f"paper: {args.paper_metrics} | notebook: {args.notebook_metrics} | {args.notes}\n")
    print(f"manifest row {args.qc} updated; log appended")
    if args.dry_run:
        return 0

    paths = [nb_rel, "manifest.csv", "REPRODUCTION_LOG.md", *args.extra]
    for p in paths:
        r = subprocess.run(["git", "check-ignore", "-q", p], cwd=REPO)
        if r.returncode == 0:
            raise SystemExit(f"refusing to add ignored path: {p}")
    git("add", "--", *paths)
    staged = git("diff", "--cached", "--name-only").splitlines()
    unexpected = [s for s in staged if s not in paths]
    if unexpected:
        raise SystemExit(f"unexpected staged files: {unexpected}")
    msg = (f"Add {Path(nb_rel).stem} notebook for {args.qc} ({args.status})\n\n"
           f"{title}\n\nCo-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>\n")
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
    print(f"github : {REMOTE_WEB}/blob/main/{nb_rel}")
    print(f"colab  : https://colab.research.google.com/github/owlmt/QML/blob/main/{nb_rel}")
    print(f"remote branches containing commit: {contains}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
