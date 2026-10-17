"""Execute a notebook top-to-bottom with nbclient and report per-cell timing and errors.

Usage:
    python tools/execute_notebook.py <notebook.ipynb> [--timeout SECONDS] [--out PATH]
                                     [--cwd DIR] [--max-size-mb N]

Exit code 0 when every cell ran without error, 1 otherwise. With --out the executed
notebook (with outputs) is written there; otherwise the input file is updated in place.
Oversized outputs (over --max-size-mb, default 4) are reported so they can be cleared.
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("notebook")
    ap.add_argument("--timeout", type=int, default=3600, help="per-cell timeout in seconds")
    ap.add_argument("--out", default=None)
    ap.add_argument("--cwd", default=None, help="working directory for the kernel (default: notebook dir)")
    ap.add_argument("--max-size-mb", type=float, default=4.0)
    ap.add_argument("--kernel", default="python3")
    args = ap.parse_args()

    nb_path = Path(args.notebook).resolve()
    out_path = Path(args.out).resolve() if args.out else nb_path
    cwd = Path(args.cwd).resolve() if args.cwd else nb_path.parent
    nb = nbformat.read(nb_path, as_version=4)

    code_cells = [c for c in nb.cells if c.cell_type == "code"]
    print(f"notebook : {nb_path}")
    print(f"cwd      : {cwd}")
    print(f"cells    : {len(nb.cells)} total, {len(code_cells)} code")
    print(f"timeout  : {args.timeout}s per cell")

    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    # Do not set MPLBACKEND: ipykernel's inline backend must stay active so figures are
    # captured as image/png outputs (Agg would silently drop every plt.show()).
    os.environ.pop("MPLBACKEND", None)
    client = NotebookClient(
        nb,
        timeout=args.timeout,
        kernel_name=args.kernel,
        resources={"metadata": {"path": str(cwd)}},
        allow_errors=False,
        record_timing=True,
    )

    t_start = time.time()
    failed_cell = None
    error_text = ""
    try:
        with client.setup_kernel():
            for idx, cell in enumerate(nb.cells):
                if cell.cell_type != "code":
                    continue
                src_head = "".join(cell.source).strip().splitlines()[:1]
                head = src_head[0][:70] if src_head else ""
                t0 = time.time()
                try:
                    client.execute_cell(cell, idx)
                    print(f"  [{idx:3d}] ok   {time.time() - t0:8.1f}s  {head}", flush=True)
                except CellExecutionError as e:
                    failed_cell = idx
                    error_text = str(e)
                    print(f"  [{idx:3d}] FAIL {time.time() - t0:8.1f}s  {head}", flush=True)
                    break
    finally:
        nbformat.write(nb, out_path)

    elapsed = time.time() - t_start
    size_mb = out_path.stat().st_size / 1e6
    print(f"elapsed  : {elapsed/60:.1f} min")
    print(f"written  : {out_path} ({size_mb:.2f} MB)")
    if size_mb > args.max_size_mb:
        print(f"WARNING  : notebook larger than {args.max_size_mb} MB; clear bulky outputs before committing")

    if failed_cell is not None:
        print(f"\nFAILED at cell {failed_cell}:\n{error_text[-3000:]}")
        return 1
    print("RESULT   : all code cells executed without error")
    return 0


if __name__ == "__main__":
    sys.exit(main())
