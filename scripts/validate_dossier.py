#!/usr/bin/env python3
"""Validate the minimum structure of an editorial project dossier.

Usage: python3 scripts/validate_dossier.py path/to/dossier [--strict | --release]
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
from pathlib import Path

REQUIRED_FILES = {
    "production-brief.md": ["# Production brief", "## Editorial intent", "## Authorization and delivery", "## Sources and assets", "## Scope ledger and freshness", "## Acceptance and blockers"],
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


GATES = ("Technical", "Factual", "Editorial", "Audio")
PLACEHOLDER = re.compile(r"^(?:TODO|TBD|UNREVIEWED|BLOCKED|NOT SET|NOT MEASURED)(?:\b|:)|<[^>]+>", re.I)


def filled(value):
    return isinstance(value, str) and bool(value.strip()) and not PLACEHOLDER.search(value.strip())


def finite(value):
    return type(value) in (int, float) and math.isfinite(value)


def validate_contract(root: Path, release=False) -> list[str]:
    """Validate declarations, never claim that a receipt was actually reviewed."""
    errors = []
    def check(ok, message):
        if not ok:
            errors.append(message)

    brief = root / "production-brief.md"
    if brief.exists():
        # The template owns field names so removing an unfinished field cannot pass.
        template = Path(__file__).resolve().parents[1] / "templates/production-brief.md"
        expected = re.findall(r"^- ([^:\n]+):", template.read_text(encoding="utf-8"), re.M)
        text = brief.read_text(encoding="utf-8")
        for field in expected:
            values = re.findall(r"^- " + re.escape(field) + r":[ \t]*(.*)$", text, re.M)
            # Final review/duration may remain open during production, not at release.
            deferred = field.startswith(("Measured final", "Technical /", "Exact master"))
            check(len(values) == 1 and (filled(values[0]) or (deferred and not release)),
                  f"brief missing, duplicate or unfinished field: {field}")
    else:
        errors.append("missing production brief")
    try:
        data = json.loads((root / "storyboard-contract.json").read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("root must be an object")
        check(data.get("schema_version") == 1, "unsupported contract schema_version")
        fps = data["fps"]
        check(all(type(fps[k]) is int and fps[k] > 0 for k in ("num", "den")), "invalid rational fps")
        rate = fps["num"] / fps["den"]
        renderer = data["renderer"]
        check(filled(renderer["revision"]) and filled(renderer["support_receipt"]), "missing renderer support receipt/revision")
        types = renderer["types"]
        check(isinstance(types, dict) and bool(types), "empty renderer types")
        for name, spec in types.items():
            check(isinstance(spec["required_props"], list) and isinstance(spec["supported_props"], list), f"invalid renderer property lists: {name}")
            check(set(spec["required_props"]) <= set(spec["supported_props"]), f"required properties unsupported: {name}")

        def index(name, key):
            rows = data[name]
            if not isinstance(rows, list):
                raise ValueError(f"{name} must be a list")
            check(bool(rows), f"empty {name}")
            result = {}
            for row in rows:
                ident = row[key]
                check(filled(ident) and ident not in result, f"invalid/duplicate {key}: {ident}")
                result[ident] = row
            return result

        assets = index("assets", "asset_id")
        for ident, asset in assets.items():
            check(all(filled(asset.get(k)) for k in ("source", "rights_status", "provenance_receipt", "evidence_class")), f"missing asset provenance/rights: {ident}")
        cues = index("cues", "cue_id")
        with (root / "narration-cue-map.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        csv_cues = {r["cue_id"]: r for r in rows}
        check(len(rows) == len(csv_cues) and set(csv_cues) == set(cues), "narration CSV cue IDs differ or duplicate")
        takes = set()
        for ident, cue in cues.items():
            check(all(filled(cue.get(k)) for k in ("take_id", "canonical_text", "synthesis_text", "subtitle_text", "measurement_receipt")), f"unfinished cue: {ident}")
            check(cue["take_id"] not in takes, f"duplicate take_id: {ident}")
            takes.add(cue["take_id"])
            check(cue["canonical_text"] == cue["subtitle_text"], f"subtitle drift: {ident}")
            if cue["canonical_text"] != cue["synthesis_text"]:
                check(filled(cue.get("meaning_review_receipt")), f"pronunciation meaning review missing: {ident}")
            start, end = cue["start_s"], cue["end_s"]
            valid_time = finite(start) and finite(end) and 0 <= start < end
            check(valid_time, f"invalid measured timing: {ident}")
            row = csv_cues.get(ident, {})
            check(row.get("spoken_text") == cue["canonical_text"] and row.get("take_id") == cue["take_id"], f"narration CSV text/take mismatch: {ident}")
            if valid_time:
                check(float(row.get("start_s", "nan")) == start and float(row.get("end_s", "nan")) == end, f"narration CSV timing mismatch: {ident}")
        shots = index("shots", "shot_id")
        used = set()
        for ident, shot in shots.items():
            visual = shot["visual_type"]
            check(visual in types, f"unsupported visual type: {ident}: {visual}")
            if visual in types:
                props = set(shot["props"])
                check(set(types[visual]["required_props"]) <= props <= set(types[visual]["supported_props"]), f"unsupported/missing visual properties: {ident}")
                check(not any(isinstance(v, str) and not filled(v) for v in shot["props"].values()), f"placeholder visual property: {ident}")
            check(filled(shot.get("proof_receipt")), f"missing encoded proof receipt: {ident}")
            check(bool(shot["asset_ids"]) and set(shot["asset_ids"]) <= set(assets), f"unresolved asset IDs: {ident}")
            check(bool(shot["cue_ids"]) and set(shot["cue_ids"]) <= set(cues), f"unresolved cue IDs: {ident}")
            used.update(shot["cue_ids"])
            frames = [shot[k] for k in ("start_frame", "before_frame", "operate_frame", "land_frame", "end_frame")]
            valid_frames = all(type(v) is int for v in frames) and 0 <= frames[0] <= frames[1] < frames[2] < frames[3] < frames[4]
            check(valid_frames, f"invalid integer phase frames: {ident}")
            for cue_id in shot["cue_ids"]:
                cue = cues.get(cue_id, {})
                if valid_frames and finite(cue.get("start_s")) and finite(cue.get("end_s")):
                    check(frames[0] / rate < cue["end_s"] and frames[4] / rate > cue["start_s"], f"shot does not overlap measured cue: {ident}")
        check(used == set(cues), "cues missing executable shots")
        master = data.get("master_sha256", "")
        gates = data["gates"]
        gate_text = (root / "review-gates.md").read_text(encoding="utf-8")
        for name in GATES:
            gate = gates[name]
            check(gate["verdict"] in ALLOWED_VERDICTS, f"invalid gate verdict: {name}")
            row = re.findall(r"^\|\s*" + name + r"\s*\|\s*([^|]+)\|", gate_text, re.M)
            check(len(row) == 1 and row[0].strip() == gate["verdict"], f"gate Markdown/JSON mismatch: {name}")
            if release or gate["verdict"] == "PASS":
                check(gate["verdict"] == "PASS" and filled(gate.get("receipt")) and bool(re.fullmatch(r"[0-9a-f]{64}", master)) and gate.get("master_sha256") == master, f"gate not approved for exact master: {name}")
        approval = data["final_approval"]
        check(approval["verdict"] in ALLOWED_VERDICTS, "invalid final approval verdict")
        if release or approval["verdict"] == "PASS":
            check(approval["verdict"] == "PASS" and all(gates[n]["verdict"] == "PASS" for n in GATES) and filled(approval.get("reviewer")) and filled(approval.get("receipt")) and bool(re.fullmatch(r"[0-9a-f]{64}", master)) and approval.get("master_sha256") == master, "final approval absent, premature or wrong master")
    except (OSError, ValueError, TypeError, KeyError, AttributeError, ZeroDivisionError) as exc:
        errors.append(f"invalid storyboard contract: {exc}")
    return errors


def error(message: str) -> None:
    print(f"FAIL: {message}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dossier", type=Path)
    parser.add_argument("--strict", action="store_true", help="validate executable production contract")
    parser.add_argument("--release", action="store_true", help="also require exact-master review and approval receipts")
    args = parser.parse_args()
    root = args.dossier
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
        for gate in GATES:
            rows = re.findall(r"^\|\s*" + gate + r"\s*\|\s*([^|]+)\|", text, re.M)
            if len(rows) != 1 or rows[0].strip() not in ALLOWED_VERDICTS:
                failures.append(f"review-gates.md missing, duplicate or invalid verdict: {gate}")

    if args.strict or args.release:
        failures.extend(validate_contract(root, release=args.release))

    if failures:
        for failure in failures:
            error(failure)
        return 1

    print(f"PASS: dossier structure valid: {root}")
    print("NOTE: this validates structure only; evidence, rights, clone checks, mix, and editorial approval still require review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
