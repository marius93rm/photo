---
name: branch-finish
description: Use before handing off, committing, or opening a PR to make sure a development branch is coherent and verified.
---

# Branch Finish

Use this skill to close a work session cleanly.

## Workflow

1. Inspect `git status --short --branch`.
2. Review the diff for accidental files, secrets, generated noise, and scope creep.
3. Run targeted verification based on changed behavior.
4. Update docs or notes only when the change creates a real maintenance need.
5. Summarize changes, checks, skipped checks, and residual risk.
6. If committing, use a concise message tied to user-visible or repo-visible behavior.

## Guardrails

- Do not stage unrelated user changes.
- Do not hide failing checks.
- Do not claim completeness without verification.

