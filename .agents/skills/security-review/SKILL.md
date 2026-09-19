---
name: security-review
description: Use for auth, secrets, input handling, dependency, config, infrastructure, or production-exposure review.
---

# Security Review

Use this skill when changes can affect trust boundaries or sensitive data.

## Workflow

1. Identify assets, actors, trust boundaries, and entry points.
2. Check authn/authz, input validation, output encoding, secret handling, and logging.
3. Inspect defaults for fail-open behavior.
4. Consider dependency, build, and deployment exposure.
5. Rank findings by impact, likelihood, and ease of exploitation.
6. Recommend practical mitigation and verification.

## Output

Each finding should include:

- evidence
- attack path or misuse path
- impact
- recommended fix
- verification step

Mark speculative risks as hypotheses.
