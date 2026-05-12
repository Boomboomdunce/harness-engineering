# Handoff Artifact Template

> Write this artifact when ending a session during long-running work.
> The next session will start by reading this file to get up to speed.

---

# Session Handoff

## Date
[YYYY-MM-DD HH:MM]

## Session Summary
[2-3 sentences: what was accomplished this session]

## Current State

### What Is Working
- [Feature/component]: [status — fully working, partially working]
- [Feature/component]: [status]

### What Is Not Working
- [Feature/component]: [what's broken and why]
- [Feature/component]: [what's broken and why]

### What Was Left In Progress
- [Feature/component]: [what was started, what remains]

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| [Decision 1] | [Why this choice was made] |
| [Decision 2] | [Why this choice was made] |

## Reusable Knowledge Extracted
| Candidate | Type | Scope | Evidence | Suggested Maturity |
|-----------|------|-------|----------|--------------------|
| [Knowledge candidate 1] | `model`/`decision`/`guideline`/`pitfall`/`process` | [Where it applies] | [Code/test/user feedback/session result] | `draft`/`verified` |
| [Knowledge candidate 2] | `model`/`decision`/`guideline`/`pitfall`/`process` | [Where it applies] | [Code/test/user feedback/session result] | `draft`/`verified` |

## Knowledge Updates Needed
- [ ] Add or update [knowledge entry path] because [reason]
- [ ] Downgrade or remove [stale entry path] because [reason]

## Known Issues
| Issue | Severity | Notes |
|-------|----------|-------|
| [Issue 1] | [Critical/High/Medium/Low] | [Context] |
| [Issue 2] | [Critical/High/Medium/Low] | [Context] |

## Next Actions (Priority Order)
1. [Highest priority next step — be specific]
2. [Next step]
3. [Next step]

## Verification Status
| Feature | Tests Pass | E2E Verified | Notes |
|---------|-----------|-------------|-------|
| [Feature 1] | ✅/❌ | ✅/❌ | [any notes] |
| [Feature 2] | ✅/❌ | ✅/❌ | [any notes] |

## Git State
- Latest commit: [hash] [message]
- Branch: [branch name]
- Uncommitted changes: [yes/no — should be no]

## Environment Notes
[Anything the next session needs to know about the environment — ports in use, external service state, database contents, etc.]
