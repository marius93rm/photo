---
name: accessibility-audit
description: Use when auditing or improving web accessibility, keyboard navigation, screen reader support, or WCAG-oriented behavior.
---

# Accessibility Audit

Use this skill for practical accessibility review.

## Workflow

1. Identify the changed or target user flow.
2. Check keyboard navigation from start to finish.
3. Inspect semantic structure: landmarks, headings, labels, roles, names, and descriptions.
4. Check contrast, focus visibility, responsive text, and non-color indicators.
5. Test dynamic states: loading, errors, dialogs, menus, toasts, and validation.
6. Report barriers with user impact and smallest fix.

## Output

- scope audited
- blockers by severity
- evidence: file/line, screenshot, or reproduction step
- automated checks run, if any
- manual checks still needed

Prefer native HTML semantics before ARIA.

