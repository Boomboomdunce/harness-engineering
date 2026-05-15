# Harness Engineering Ecosystem

> A curated collection of key resources, articles, and projects in the harness engineering space.

## Foundational Articles

### OpenAI

| Resource | Description |
|----------|-------------|
| [Harness Engineering: Leveraging Codex in an Agent-First World](https://openai.com/index/harness-engineering/) | The original article defining harness engineering. 3-person team, 5 months, ~1M lines of agent-generated code, ~1500 PRs. Introduces the six core concepts. |

### Anthropic

| Resource | Description |
|----------|-------------|
| [Harness Design for Long-Running Application Development](https://www.anthropic.com/engineering/harness-design-long-running-apps) | GAN-inspired three-agent architecture (Planner → Generator → Evaluator). Sprint contracts, context anxiety, evaluator calibration, and harness simplification as models improve. |
| [Effective Harnesses for Long-Running Coding Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Two-part harness: initializer agent + coding agent. Feature list in JSON, incremental progress, structured handoffs via progress files and git history. |
| [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) | Core principle: "find the simplest solution possible, and only increase complexity when needed." |
| [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Context window management, compaction strategies, and progressive disclosure. |

### Martin Fowler / Thoughtworks

| Resource | Description |
|----------|-------------|
| [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) | Birgitta Böckeler's three-layer framework: Context Engineering → Architectural Constraints → Garbage Collection Agents. Four hypotheses on the future: harness as service template, stricter constraints → more autonomy, tech stack convergence toward AI-friendly choices, pre/post-AI application split. Critiques OpenAI's original for underemphasizing functional correctness verification. |

### LangChain

| Resource | Description |
|----------|-------------|
| [Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) | Defines Agent = Model + Harness. Introduces context rot, the Ralph loop mechanism, model-harness coupling (models overfit to specific harnesses), and progressive disclosure via skills. Terminal Bench 2.0 finding: pure harness optimization moved from Top 30 → Top 5. |

### HumanLayer

| Resource | Description |
|----------|-------------|
| [Skill Issue: Harness Engineering for Coding Agents](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents) | Defines 6 configuration levers: AGENTS.md (≤60 lines), MCP Servers, Skills, Sub-Agents, Hooks, Back-Pressure. Key insight: "the model is probably fine — it's just a skill issue." Cheap models for subtasks, expensive models for orchestration. |

### Mitchell Hashimoto

| Resource | Description |
|----------|-------------|
| [My AI Adoption Journey: Engineer the Harness](https://mitchellh.com/writing/my-ai-adoption-journey#step-5-engineer-the-harness) | Early articulation of "engineer the harness" concept. Focus on how to set up the environment so AI coding agents succeed — constraints, tooling, and feedback loops as the engineer's primary output. |

### YDD / Efficiency Paradox

| Resource | Description |
|----------|-------------|
| [Efficiency Paradox in AI-Assisted Development](https://yentingchen.com/ydd-efficiency-paradox/) | AI as NCX-10 (Theory of Constraints metaphor). Distinguishes Spec vs Rule vs Skill (loading mechanism distinction). Swiss cheese model for multi-layer verification defense. "Washing machine paradox" — speed gain enables capability evolution, not just time saving. Key insight: single-task speed isn't the bottleneck; inability to parallelize is. |

## Open-Source Projects

### Ralph Pattern

The "Ralph Wiggum loop" is one of the core implementation patterns for harness engineering: agents work in a loop, each iteration starting with fresh context, reading state from disk, doing one unit of work, and exiting cleanly.

| Project | Stars | Description |
|---------|-------|-------------|
| [snarktank/ralph](https://github.com/snarktank/ralph) | 13.6k+ | Original Ralph: bash script that repeatedly launches AI agents. Each iteration clears context, reads the plan, does work, commits. Six core tenets: Fresh Context, Backpressure, Plan Is Disposable, Disk Is State, Steer With Signals, Let Ralph Ralph. |
| [ralph-orchestrator](https://mikeyobrien.github.io/ralph-orchestrator/) | 2.3k+ | Rust evolution: Hat role system, event-driven coordination, multi-backend (Claude/Kiro/Gemini/Codex), backpressure gating, persistent memory. |
| [bmad-ralph](https://github.com/qianxiaofeng/bmad-ralph) | — | BMAD methodology + Ralph: parallel Claude Code worktrees, three-layer self-healing (retry → restart → diagnose), SQLite state machine. |

### Community Collections

| Project | Description |
|---------|-------------|
| [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) | Comprehensive curated list of articles, playbooks, benchmarks, specifications, and open-source projects for harness engineering. |
| [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) | Learning archive: concept notes, independent thinking, practice projects, and prompt collections for harness engineering. |

## Agent Skills Specification

| Resource | Description |
|----------|-------------|
| [Agent Skills Quickstart](https://agentskills.io/skill-creation/quickstart) | How to create skills in the open format |
| [Agent Skills Specification](https://agentskills.io/specification) | Full specification for the SKILL.md format |
| [Codex Skills Docs](https://developers.openai.com/codex/skills) | OpenAI Codex skill discovery and usage |
| [Claude Code Skills Docs](https://code.claude.com/docs/en/skills) | Anthropic Claude Code skill discovery and usage |

## Key Concepts Mapping

### Six Core Concepts (OpenAI)

| Concept | Description |
|---------|-------------|
| Repository as system of record | Everything the agent needs is in the repo — Slack, docs, and human memory don't count |
| Map, not encyclopedia | AGENTS.md is a ~100-line directory, not a knowledge dump. Progressive disclosure. |
| Mechanical enforcement | Lint rules and CI checks, not prose rules. Error messages embed fix instructions. |
| Agent readability | Choose boring tech. Reimplement subsets over wrapping opaque upstream. Git worktree support. |
| Throughput changes merge | Short PR lifecycles. Fix-forward over gate-keeping. Agent throughput exceeds human attention. |
| Entropy management | Agents replicate existing patterns including bad ones. Encode golden rules. Regular quality audits. |

### Ralph Six Tenets → Harness Engineering

| Ralph Tenet | Harness Engineering Concept |
|-------------|---------------------------|
| Fresh Context Is Reliability | Agent readability — each iteration reads fresh state |
| Backpressure Over Prescription | Mechanical enforcement — gate results, don't script steps |
| The Plan Is Disposable | Entropy management — regeneration costs one planning loop |
| Disk Is State, Git Is Memory | Repository as system of record — files are the handoff |
| Steer With Signals, Not Scripts | Human steers, agent executes — add guardrails, not instructions |
| Let Ralph Ralph | Agent autonomy — sit on the loop, not in the loop |

### Anthropic Three-Agent Pattern

| Agent | Role | Key Behavior |
|-------|------|-------------|
| Planner | Expand intent → full spec | Ambitious scope, high-level implementation, AI feature integration |
| Generator | Build one feature at a time | Incremental commits, self-evaluate per sprint, respect the contract |
| Evaluator | Test the running product | Skeptical by default, concrete failures, threshold-based pass/fail |

## Related Practices

| Practice | Relationship to Harness Engineering |
|----------|-------------------------------------|
| Context Engineering | How to manage information flow to and from agents |
| Prompt Engineering | How to instruct agents effectively within the harness |
| Evaluation Engineering | How to build reliable evaluators for agent output |
| Agent Orchestration | How to coordinate multiple agents and manage handoffs |
| Observability Engineering | How to make applications legible to agents |

### Martin Fowler Three-Layer Framework

| Layer | Description | Examples |
|-------|-------------|----------|
| Context Engineering | What the model sees | AGENTS.md, progressive disclosure, structured prompts, conversation management |
| Architectural Constraints | What the model is allowed to do | Module boundaries, dependency rules, lint enforcement, CI gates, type systems |
| Garbage Collection Agents | What cleans up after the model | Entropy detection, pattern drift correction, stale doc removal, refactoring sweeps |

### Four Forward-Looking Hypotheses (Böckeler)

| Hypothesis | Implication |
|------------|------------|
| Harness as future service template | Today's harness patterns will evolve into standardized project templates |
| Stricter constraints → more autonomy | Counterintuitively, narrowing the solution space makes agents more reliable |
| Tech stack convergence | Teams will select technologies partly based on AI-friendliness |
| Pre-AI / Post-AI application split | Existing codebases and greenfield AI-native codebases will follow different patterns |

### HumanLayer Six Levers

| Lever | Key Insight |
|-------|-------------|
| AGENTS.md | ≤60 lines. Beyond that, effectiveness drops. |
| MCP Servers | Trust boundary — only expose what the agent needs. Too many tools fill context. |
| Skills | Progressive loading — load on demand, not upfront. |
| Sub-Agents | Context firewalls — each gets only the context it needs. Use cheap models for subtasks. |
| Hooks | Success: silent. Failure: loud and actionable. |
| Back-Pressure | The primary quality mechanism — tests, linters, structural checks. |

### LangChain Agent Anatomy

| Concept | Description |
|---------|-------------|
| Agent = Model + Harness | The harness is everything around the model: system prompts, tools, skills, sandbox, orchestration, hooks |
| Context Rot | Performance degrades as the context window fills with stale information |
| Model-Harness Coupling | Models can overfit to specific harnesses — test with different configurations |
| Ralph Loop | Fresh context → read state → do work → commit → exit cleanly |
| Terminal Bench 2.0 | Pure harness optimization moved from Top 30 → Top 5, demonstrating harness impact |
