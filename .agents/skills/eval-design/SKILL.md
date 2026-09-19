---
name: eval-design
description: Use when prompts, AI features, retrieval, tools, or agent workflows need evaluation scenarios, rubrics, and regression gates.
---

# Eval Design

Use this skill to make AI behavior measurable.

## Workflow

1. Define the workflow and decision the eval must support.
2. Identify high-risk failure modes.
3. Create scenario coverage for happy path, edge cases, adversarial inputs, and tool failures.
4. Define scoring rubric, pass/fail threshold, and reviewer instructions.
5. Track cost, latency, and refusal/safety behavior where relevant.
6. Decide what requires human review or live validation.

## Output

- eval objective
- scenario matrix
- scoring rubric
- regression threshold
- dataset gaps
- rollout decision rule

Avoid vanity benchmarks that cannot change a ship/no-ship decision.

