"""Extract text from a paper PDF for reading (pypdf).

Usage: python tools/pdf_text.py <file.pdf> [--pages 1-4] [--out file.txt]
"""
import argparse
import sys
from pathlib import Path

from pypdf import PdfReader


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--pages", default=None, help="1-based inclusive range, e.g. 1-4")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    reader = PdfReader(args.pdf)
    n = len(reader.pages)
    lo, hi = 1, n
    if args.pages:
        a, _, b = args.pages.partition("-")
        lo, hi = int(a), int(b or a)
    chunks = [f"# {Path(args.pdf).name} | pages {lo}-{hi} of {n}\n"]
    for i in range(lo - 1, min(hi, n)):
        chunks.append(f"\n----- page {i + 1} -----\n")
        chunks.append(reader.pages[i].extract_text() or "")
    text = "".join(chunks)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out} ({len(text)} chars)")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
