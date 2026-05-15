# harness-engineering

`harness-engineering` is a portable Agent Skill that helps coding agents (Codex, Claude Code, and other compatible clients) follow best practices in product development and project modification.

The skill brings together insights from OpenAI's harness engineering paradigm, Anthropic's multi-agent research, and the community's Ralph pattern into actionable playbooks, templates, and principles that agents use automatically.

It also includes patterns from real long-running agent work: prompt-to-artifact evidence chains, explicit blocker handling, machine-readable progress tracking, and knowledge extraction from delivery sessions.

## What It Does

When triggered, this skill gives agents:

- **A startup audit** — fast harness check when entering any new repository
- **Workflow routing** — playbooks for common scenarios (new project, feature dev, long-running build, refactoring, bugfix)
- **Ready-to-use templates** — for instruction files, handoff artifacts, sprint contracts, evaluator rubrics, and progress tracking
- **Evidence-driven delivery** — a playbook for proving milestones, release gates, experiments, and risky changes with durable artifacts
- **Knowledge governance** — lightweight catalogs and entries for reusable decisions, pitfalls, processes, and domain models
- **Mechanical audit helper** — a small script for checking whether a repository exposes the basic harness surfaces agents need
- **Core principles** — repo as system of record, map not encyclopedia, separate planning/doing/judging, verify against reality, structured handoffs, incremental commits, knowledge governance, entropy management
- **Context engineering** — progressive disclosure, context resets vs compaction, fresh context reliability
- **Multi-agent patterns** — when and how to use planner/generator/evaluator architecture
- **Knowledge governance** — catalog-first retrieval, reusable knowledge entries, maturity levels, and handoff-driven capture

## Repository Layout

```text
harness-engineering/
├── README.md
├── .gitignore
└── harness-engineering/
    ├── SKILL.md                        # Core skill — principles, workflow router, guidance
    ├── playbooks/
    │   ├── new-project.md              # Greenfield project kickoff
    │   ├── feature-development.md      # Feature work in existing repo
    │   ├── long-running-build.md       # Multi-session autonomous builds
    │   ├── refactor-cleanup.md         # Refactoring and debt reduction
    │   ├── bugfix-investigation.md     # Bug investigation workflow
    │   ├── evidence-driven-delivery.md # Prompt-to-artifact evidence workflow
    │   └── knowledge-governance.md     # Reusable knowledge lifecycle
    ├── templates/
    │   ├── AGENTS.md.template          # Template for project instruction files
    │   ├── handoff-artifact.md         # Template for session handoffs
    │   ├── sprint-contract.md          # Template for sprint contracts
    │   ├── evaluator-rubric.md         # Template for evaluator criteria
    │   ├── progress-tracker.json       # Template for feature tracking (JSON)
    │   ├── knowledge-entry.md          # Template for reusable knowledge entries
    │   └── knowledge-catalog.md        # Template for catalog-first retrieval
    ├── scripts/
    │   ├── harness_audit.py            # Fast JSON audit of repo harness surfaces
    │   └── test_harness_audit.py       # Unit tests for harness_audit.py
    └── references/
        └── ecosystem.md               # Harness engineering ecosystem resources
```

## Install

Copy the `harness-engineering/` skill directory into the location your client scans for skills.

### Codex

Personal install:

```bash
mkdir -p ~/.codex/skills
cp -R harness-engineering ~/.codex/skills/
```

Project install:

```bash
mkdir -p /path/to/repo/.agents/skills
cp -R harness-engineering /path/to/repo/.agents/skills/
```

### Claude Code

Personal install:

```bash
mkdir -p ~/.claude/skills
cp -R harness-engineering ~/.claude/skills/
```

Project install:

```bash
mkdir -p /path/to/repo/.claude/skills
cp -R harness-engineering /path/to/repo/.claude/skills/
```

### GitHub Copilot CLI

Personal install:

```bash
mkdir -p ~/.copilot/skills
cp -R harness-engineering ~/.copilot/skills/
```

## Verify

Validate the skill folder:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py harness-engineering
python3 harness-engineering/scripts/test_harness_audit.py
```

After installing, ask the agent "what skills are available" or start a task that involves project setup, code review, or long-running development. The skill should trigger automatically.

To audit a target repository's harness surfaces:

```bash
python3 harness-engineering/scripts/harness_audit.py /path/to/repo --pretty
```

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Repo as system of record** | Everything the agent needs lives in the repo — Slack, tickets, and memory don't count |
| **Map, not encyclopedia** | Instruction files are ~100-line directories pointing to deeper docs |
| **Knowledge as moat** | Harness moves work through the system; typed, scoped, evidenced knowledge compounds across work |
| **Separate planning, doing, judging** | Don't let one agent spec, implement, and grade itself |
| **Make quality gradable** | Convert "make it better" into concrete, weighted criteria |
| **Verify against reality** | Test the running product, not just the code |
| **Evidence over claims** | Completion requires commands, artifacts, review notes, or explicit blockers |
| **Structured handoffs** | Context reset + handoff artifact beats a bloated session |
| **Knowledge compounds** | Reusable decisions, pitfalls, and processes should be cataloged with evidence |
| **Work incrementally** | One feature at a time, commit often, test each feature |
| **Manage entropy** | Agents replicate patterns — including bad ones. Encode good patterns as lint rules. |
| **Complexity earns its keep** | Every harness component is a claim the model can't do X. Stress-test those claims. |

## Playbooks

| Playbook | When to Use |
|----------|-------------|
| [New Project](harness-engineering/playbooks/new-project.md) | Starting from scratch — spec expansion, scaffold, incremental build |
| [Feature Development](harness-engineering/playbooks/feature-development.md) | Adding features to an existing codebase |
| [Long-Running Build](harness-engineering/playbooks/long-running-build.md) | Multi-hour/multi-session autonomous development |
| [Refactor & Cleanup](harness-engineering/playbooks/refactor-cleanup.md) | Tech debt, code cleanup, architectural improvement |
| [Bug Investigation](harness-engineering/playbooks/bugfix-investigation.md) | Reproduce → diagnose → test → fix → prevent |
| [Evidence-Driven Delivery](harness-engineering/playbooks/evidence-driven-delivery.md) | Proving milestones, release gates, experiments, and risky changes |
| [Knowledge Governance](harness-engineering/playbooks/knowledge-governance.md) | Capture, catalog, retrieve, and mature reusable project knowledge |

## Sources

This skill synthesizes:

- [OpenAI: Harness Engineering](https://openai.com/index/harness-engineering/) — the original paradigm
- [Anthropic: Harness Design for Long-Running Apps](https://www.anthropic.com/engineering/harness-design-long-running-apps) — three-agent architecture
- [Anthropic: Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — initializer + coding agent pattern
- [Ralph (snarktank/ralph)](https://github.com/snarktank/ralph) — iterative agent loop
- [Awesome Harness Engineering](https://github.com/walkinglabs/awesome-harness-engineering) — community resources
- [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) — learning archive and concept analysis
- [Harness不是目的，知识才是护城河](https://mp.weixin.qq.com/s/JV4-oPP0jjsBCZ4tW3Gy1g) — knowledge layering and delivery-team knowledge capture practice

## Compatibility

This repository follows the open Agent Skills format:

- Agent Skills quickstart: https://agentskills.io/skill-creation/quickstart
- Agent Skills specification: https://agentskills.io/specification
- Codex skills docs: https://developers.openai.com/codex/skills
- Claude Code skills docs: https://code.claude.com/docs/en/skills

## Contributing

Contributions welcome via Issues and PRs:

- Improve or add playbooks
- Enhance templates
- Add ecosystem references
- Share real-world experience reports
- Add reusable knowledge patterns with clear scope, evidence, and maturity

## License

This repository is licensed under the MIT License.
