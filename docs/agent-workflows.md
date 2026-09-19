# Agent Workflows

This repository uses Paseo as the orchestration layer and Codex as the primary coding agent runtime. Keep orchestration lightweight and explicit.

## Default Single-Agent Flow

Use one Codex agent for most work:

1. Read `AGENTS.md`.
2. Explore the relevant repo surface.
3. Implement the smallest safe change.
4. Verify.
5. Report changes and residual risk.

Escalate to Paseo only when parallelism or a second perspective reduces risk.

## Local Specialist Flow

Before using Paseo, consider whether a repo-local Codex subagent is enough:

1. Use `context_manager` to gather a compact packet for unfamiliar code.
2. Use one implementation specialist for a scoped build task.
3. Use one or two review specialists for the risky part of the diff.
4. Use `evidence_collector` when the final claim needs screenshots, logs, or command proof.

Good examples:

- React change: `frontend_developer`, then `react_reviewer` and `accessibility_tester`.
- Backend write path: `backend_developer`, then `security_auditor` and `database_reviewer`.
- AI workflow: `eval_engineer`, then `reviewer` for the implementation.
- Narrow bug: `debugger`, then `test_automator`.

Do not call five agents when one specialist plus verification is enough.

## Advisor

Use an advisor for a second opinion without delegating the work.

Good fits:

- architecture tradeoffs
- uncertain bug root cause
- security-sensitive design
- reviewing a plan before implementation

Expected output:

- concise critique
- missing risks
- preferred option with rationale

## Committee

Use a committee for hard planning problems, repeated failures, or risky cross-cutting changes.

Good fits:

- stalled debugging
- unclear product or architecture direction
- high-blast-radius refactors
- conflicting requirements

Expected output:

- root-cause analysis
- decision-ready plan
- risks and verification strategy

## Handoff

Use handoff only when another agent should continue the work with full context.

The handoff must include:

- user goal
- current repo state
- files changed or inspected
- commands run and results
- open questions
- next concrete step

Do not hand off vague intent.

## Loop

Use loops only with explicit acceptance criteria and a stop condition.

Good loop criteria:

- a test passes
- a command returns clean
- a rendered UI matches stated checks
- a reviewer finds no blocking issues

Bad loop criteria:

- "make it better"
- "keep trying"
- "finish everything"
- subjective quality without a verifier

## Subagent Discipline

Codex subagents are useful for parallel investigation and review, but they increase token use and coordination overhead. Use narrow prompts, bounded scope, and read-only sandboxes for analysis roles.

Use `docs/agent-catalog.md` as the activation matrix. If a role is not listed there, prefer the main agent unless the task clearly needs a temporary specialist.

Use `docs/model-routing.md` for the checked-in Sol, Terra, and Luna defaults. Override a model only when the task's ambiguity, risk, volume, or output contract differs materially from the role's normal workload.
