"""Decision and input checks for the TurtleBird CLI."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
SPEC = importlib.util.spec_from_file_location("turtlebird_assess", ROOT / "assess.py")
assess = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(assess)


class SafetyGateTests(unittest.TestCase):
    def setUp(self):
        self.policy = assess.load_policy(EXAMPLES / "policy.json")
        self.cases = assess.load_cases(EXAMPLES / "validation.csv")

    def test_validated_sample_is_ready_for_human_review(self):
        report = assess.assess(self.cases, self.policy, "validate")
        self.assertEqual(report["status"], "ready_for_human_review")
        self.assertEqual(report["overall"]["model_passes"], 11)
        self.assertEqual(report["overall"]["baseline_passes"], 8)

    def test_critical_failure_overrides_good_pass_rates(self):
        cases = assess.load_cases(EXAMPLES / "monitoring.csv")
        report = assess.assess(cases, self.policy, "monitor")
        self.assertEqual(report["status"], "escalate_and_consider_pause")
        self.assertGreater(report["overall"]["model_pass_rate"], 0.80)
        self.assertEqual(report["slices"]["no-current-source"]["reasons"], ["critical_failure"])
        self.assertEqual(assess.assess(cases, self.policy, "validate")["status"], "hold")

    def test_missing_slice_blocks_an_otherwise_good_result(self):
        cases = self.cases[:8] * 2
        report = assess.assess(cases, self.policy, "validate")
        self.assertEqual(report["status"], "hold")
        self.assertEqual(report["overall"]["reasons"], [])
        self.assertIsNone(report["slices"]["no-current-source"]["model_pass_rate"])

    def test_unplanned_slice_goes_to_review(self):
        report = assess.assess(self.cases + [("new-context", "pass", "pass")], self.policy, "monitor")
        self.assertEqual(report["status"], "investigate")
        self.assertEqual(report["slices"]["new-context"]["reasons"], ["slice_not_in_policy"])

    def test_empty_input_requires_investigation(self):
        report = assess.assess([], self.policy, "monitor")
        self.assertEqual(report["status"], "investigate")
        self.assertIsNone(report["overall"]["model_pass_rate"])
        self.assertEqual(report["overall"]["reasons"], ["too_few_cases"])

    def test_threshold_boundaries(self):
        assess.validate_thresholds({"min_cases": 1, "min_pass_rate": 1}, "test")
        invalid = [
            {"min_cases": True, "min_pass_rate": 0.8},
            {"min_cases": 0, "min_pass_rate": 0.8},
            {"min_cases": 1, "min_pass_rate": 0},
            {"min_cases": 1, "min_pass_rate": 1.01},
            {"min_cases": 1, "min_pass_rate": float("nan")},
            {"min_cases": 1, "min_pass_rate": True},
        ]
        for value in invalid:
            with self.subTest(value=value), self.assertRaises(ValueError):
                assess.validate_thresholds(value, "test")

    def test_duplicate_policy_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "policy.json"
            path.write_text('{"overall": {}, "overall": {}, "slices": {}}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Duplicate policy key"):
                assess.load_policy(path)

    def test_csv_structure_and_results_are_checked(self):
        header = "case_id,slice,model_result,baseline_result\n"
        invalid = [
            "wrong,columns\n",
            header + "A,x,pass\n",
            header + "A,x,pass,pass,extra\n",
            header + "A,x,unknown,pass\n",
            header + "A,,pass,pass\n",
        ]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "cases.csv"
            for contents in invalid:
                with self.subTest(contents=contents), self.assertRaises(ValueError):
                    path.write_text(contents, encoding="utf-8")
                    assess.load_cases(path)

    def test_cli_exit_codes_and_malformed_input(self):
        command = [sys.executable, str(ROOT / "assess.py"), "monitor",
                   "--policy", str(EXAMPLES / "policy.json"), "--cases"]
        completed = subprocess.run(
            command + [str(EXAMPLES / "monitoring.csv")], capture_output=True, text=True, check=False
        )
        self.assertEqual(completed.returncode, 1)
        self.assertEqual(json.loads(completed.stdout)["status"], "escalate_and_consider_pause")

        with tempfile.TemporaryDirectory() as folder:
            bad = Path(folder) / "bad.csv"
            bad.write_text("case_id,slice,model_result,baseline_result\nA,x,pass,pass\nA,x,pass,pass\n")
            completed = subprocess.run(command + [str(bad)], capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 2)
        self.assertIn("duplicate case ID", completed.stderr)
        self.assertEqual(completed.stdout, "")


if __name__ == "__main__":
    unittest.main()
