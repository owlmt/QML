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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--exclude", nargs="*", default=[])
    ap.add_argument("--index", default=None, help="paper_index.csv from tools/paper_index.py")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    with MANIFEST.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    done = {r["QC-ID"]: r for r in rows if r.get("Reproduction status", "") not in ("", "not started")}
    if args.status:
        counts = Counter(r.get("Reproduction status", "") or "unprocessed" for r in rows)
        print(f"total {len(rows)} | " + " | ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
        pending = [r["QC-ID"] for r in rows if r["QC-ID"] not in done]
        print(f"next unprocessed: {pending[:5]} ... ({len(pending)} left)")
        return 0

    index = {}
    if args.index and Path(args.index).exists():
        with open(args.index, encoding="utf-8", newline="") as f:
            index = {r["QC-ID"]: r for r in csv.DictReader(f)}
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
