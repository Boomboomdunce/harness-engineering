# Playbook: Evidence-Driven Delivery

> Use this playbook when an agent session must produce a trustworthy project change, milestone, report, release gate, or research result.

## Goal

Convert a prompt into durable repository evidence. A task is not complete because the agent says it is complete; it is complete when the repository contains commands, artifacts, and review notes that let a fresh agent or human verify the claim later.

This playbook is useful for long-running feature work, release readiness, data or ML experiments, security-sensitive workflows, and any task where "looks done" is weaker than "provably done."

## Core Pattern

```text
Prompt → scope boundary → acceptance matrix → implementation → verification commands
       → evidence artifacts → review/audit note → progress update → handoff
```

Keep the chain in versioned files when possible. Chat logs are useful diagnostics, but they are not the source of truth.

## Phase 1: Restate Scope And Boundaries

Before implementing, write down:

- the active objective in one sentence
- what is explicitly out of scope
- what must not change
- what would block completion
- what artifact will prove the result

For risky systems, include non-authorization language. Example:

```text
This stage does not authorize production promotion, model or threshold changes,
external network execution, credential use, destructive data migration, or raw
sensitive samples in git.
```

## Phase 2: Build An Acceptance Matrix

Create a small table in a plan, review note, or sprint contract:

| Requirement | Evidence | Status |
|-------------|----------|--------|
| [Concrete requirement] | [Command, file, test, report, or artifact] | Pending |
| [Concrete requirement] | [Command, file, test, report, or artifact] | Pending |

Good evidence is specific and replayable:

- exact test or script command
- generated JSON/report path
- code path that enforces a boundary
- UI or API workflow checked end-to-end
- commit hash or clean `git status` when git state matters

Weak evidence:

- "the agent checked it"
- "the code looks correct"
- "the output seemed fine"
- screenshots without reproduction steps
- claims stored only in chat

## Phase 3: Verify Against Reality

Run the smallest command that proves each requirement, then run broader gates before completion.

For application work, prefer a layered sequence:

1. Static checks: format, lint, typecheck, schema validation.
2. Focused tests: the changed behavior or bug path.
3. Integration tests: database, API, worker, queue, or service boundary.
4. End-to-end checks: browser, CLI, or full user workflow.
5. Artifact validation: JSON reports, manifests, generated files, ignored lab outputs.

Record blocked verification explicitly. A blocked check is not a pass; it becomes a known issue or next action with the reason and expected unblock condition.

## Phase 4: Write A Review Or Audit Note

When the work is non-trivial, create a durable review note under a project-appropriate path such as:

```text
docs/reviews/YYYY-MM-DD-<topic>-review.md
docs/reviews/YYYY-MM-DD-<milestone>-audit.md
docs/<feature>/YYYY-MM-DD-<experiment>-report.md
```

The note should include:

- objective restatement
- scope and non-goals
- acceptance matrix
- commands run and outcomes
- evidence artifacts created or refreshed
- boundaries preserved
- residual risks or blockers
- next actions

Do not hide failed attempts. If a command failed and led to a fix or a better command, record the final meaningful failure when it matters for future agents.

## Phase 5: Update Progress And Knowledge

After evidence is recorded:

1. Update `progress-tracker.json`, checklist, or milestone tracker.
2. Add any new decision, pitfall, or process candidate to the handoff.
3. Update `docs/knowledge-catalog.md` if the knowledge is reusable.
4. Keep generated or sensitive evidence out of git when policy requires it, but record the ignored artifact path and validation command.

## Completion Gate

Before claiming completion, confirm:

- every acceptance row is `Passed`, `Blocked`, or `Out of scope`
- no row remains vague or unverified
- blocked rows include concrete next actions
- git status is understood
- docs and code agree on the current state
- sensitive or generated artifacts follow the repo's storage policy

If the active objective is blocked, say it is blocked. A well-proven blocker is a valid delivery outcome; pretending the goal is complete is not.

## Anti-Patterns

- marking a feature complete because tests pass while acceptance requirements remain unchecked
- overwriting blocked status with optimistic language
- treating ignored lab artifacts as if they are committed evidence without recording paths and checks
- using review notes as release notes without including commands and outcomes
- allowing one agent to implement, evaluate, and approve a risky change without a skeptical pass
