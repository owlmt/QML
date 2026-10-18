"""Print the text outputs of the comparison / verdict cells of an executed notebook.

Usage: python tools/notebook_summary.py <notebook> [--grep verdict,reproduced,...] [--last N]
Deterministic helper for the dispatcher: shows the config cell, every stream/text output that
mentions a verdict keyword, and the last N code cells' outputs, so manifest metrics can be
written without another model call.
"""
import argparse
import json
import sys
from pathlib import Path


def text_outputs(cell):
    parts = []
    for o in cell.get("outputs", []):
        if o.get("output_type") == "stream":
            parts.append("".join(o.get("text", "")))
        elif "text/plain" in o.get("data", {}):
            parts.append("".join(o["data"]["text/plain"]))
        elif o.get("output_type") == "error":
            parts.append(f"ERROR {o.get('ename')}: {o.get('evalue')}")
    return "\n".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("notebook")
    ap.add_argument("--grep", default="verdict,reproduced,not reached,exceeded,cannot be checked,paper")
    ap.add_argument("--last", type=int, default=3)
    ap.add_argument("--max-chars", type=int, default=2500)
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    nb = json.loads(Path(args.notebook).read_text(encoding="utf-8"))
    cells = nb["cells"]
    code = [(i, c) for i, c in enumerate(cells) if c["cell_type"] == "code"]
    keys = [k.strip().lower() for k in args.grep.split(",") if k.strip()]

    print("### TITLE")
    for c in cells[:3]:
        if c["cell_type"] == "markdown":
            print("".join(c["source"])[:600])
            break
    print("\n### CONFIG CELL")
    for i, c in code:
        src = "".join(c["source"])
        if "FAST_MODE" in src and "=" in src:
            print(src[:1800])
            break
    print("\n### OUTPUTS MENTIONING VERDICT KEYWORDS")
    shown = set()
    for i, c in code:
        out = text_outputs(c)
        if out and any(k in out.lower() for k in keys):
            shown.add(i)
            print(f"\n--- cell {i} ---\n{out[: args.max_chars]}")
    print(f"\n### LAST {args.last} CODE CELL OUTPUTS")
    for i, c in code[-args.last:]:
        if i in shown:
            continue
        out = text_outputs(c)
        print(f"\n--- cell {i} ---\n{out[: args.max_chars] if out else '(no text output)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
