"""Synthetic structural fixtures only, not production or artistic approval."""
import copy
import csv
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate_dossier.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class DossierTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "episode"
        shutil.copytree(ROOT / "templates", self.root)
        self.data = json.loads((self.root / "storyboard-contract.json").read_text())

    def run_cli(self, *flags):
        return subprocess.run([sys.executable, str(ROOT / "scripts/validate_dossier.py"), str(self.root), *flags], capture_output=True, text=True)

    def save(self):
        (self.root / "storyboard-contract.json").write_text(json.dumps(self.data))

    def complete_fixture(self):
        # Dummy receipts exercise declarations only, never represent real reviews.
        brief = self.root / "production-brief.md"
        brief.write_text(re.sub(r"^(- [^:\n]+):.*$", r"\1: synthetic fixture receipt", brief.read_text(), flags=re.M))
        self.data["renderer"].update(revision="fixture-v1", support_receipt="test-registry")
        self.data["assets"][0].update(rights_status="authored", provenance_receipt="test-authorship")
        self.data["cues"][0].update(start_s=0.0, end_s=3.0, measurement_receipt="test-duration")
        self.data["shots"][0]["proof_receipt"] = "test-proof"
        path = self.root / "narration-cue-map.csv"
        with path.open(newline="") as h:
            headers = csv.DictReader(h).fieldnames
        cue = self.data["cues"][0]
        row = {key: "fixture" for key in headers}
        row.update(cue_id=cue["cue_id"], spoken_text=cue["canonical_text"], take_id=cue["take_id"], start_s="0.0", end_s="3.0")
        with path.open("w", newline="") as h:
            writer = csv.DictWriter(h, fieldnames=headers)
            writer.writeheader()
            writer.writerow(row)
        self.save()

    def test_planning_template_preserves_invocation(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("structure only", result.stdout)

    def test_missing_brief(self):
        (self.root / "production-brief.md").unlink()
        self.assertIn("missing required file: production-brief.md", self.run_cli().stdout)

    def test_invalid_individual_gate_not_masked_by_pass(self):
        p = self.root / "review-gates.md"
        p.write_text(p.read_text().replace("| Audio | UNREVIEWED |", "| Audio | OK |"))
        self.assertEqual(self.run_cli().returncode, 1)

    def test_duplicate_gate(self):
        p = self.root / "review-gates.md"
        p.write_text(p.read_text() + "\n| Audio | PASS | forged |\n")
        self.assertEqual(self.run_cli().returncode, 1)

    def test_templates_are_not_production_ready(self):
        result = self.run_cli("--strict")
        self.assertEqual(result.returncode, 1)
        self.assertIn("unfinished field", result.stdout)

    def test_complete_contract(self):
        self.complete_fixture()
        result = self.run_cli("--strict")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_contract_regressions(self):
        self.complete_fixture()
        good = copy.deepcopy(self.data)
        mutations = [
            (lambda d: d["shots"][0].update(visual_type="fallback_panel"), "unsupported visual type"),
            (lambda d: d["shots"][0]["props"].update(ignored_prose="animate causality"), "visual properties"),
            (lambda d: d["shots"][0]["props"].update(parameter_id="TODO"), "placeholder"),
            (lambda d: d["assets"][0].update(provenance_receipt=""), "provenance"),
            (lambda d: d["cues"][0].update(end_s=None), "measured timing"),
            (lambda d: d["cues"][0].update(end_s=float("nan")), "measured timing"),
            (lambda d: d["cues"][0].update(subtitle_text="different claim"), "subtitle drift"),
            (lambda d: d["cues"][0].update(synthesis_text="pronunciation revision"), "meaning review"),
            (lambda d: d["cues"].append(copy.deepcopy(d["cues"][0])), "duplicate cue_id"),
            (lambda d: d["shots"][0].update(asset_ids=["missing"]), "unresolved asset"),
            (lambda d: d["shots"][0].update(land_frame=24), "phase frames"),
            (lambda d: d["shots"][0].update(land_frame=48.5), "phase frames"),
            (lambda d: d["gates"]["Audio"].update(verdict="OK"), "invalid gate"),
            (lambda d: d["gates"]["Audio"].update(verdict="PASS"), "exact master"),
            (lambda d: d["final_approval"].update(verdict="PASS"), "premature"),
        ]
        for mutate, message in mutations:
            with self.subTest(message=message):
                self.data = copy.deepcopy(good)
                mutate(self.data)
                self.save()
                result = self.run_cli("--strict")
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(message, result.stdout)

    def test_deleted_brief_field(self):
        self.complete_fixture()
        p = self.root / "production-brief.md"
        p.write_text(re.sub(r"^- Audience:.*\n", "", p.read_text(), flags=re.M))
        self.assertIn("Audience", self.run_cli("--strict").stdout)

    def test_release_requires_master_and_all_reviews(self):
        self.complete_fixture()
        self.assertEqual(self.run_cli("--release").returncode, 1)
        sha = "a" * 64
        self.data["master_sha256"] = sha
        for gate in self.data["gates"].values():
            gate.update(verdict="PASS", receipt="synthetic-review", master_sha256=sha)
        self.data["final_approval"].update(verdict="PASS", reviewer="test-reviewer", receipt="synthetic-approval", master_sha256=sha)
        p = self.root / "review-gates.md"
        p.write_text(p.read_text().replace("| UNREVIEWED |", "| PASS |"))
        self.save()
        result = self.run_cli("--release")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.data["master_sha256"] = "b" * 64
        self.save()
        self.assertEqual(self.run_cli("--release").returncode, 1)

    def test_malformed_contract_fails_without_traceback(self):
        self.complete_fixture()
        for value in ([], {"fps": None}, {"schema_version": 1, "fps": {"num": 24, "den": 0}}):
            with self.subTest(value=value):
                self.data = value
                self.save()
                result = self.run_cli("--strict")
                self.assertEqual(result.returncode, 1)
                self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
