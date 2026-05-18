"""Tests for PhishGuard AI MVP."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from apps.api.app.cli import analyze_email, build_triage_report


ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "data/samples/phishing.eml"


class PhishGuardTests(unittest.TestCase):
    def test_detects_phishing_signals(self) -> None:
        _, findings, summary = analyze_email(SAMPLE)
        kinds = {finding["kind"] for finding in findings}

        self.assertIn("email.auth.spf_fail", kinds)
        self.assertIn("email.auth.dkim_fail", kinds)
        self.assertIn("email.auth.dmarc_fail", kinds)
        self.assertIn("email.sender.reply_to_mismatch", kinds)
        self.assertIn("email.content.urgency", kinds)
        self.assertIn("email.link.suspicious_host", kinds)
        self.assertGreater(summary["risk_score"], 80)
        self.assertEqual("high", summary["risk_level"])
        self.assertEqual(5, summary["severity_counts"]["high"])
        self.assertIn("Quarantine", summary["recommended_response"])

    def test_cli_writes_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, "-m", "apps.api.app.cli", "--email", str(SAMPLE), "--out-dir", tmp],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            summary = json.loads(Path(tmp, "summary.json").read_text(encoding="utf-8"))
            report = Path(tmp, "report.md").read_text(encoding="utf-8")
            triage = Path(tmp, "triage.md").read_text(encoding="utf-8")

            self.assertIn("Risk score", result.stdout)
            self.assertGreater(summary["findings"], 5)
            self.assertIn("PhishGuard AI Report", report)
            self.assertIn("Priority Queue", report)
            self.assertIn("Analyst Checklist", triage)

    def test_builds_triage_report(self) -> None:
        _, findings, summary = analyze_email(SAMPLE)
        triage = build_triage_report(summary, findings)

        self.assertIn("PhishGuard AI Triage", triage)
        self.assertIn("High Priority Findings", triage)


if __name__ == "__main__":
    unittest.main()
