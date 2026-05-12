# Playbook: Knowledge Governance

> Use this playbook when repository work should improve the team's reusable knowledge, not just complete the immediate task.

## Goal

Harnesses make agents reliable in the moment. Knowledge makes agents better over time. Treat each delivery session as a chance to consume existing knowledge and extract new reusable knowledge.

## Knowledge Types

Use a small taxonomy so agents can find the right material quickly:

| Type | Purpose | Example |
|------|---------|---------|
| `model` | How the domain or system works | Billing lifecycle, security boundary, data flow |
| `decision` | Why a tradeoff was chosen | Chose SQLite for local-first sync |
| `guideline` | Rule agents should follow | API handlers validate input before service calls |
| `pitfall` | Known failure mode | Migration fails if seed data is stale |
| `process` | Repeatable workflow | Release checklist, incident review steps |

## Maturity Levels

| Level | Meaning | Promotion Signal |
|-------|---------|------------------|
| `draft` | Captured from one session; useful but unproven | Clear source and scope |
| `verified` | Checked against code, docs, or repeated use | Survived review or validation |
| `proven` | Reused successfully across multiple tasks | Multiple references or outcomes |

Do not mark knowledge `proven` because it sounds correct. It must have evidence.

## Retrieval Flow

Use progressive disclosure:

1. Read the project instruction file for the knowledge map.
2. Read the catalog for relevant entries only.
3. Open full entries only when their scope matches the task.
4. Ignore stale or low-confidence entries unless they explain a risk.

Keep the context budget explicit. Loading every knowledge entry defeats the harness.

## Work Loop

### At Startup

1. Read `AGENTS.md`, `CLAUDE.md`, or equivalent.
2. Check whether a knowledge catalog exists.
3. Pull only entries relevant to the current task, module, or risk.
4. Record which entries influenced the plan.

### During Work

1. If existing knowledge is wrong, note the contradiction.
2. If a decision is made, capture the tradeoff and evidence.
3. If a failure mode appears, capture a pitfall with reproduction or symptoms.
4. If a workflow repeats, capture it as a process.

### At Handoff Or Archive

1. Add candidate entries to the handoff artifact.
2. Promote only entries with evidence.
3. Update the catalog with tags, scope, maturity, and source links.
4. Remove or downgrade stale entries that misled the work.

## Recommended Files

For small repositories, keep this lightweight:

```text
docs/
├── knowledge-catalog.md
└── knowledge/
    ├── decisions/
    ├── guidelines/
    ├── pitfalls/
    ├── models/
    └── processes/
```

For very small projects, a single `docs/knowledge.md` is enough. Add structure only when it reduces search cost.

## Quality Bar

Good knowledge entries are:

- scoped to a system, module, workflow, or decision
- sourced from code, tests, incidents, user feedback, or repeated delivery
- short enough to read in one pass
- linked from a catalog
- clear about maturity and last review date

## Anti-Patterns

- treating a one-off observation as a universal rule
- storing critical knowledge only in chat or tickets
- loading the whole knowledge base into every session
- letting stale knowledge override current code
- capturing vague advice without evidence or scope
