"""Dispatcher check before publishing: executed, error-free, figures present, badge, size.

Usage: python tools/verify_notebook.py <repo-relative notebook path>
Exit 0 when all checks pass, 1 otherwise. Prints a one-line summary plus any problems.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    rel = sys.argv[1].replace("\\", "/")
    path = REPO / rel
    nb = json.loads(path.read_text(encoding="utf-8"))
    cells = nb["cells"]
    code = [c for c in cells if c["cell_type"] == "code"]
    src = "\n".join("".join(c["source"]) for c in cells)
    problems = []
    size_mb = path.stat().st_size / 1e6
    png = sum(1 for c in code for o in c.get("outputs", []) if "image/png" in o.get("data", {}))
    errs = [i for i, c in enumerate(cells) if c["cell_type"] == "code"
            and any(o.get("output_type") == "error" for o in c.get("outputs", []))]
    unexec = [i for i, c in enumerate(cells) if c["cell_type"] == "code" and c.get("execution_count") is None]
    no_id = [i for i, c in enumerate(cells) if not c.get("id")]
    fast = re.findall(r"^FAST_MODE\s*=\s*(True|False)", src, re.M)
    badge_ok = f"blob/main/{rel}" in src
    if errs:
        problems.append(f"error outputs in cells {errs}")
    if unexec:
        problems.append(f"unexecuted code cells {unexec}")
    if png == 0:
        problems.append("no image/png outputs")
    if not badge_ok:
        problems.append("Colab badge path does not match the file path")
    if size_mb > 4:
        problems.append(f"size {size_mb:.2f} MB > 4 MB")
    if no_id:
        problems.append(f"{len(no_id)} cells without id")
    print(f"{rel}: {len(cells)} cells ({len(code)} code), {png} figures, {size_mb:.2f} MB, "
          f"FAST_MODE={fast[0] if fast else '?'}, badge={'ok' if badge_ok else 'BAD'}")
    for p in problems:
        print("PROBLEM:", p)
    print("VERIFY OK" if not problems else "VERIFY FAILED")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
