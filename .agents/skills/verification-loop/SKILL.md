---
name: verification-loop
description: Use before declaring work complete. Defines targeted build, test, lint, and manual verification expectations.
---

# Verification Loop

Use this skill before final reporting.

## Workflow

1. Identify the behavior changed and the failure modes most likely to matter.
2. Run the narrowest meaningful automated checks first.
3. Broaden checks when shared contracts, security, migrations, or user-facing flows changed.
4. Inspect failures instead of rerunning blindly.
5. Report checks run, checks skipped, and residual risk.

## Minimum Bar

- For docs/config-only changes: syntax and file-shape checks are usually enough.
- For code changes: run targeted tests and relevant lint/type checks when available.
- For UI changes: verify rendered behavior where feasible.
- For security-sensitive changes: include negative or failure-path validation where possible.

Never say "done" based only on intent.
