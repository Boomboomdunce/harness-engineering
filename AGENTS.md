# Repository Guidelines

## Project Structure & Module Organization

This repository packages the `harness-engineering` Agent Skill. The root `README.md` explains purpose, installation, and compatibility. Skill content lives in `harness-engineering/`:

- `SKILL.md`: main skill entry point, principles, and workflow router.
- `playbooks/`: task-specific workflows such as feature development, bug investigation, and refactoring.
- `templates/`: reusable artifacts such as `AGENTS.md.template`, handoff notes, rubrics, sprint contracts, and `progress-tracker.json`.
- `references/`: supporting ecosystem notes.

There is no application source tree, compiled asset pipeline, or test directory at present. Treat Markdown and JSON templates as the primary source.

## Build, Test, and Development Commands

- `rg --files`: list repository files quickly before editing.
- `sed -n '1,180p' harness-engineering/SKILL.md`: review the skill entry point and front matter.
- `python3 -m json.tool harness-engineering/templates/progress-tracker.json`: validate the JSON template.
- `git diff --check`: catch trailing whitespace and patch formatting issues before committing.
- `git status --short`: confirm the final change set is limited to intended files.

No formal build command is required. If a Markdown linter is available locally, run it on changed `.md` files, but do not introduce a new lint dependency just for small documentation edits.

## Coding Style & Naming Conventions

Use concise Markdown with clear headings and short, actionable paragraphs. Keep skill instructions navigational rather than encyclopedic; link to playbooks or templates instead of duplicating long guidance. Preserve existing naming patterns: lowercase kebab-case for playbooks, descriptive template names, and uppercase `SKILL.md` for the skill entry point.

Prefer ASCII punctuation in new files unless the surrounding file already uses Unicode. Avoid broad reformatting of unrelated Markdown.

## Testing Guidelines

Validate changed documents by reading them as an agent would: check that links and paths are accurate, commands are copy-pasteable, and instructions do not conflict with `SKILL.md`. For JSON changes, run `python3 -m json.tool` on the edited file.

## Commit & Pull Request Guidelines

Recent history uses Conventional Commits, for example `feat: comprehensive harness engineering skill upgrade` and `fix: add missing concepts from cross-reference verification`. Follow that style with focused subjects such as `docs: add contributor guide`.

Pull requests should describe the changed guidance, list affected files, and mention validation performed. Link related issues when available. Screenshots are not needed for text-only changes.

## Agent-Specific Instructions

Keep this repository agent-friendly. Make small, surgical edits, preserve the skill package layout, and avoid adding toolchain files unless they are required by the change being made.
