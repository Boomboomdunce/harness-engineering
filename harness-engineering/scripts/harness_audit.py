#!/usr/bin/env python3
"""Audit repository harness surfaces and print a small JSON report."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


AGENT_FILES = ("AGENTS.md", "CLAUDE.md", "GEMINI.md")
RUNTIME_FILES = (
    "package.json",
    "pyproject.toml",
    "Cargo.toml",
    "go.mod",
    "Makefile",
    "docker-compose.yml",
    "Dockerfile",
)
META_FILES = {".DS_Store", "._.DS_Store"}


def _exists_any(root: Path, names: tuple[str, ...]) -> bool:
    return any((root / name).exists() for name in names)


def _count_lines(path: Path) -> int:
    try:
        return len(path.read_text(encoding="utf-8", errors="ignore").splitlines())
    except OSError:
        return 0


def _git_status(root: Path) -> dict[str, Any]:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "status", "--short"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return {"available": False, "dirty_count": 0, "meta_only": False, "sample": []}

    lines = [line for line in result.stdout.splitlines() if line.strip()]
    non_meta = []
    for line in lines:
        path_text = line[3:].strip().strip('"') if len(line) > 3 else ""
        if Path(path_text).name not in META_FILES:
            non_meta.append(line)

    return {
        "available": True,
        "dirty_count": len(lines),
        "meta_only": bool(lines) and not non_meta,
        "sample": non_meta[:5],
    }


def audit_repo(root: Path) -> dict[str, Any]:
    root = root.resolve()
    agent_files = [name for name in AGENT_FILES if (root / name).exists()]
    agent_line_counts = {name: _count_lines(root / name) for name in agent_files}

    docs_dir = root / "docs"
    doc_dir = root / "doc"
    docs_path = docs_dir if docs_dir.exists() else doc_dir

    report = {
        "path": str(root),
        "agent_files": agent_files,
        "agent_line_counts": agent_line_counts,
        "has_readme": _exists_any(root, ("README.md", "README.rst", "README")),
        "has_docs": docs_dir.is_dir() or doc_dir.is_dir(),
        "has_architecture": (docs_path / "architecture.md").exists(),
        "has_spec": (docs_path / "spec.md").exists(),
        "has_verification_doc": (docs_path / "verification.md").exists(),
        "has_progress_tracker": (root / "progress-tracker.json").exists()
        or (docs_path / "progress-tracker.json").exists()
        or (docs_path / "progress.json").exists(),
        "has_knowledge_catalog": (docs_path / "knowledge-catalog.md").exists()
        or (docs_path / "knowledge.md").exists(),
        "has_decisions": (docs_path / "decisions").is_dir()
        or (docs_path / "pending-decisions.md").exists(),
        "has_debt": (docs_path / "debt.md").exists(),
        "has_reviews": (docs_path / "reviews").is_dir(),
        "has_ci": (root / ".github" / "workflows").is_dir(),
        "has_runtime_entry": _exists_any(root, RUNTIME_FILES),
        "has_init_script": (root / "init.sh").exists(),
        "git": _git_status(root),
    }

    warnings: list[str] = []
    if not agent_files:
        warnings.append("missing project instruction file")
    for name, lines in agent_line_counts.items():
        if lines > 150:
            warnings.append(f"{name} is {lines} lines; consider splitting into docs")
    if not report["has_docs"]:
        warnings.append("missing docs/ or doc/")
    if not report["has_progress_tracker"]:
        warnings.append("missing progress tracker")
    if not report["has_verification_doc"] and not report["has_init_script"]:
        warnings.append("missing explicit verification doc or init.sh")
    if report["git"]["dirty_count"] and not report["git"]["meta_only"]:
        warnings.append("worktree has non-metadata changes")

    report["warnings"] = warnings
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".", help="repository path to audit")
    parser.add_argument("--pretty", action="store_true", help="pretty-print JSON")
    args = parser.parse_args()

    report = audit_repo(Path(args.path))
    print(json.dumps(report, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
