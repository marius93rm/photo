---
name: incident-response
description: Use for production incidents, outages, regressions, degraded service, or urgent operational debugging.
---

# Incident Response

Use this skill to restore service and preserve evidence.

## Workflow

1. State impact, start time, affected users/systems, and current severity.
2. Freeze assumptions. Capture logs, metrics, traces, deploys, and recent changes.
3. Stabilize first: rollback, disable flag, scale, rate-limit, or isolate.
4. Identify likely root cause only after evidence supports it.
5. Verify recovery from the user or system perspective.
6. Record follow-ups separately from immediate mitigation.

## Output

- impact and timeline
- mitigation taken
- evidence gathered
- root cause or strongest hypothesis
- verification of recovery
- follow-up actions

Do not perform risky data changes without explicit approval and rollback notes.

