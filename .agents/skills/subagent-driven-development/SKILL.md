---
name: subagent-driven-development
description: Use when a plan has independent workstreams that benefit from specialized Codex subagents or Paseo orchestration.
---

# Subagent-Driven Development

Use subagents deliberately when they reduce risk or isolate context.

## Workflow

1. Confirm there is a concrete plan with independent tasks.
2. Choose the smallest set of agents whose specialization changes quality.
3. Read `docs/model-routing.md` before overriding a checked-in agent model or reasoning effort.
4. Give each agent a bounded prompt: goal, files, constraints, allowed actions, expected output.
5. Keep review separate from implementation.
6. Integrate results in the parent session and verify the final repo state.

## Good Delegations

- `context_manager` maps an unfamiliar repo slice.
- `docs_researcher` verifies current API behavior.
- `security_auditor` inspects a trust boundary.
- `reviewer` reviews the final diff.
- `evidence_collector` gathers screenshots or command proof.

## Model Routing

- Keep Sol for ambiguous, cross-cutting, or high-impact work.
- Use Terra for bounded specialist reasoning, exploration, scans, and supporting synthesis.
- Use Luna only when scope, inputs, and the expected output are explicit and repeatable.
- Start with the configured reasoning effort; increase it only when complexity or failed verification warrants it.

## Guardrails

- Do not spawn agents just to look busy.
- Do not let agents make broad edits without a narrow target.
- Do not accept subagent claims without checking file diffs or evidence.
- Do not downgrade a task to a cheaper model when its scope or verifier is unclear.
- Use Paseo advisor/committee/loop only when its workflow fits the risk.

## Output

- agents used and why
- prompts or scope boundaries
- findings integrated
- final verification performed
