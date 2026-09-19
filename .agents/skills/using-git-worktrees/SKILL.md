---
name: using-git-worktrees
description: Use when feature work should be isolated from a dirty main workspace or when parallel Paseo/Codex workstreams need separate checkouts.
---

# Using Git Worktrees

Use worktrees to isolate risk without disturbing the user's current branch.

## Workflow

1. Detect whether the current checkout is already a linked worktree:
   `git rev-parse --git-dir` and `git rev-parse --git-common-dir`.
2. Check for a submodule before assuming linked-worktree status:
   `git rev-parse --show-superproject-working-tree`.
3. If not already isolated, ask before creating a new worktree unless the user already requested one.
4. Prefer project-local `.worktrees/` only if it is ignored.
5. Create a branch with a descriptive name and run baseline setup/checks.
6. Report the worktree path, branch, and baseline result.

## Guardrails

- Never create a worktree inside a tracked directory.
- Never use destructive git commands to clean the user's current work.
- If worktree creation is blocked, continue in place only after reporting the fallback.

## Quick Checks

```bash
git status --short --branch
git worktree list
git check-ignore -q .worktrees
```

