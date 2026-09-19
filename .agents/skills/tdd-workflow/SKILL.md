---
name: tdd-workflow
description: Use when implementing behavior that can be protected by tests, especially bug fixes and shared logic.
---

# TDD Workflow

Use this skill when tests can clarify behavior and prevent regressions.

## Workflow

1. Define the expected behavior in one sentence.
2. Write or identify a failing test that proves the current gap.
3. Run the test and confirm the failure is relevant.
4. Implement the smallest change that makes the test pass.
5. Run the focused test again.
6. Refactor only if it reduces real complexity.

## Guardrails

- Do not add broad test suites for narrow behavior.
- Do not change production code before understanding the expected failure.
- If no test harness exists, document the manual verification path and consider adding a minimal test only when the project shape supports it.
