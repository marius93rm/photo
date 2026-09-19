---
name: evidence-qa
description: Use when implementation claims need proof through screenshots, logs, test output, or direct reproduction.
---

# Evidence QA

Use this skill to avoid unsupported completion claims.

## Workflow

1. List the claims that need proof.
2. Choose direct evidence for each claim: command output, screenshot, trace, log, rendered page, or test.
3. Capture evidence and compare it to the requirement.
4. Report what passed, failed, and remained unverified.

## Evidence Rules

- For UI: capture desktop and mobile screenshots when feasible.
- For commands: include the command and result summary.
- For bugs: include reproduction steps and observed behavior.
- For docs/config: validate file shape, links, or syntax where possible.

## Output

| Claim | Evidence | Result | Gap |
| --- | --- | --- | --- |

Do not say "works" unless the evidence directly supports it.

