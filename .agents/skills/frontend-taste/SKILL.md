---
name: frontend-taste
description: Use when designing, building, reviewing, or improving frontend UI. Focuses on polished, non-generic interfaces with clear hierarchy and usable controls.
---

# Frontend Taste

Use this skill for frontend implementation, redesign, and UI review.

## Principles

- Build the actual usable experience first, not a marketing shell, unless the task is explicitly a landing page.
- Match visual density to the product. Operational tools should be quiet, organized, and scannable.
- Use established UI primitives: icons for tool buttons, toggles for binary settings, tabs for views, menus for option sets, sliders or inputs for numbers.
- Avoid generic one-hue palettes, decorative blobs, oversized cards, and empty hero sections.
- Ensure text fits at mobile and desktop widths.
- Use stable dimensions for boards, grids, toolbars, and repeated controls so state changes do not shift layout.

## Workflow

1. Read the existing `DESIGN.md`, theme, tokens, and representative components when present.
2. Turn the request into a compact brief: platform, page type, user task, content structure, visual direction, states, breakpoints, and constraints. Infer low-risk gaps; ask only when a missing choice materially changes the result.
3. Choose a restrained design direction that fits the domain and express colors, typography, spacing, and components by semantic role.
4. Implement complete controls and loading, empty, error, disabled, and success states.
5. Preserve real navigation and data boundaries. Replace dead placeholder links, and never invent metrics, customer claims, or realistic-looking product data.
6. Verify responsive layout, text fit, focus behavior, and visual fidelity against available references.
7. Review for hierarchy, spacing, contrast, interaction clarity, and drift from the established system.

For multi-screen work, keep shared navigation, tokens, and primitives consistent. Work in bounded screen-level increments and leave a concrete next task only when the user requested an iterative loop.

Do not add visible instructional text about how the interface is built unless the product genuinely needs it.
