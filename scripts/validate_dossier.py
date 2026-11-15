#!/usr/bin/env python3
"""Validate the minimum structure of an editorial project dossier.

Usage: python3 scripts/validate_dossier.py path/to/dossier
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

REQUIRED_FILES = {
    "claim-map.md": ["# Claim map", "## Brief", "## Claims", "## Section handoffs"],
    "sequence-board.md": ["# Sequence board", "## Sequence notes"],
    "review-gates.md": ["# Review gates", "## Delivery label"],
    "asset-ledger.csv": [],
}
ALLOWED_VERDICTS = {"PASS", "FAIL", "UNREVIEWED", "BLOCKED"}
ASSET_HEADERS = {
    "asset_id", "sequence_id", "description", "narrative_role", "classification",
    "source", "date", "rights_status", "credit_needed", "crop_or_usage_notes",
    "replacement_if_missing", "status",
}


def error(message: str) -> None:
    print(f"FAIL: {message}")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2

    root = Path(sys.argv[1])
    if not root.is_dir():
        error(f"dossier is not a directory: {root}")
        return 2

    failures: list[str] = []
    for name, headings in REQUIRED_FILES.items():
        path = root / name
        if not path.is_file():
            failures.append(f"missing required file: {name}")
            continue
        if name.endswith(".md"):
            text = path.read_text(encoding="utf-8")
            for heading in headings:
                if heading not in text:
                    failures.append(f"{name} missing heading: {heading}")

    ledger = root / "asset-ledger.csv"
    if ledger.is_file():
        with ledger.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            found = set(reader.fieldnames or [])
            missing = ASSET_HEADERS - found
            if missing:
                failures.append("asset-ledger.csv missing headers: " + ", ".join(sorted(missing)))

    gates = root / "review-gates.md"
    if gates.is_file():
        text = gates.read_text(encoding="utf-8")
        for gate in ("Technical", "Factual", "Editorial", "Audio"):
            if gate not in text:
                failures.append(f"review-gates.md missing gate: {gate}")
        verdicts = {word for word in ALLOWED_VERDICTS if word in text}
        if not verdicts:
            failures.append("review-gates.md has no recognized verdict")

    if failures:
        for failure in failures:
            error(failure)
        return 1

    print(f"PASS: dossier structure valid: {root}")
    print("NOTE: this validates file structure only; evidence, rights, edit, and audio still require review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
