---
name: dependency-review
description: Use when adding, upgrading, auditing, or removing dependencies, packages, plugins, or external tools.
---

# Dependency Review

Use this skill to manage third-party risk.

## Workflow

1. Identify package manager, manifests, lockfiles, and runtime targets.
2. Explain why the dependency is needed and why existing code is insufficient.
3. Check license, maintenance health, security advisories, transitive risk, and bundle/runtime impact.
4. Prefer mature standard libraries or existing project dependencies when adequate.
5. Run install, audit, type/build, and focused tests as appropriate.

## Output

- recommendation: add, keep, upgrade, replace, or remove
- rationale and alternatives
- security/license/maintenance risk
- verification commands
- rollback path

Do not add dependencies for trivial helpers.

