---
name: code-review
description: Use when reviewing local diffs, PR changes, or subagent output for correctness, regressions, security, and missing tests.
---

# Code Review

Adopt a PR-review stance: findings first, evidence always.

## Workflow

1. Identify base and changed files with `git status`, `git diff`, or PR metadata.
2. Read surrounding code, not just hunks.
3. Prioritize bugs, regressions, security issues, data loss, and missing tests.
4. Run targeted checks when safe and available.
5. Report findings by severity with file and line references.

## Finding Template

```markdown
[SEVERITY] Title
File: path/to/file:line
Issue: What is wrong.
Impact: Why it matters.
Fix: Smallest recommended correction.
```

If no issues are found, state the reviewed scope and remaining risk.

