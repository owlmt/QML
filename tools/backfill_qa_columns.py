"""One-off: add the five visualisation QA columns to manifest.csv and backfill existing rows.

Published notebooks (reproduced / partially reproduced / implemented but unvalidated) get
PENDING in every QA column (the retrospective audit upgrades them); blocked papers get
NOT_APPLICABLE; unprocessed rows stay empty. Idempotent: existing non-empty values are kept.
"""
import csv
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "manifest.csv"
QA = ["dataset_visualisation_status", "class_scatter_status",
      "quantum_circuit_visualisation_status", "visualisation_validation_status",
      "retrospective_audit_status"]
IMPLEMENTED = {"reproduced", "partially reproduced", "implemented but unvalidated"}

raw = MANIFEST.read_bytes()
newline = "\r\n" if b"\r\n" in raw else "\n"
with MANIFEST.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fields = list(reader.fieldnames)
    rows = list(reader)
for c in QA:
    if c not in fields:
        fields.append(c)
changed = 0
for r in rows:
    status = r.get("Reproduction status", "")
    for c in QA:
        r.setdefault(c, "")
        if r[c]:
            continue
        if status in IMPLEMENTED:
            r[c] = "PENDING"; changed += 1
        elif status == "blocked":
            r[c] = "NOT_APPLICABLE"; changed += 1
with MANIFEST.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator=newline)
    w.writeheader(); w.writerows(rows)
print(f"columns now: {len(fields)}; cells backfilled: {changed}")
