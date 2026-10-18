"""List the next unprocessed papers from manifest.csv (the persistent queue).

Usage: python tools/next_papers.py [--n 5] [--exclude QC-001 QC-002 ...] [--index <paper_index.csv>]
        [--status]   (print a status summary instead)

A paper is unprocessed when its "Reproduction status" column is empty or "not started".
Papers are returned in QC-ID order so the queue position is simply the first unprocessed row.
"""
import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "manifest.csv"


IMPLEMENTED = {"reproduced", "partially reproduced", "implemented but unvalidated"}


def topics_of(row):
    return [t.strip() for t in row["Assigned cybersecurity topic folder(s)"].split(";") if t.strip()]


def load_index(path):
    if path and Path(path).exists():
        with open(path, encoding="utf-8", newline="") as f:
            return {r["QC-ID"]: r for r in csv.DictReader(f)}
    return {}


def candidate_score(row, ix):
    """Higher is better: readable text, a known framework, a known dataset, not a survey."""
    if not ix:
        return 0
    s = 0
    if int(ix.get("chars", "0") or 0) > 5000:
        s += 2
    if any(k in ix.get("frameworks", "") for k in ("Qiskit", "PennyLane", "TensorFlow Quantum")):
        s += 2
    if ix.get("datasets", ""):
        s += 1
    if "Survey" in ix.get("models", ""):
        s -= 2
    if "survey" in row["Full paper title"].lower() or "review" in row["Full paper title"].lower():
        s -= 3
    if ix.get("metric snippets", ""):
        s += 1
    return s


def coverage_mode(rows, done, args):
    index = load_index(args.index)
    folders = sorted({t for r in rows for t in topics_of(r)})
    counts = {t: 0 for t in folders}
    for r in done.values():
        if r.get("Reproduction status") in IMPLEMENTED and r.get("Notebook path"):
            folder = r["Notebook path"].split("/")[0]
            counts[folder] = counts.get(folder, 0) + 1
    print("implemented notebooks per topic folder:")
    for t in folders:
        print(f"  {counts[t]}  {t}")
    print()
    short = [t for t in folders if counts[t] < args.coverage and not t.startswith("_")]
    print(f"topics below {args.coverage}: {len(short)}\n")
    for t in sorted(short, key=lambda x: (counts[x], x)):
        cands = [r for r in rows if r["QC-ID"] not in done and r["QC-ID"] not in args.exclude
                 and t in topics_of(r)]
        cands.sort(key=lambda r: (-candidate_score(r, index.get(r["QC-ID"])), r["QC-ID"]))
        print(f"== {t} (has {counts[t]}, {len(cands)} unprocessed candidates)")
        for r in cands[: args.per_topic]:
            ix = index.get(r["QC-ID"], {})
            print(f"   {r['QC-ID']} | {r['Year']} | {r['Full paper title'][:95]}")
            print(f"      score {candidate_score(r, ix)} | ds: {ix.get('datasets', '')[:70]} | fw: "
                  f"{ix.get('frameworks', '')[:40]} | m: {ix.get('models', '')[:60]}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--exclude", nargs="*", default=[])
    ap.add_argument("--index", default=None, help="paper_index.csv from tools/paper_index.py")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--coverage", type=int, default=0,
                    help="coverage-first mode: list candidates for every topic folder that has fewer "
                         "than this many implemented notebooks (each candidate is the best unprocessed "
                         "paper assigned to that topic)")
    ap.add_argument("--per-topic", type=int, default=2, help="candidates to show per topic in coverage mode")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    with MANIFEST.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    done = {r["QC-ID"]: r for r in rows if r.get("Reproduction status", "") not in ("", "not started")}

    if args.coverage:
        return coverage_mode(rows, done, args)
    if args.status:
        counts = Counter(r.get("Reproduction status", "") or "unprocessed" for r in rows)
        print(f"total {len(rows)} | " + " | ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
        pending = [r["QC-ID"] for r in rows if r["QC-ID"] not in done]
        print(f"next unprocessed: {pending[:5]} ... ({len(pending)} left)")
        return 0

    index = load_index(args.index)
    shown = 0
    for r in rows:
        qc = r["QC-ID"]
        if qc in done or qc in args.exclude:
            continue
        folder = r["Assigned cybersecurity topic folder(s)"].split(";")[0].strip()
        print(f"{qc} | {r['Year']} | {r['Full paper title'][:110]}")
        print(f"   folder: {folder} | pdf: {r['PDF filename']}")
        if qc in index:
            ix = index[qc]
            print(f"   chars: {ix['chars']} | datasets: {ix['datasets'][:120]}")
            print(f"   frameworks: {ix['frameworks'][:80]} | models: {ix['models'][:120]}")
            print(f"   metrics: {ix['metric snippets'][:120]} | code: {ix['code links'][:80]}")
        shown += 1
        if shown >= args.n:
            break
    return 0


if __name__ == "__main__":
    sys.exit(main())
