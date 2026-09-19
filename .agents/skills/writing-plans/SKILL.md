---
name: writing-plans
description: Use when a feature, refactor, migration, or multi-file change needs a decision-complete implementation plan before editing.
---

# Writing Plans

Use this skill after discovery or brainstorming when execution needs sequencing.

## Workflow

1. Ground the plan in files, commands, and existing patterns.
2. Define goal, non-goals, acceptance criteria, and risk level.
3. Break work into phases where each phase can be verified.
4. Name affected files or modules when known.
5. Define tests, lint/type checks, migrations, browser checks, or manual validation.
6. Identify rollback or recovery path when production behavior changes.

## Plan Shape

```markdown
## Goal
## Non-Goals
## Affected Surface
## Implementation Steps
## Verification
## Risks and Rollback
## Assumptions
```

Keep plans executable. Avoid architecture that the current task does not need.

