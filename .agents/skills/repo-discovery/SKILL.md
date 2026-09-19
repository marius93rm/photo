---
name: repo-discovery
description: Use when starting unfamiliar repo work, onboarding, or preparing context before implementation. Focuses on evidence-first repository exploration.
---

# Repo Discovery

Use this skill before non-trivial changes in an unfamiliar or newly initialized project.

## Workflow

1. Inspect the root: `rg --files -uu`, `git status --short --branch`, and relevant manifests.
2. Read `AGENTS.md`, `README.md`, and task-relevant docs before source files.
3. Identify likely entry points, tests, build commands, config, and ownership boundaries.
4. Record confirmed facts, assumptions, and unknowns separately.
5. Stop once you have enough context to make the next decision.

## Output

Return a compact packet:

- task-relevant files and why they matter
- commands discovered for build, test, lint, or run
- constraints and conventions agents must preserve
- unresolved questions that cannot be answered from the repo

Avoid broad inventories that do not change execution.
