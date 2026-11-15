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
}
CSV_SCHEMAS = {
    "asset-ledger.csv": {
        "asset_id", "sequence_id", "description", "narrative_role", "classification",
        "source", "date", "rights_status", "credit_needed", "crop_or_usage_notes",
        "replacement_if_missing", "status",
    },
    "visual-asset-plan.csv": {
        "asset_id", "sequence_id", "cue_id", "viewer_understanding", "visual_job",
        "asset_class", "source_or_build", "rights_status", "proof_status", "crop_treatment",
        "credit_or_label", "visible_operation", "fallback", "status",
    },
    "narration-cue-map.csv": {
        "cue_id", "sequence_id", "spoken_text", "claim_ids", "visual_job", "delivery_note",
        "voice_policy", "reference_id", "take_id", "start_s", "end_s", "asr_status",
        "speaker_check_status", "retime_status", "status",
    },
    "music-cue-map.csv": {
        "music_cue_id", "sequence_ids", "start_s", "end_s", "narrative_state", "energy_1_to_5",
        "tempo_feel", "instrumentation_role", "track_or_stem_source", "license_status",
        "entry_exit_action", "ducking_or_silence_plan", "status",
    },
}
ALLOWED_VERDICTS = {"PASS", "FAIL", "UNREVIEWED", "BLOCKED"}


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
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                failures.append(f"{name} missing heading: {heading}")

    for name, expected_headers in CSV_SCHEMAS.items():
        path = root / name
        if not path.is_file():
            failures.append(f"missing required file: {name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            found = set(reader.fieldnames or [])
        missing = expected_headers - found
        if missing:
            failures.append(f"{name} missing headers: " + ", ".join(sorted(missing)))

    gates = root / "review-gates.md"
    if gates.is_file():
        text = gates.read_text(encoding="utf-8")
        for gate in ("Technical", "Factual", "Editorial", "Audio"):
            if gate not in text:
                failures.append(f"review-gates.md missing gate: {gate}")
        if not any(word in text for word in ALLOWED_VERDICTS):
            failures.append("review-gates.md has no recognized verdict")

    if failures:
        for failure in failures:
            error(failure)
        return 1

    print(f"PASS: dossier structure valid: {root}")
    print("NOTE: this validates structure only; evidence, rights, clone checks, mix, and editorial approval still require review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
