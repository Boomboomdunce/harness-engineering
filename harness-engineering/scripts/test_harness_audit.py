#!/usr/bin/env python3
"""Tests for harness_audit.py."""

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("harness_audit.py")


class HarnessAuditTest(unittest.TestCase):
    def run_audit(self, root: Path) -> dict:
        result = subprocess.run(
            ["python3", str(SCRIPT), str(root)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return json.loads(result.stdout)

    def test_reports_core_harness_surfaces(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AGENTS.md").write_text("# Test\n\nShort guide\n", encoding="utf-8")
            (root / "README.md").write_text("# Readme\n", encoding="utf-8")
            (root / "docs").mkdir()
            (root / "docs" / "architecture.md").write_text("# Architecture\n", encoding="utf-8")
            (root / "docs" / "spec.md").write_text("# Spec\n", encoding="utf-8")
            (root / "docs" / "verification.md").write_text("# Verification\n", encoding="utf-8")
            (root / "progress-tracker.json").write_text("[]\n", encoding="utf-8")
            (root / "pyproject.toml").write_text("[project]\nname='x'\n", encoding="utf-8")

            report = self.run_audit(root)

            self.assertEqual(report["agent_files"], ["AGENTS.md"])
            self.assertTrue(report["has_readme"])
            self.assertTrue(report["has_docs"])
            self.assertTrue(report["has_architecture"])
            self.assertTrue(report["has_spec"])
            self.assertTrue(report["has_verification_doc"])
            self.assertTrue(report["has_progress_tracker"])
            self.assertTrue(report["has_runtime_entry"])
            self.assertNotIn("missing project instruction file", report["warnings"])

    def test_warns_for_long_instruction_file_and_missing_tracker(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AGENTS.md").write_text("\n".join(["line"] * 151), encoding="utf-8")
            (root / "docs").mkdir()

            report = self.run_audit(root)

            self.assertIn("AGENTS.md is 151 lines; consider splitting into docs", report["warnings"])
            self.assertIn("missing progress tracker", report["warnings"])


if __name__ == "__main__":
    unittest.main()
