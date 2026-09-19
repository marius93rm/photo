---
name: design-taste-frontend
description: Anti-slop frontend skill for landing pages, portfolios, and redesigns. Use when a visual web surface needs stronger art direction, non-templated layout, better typography, spacing, motion, and a strict pre-flight design check.
---

# Design Taste Frontend

Repo-local adaptation of `Leonxlnx/taste-skill` default skill, install name `design-taste-frontend`.

Source: https://github.com/Leonxlnx/taste-skill
Verified commit: `5436c5952cc88d18a034d496988680a8c28a836a`
License: MIT, copyright 2026 Leonxlnx.

Use this skill for landing pages, portfolios, marketing pages, and redesigns where visual quality is the main risk. For dense dashboards, forms, and product workflows, prefer `frontend-taste` unless the user explicitly asks for a stronger visual redesign.

## Operating Mode

1. Read the brief before touching code.
2. State one design read: page kind, audience, vibe, and design-system family.
3. Set three dials: `DESIGN_VARIANCE`, `MOTION_INTENSITY`, and `VISUAL_DENSITY`.
4. Work with the existing stack and dependencies. Check manifests before importing libraries.
5. Build complete states and responsive layouts, not just the happy-path desktop.
6. Run a pre-flight audit before reporting completion.

## Design Read

Infer these signals:

- Page kind: landing, portfolio, redesign, editorial, product page, campaign page.
- Audience: buyer, recruiter, consumer, technical user, regulated/public-sector user.
- Vibe: calm, premium, playful, brutalist, editorial, trust-first, experimental, enterprise.
- References: screenshots, URLs, brands, existing assets, current design system.
- Constraints: accessibility, brand colors, legal/regulatory trust, performance, existing UI library.

If the design direction genuinely diverges, ask one clarifying question. Otherwise proceed with the best supported read.

## Dials

Default baseline:

- `DESIGN_VARIANCE: 7`
- `MOTION_INTENSITY: 5`
- `VISUAL_DENSITY: 4`

Adjust by context:

- Minimal, calm, Linear-style: variance 5-6, motion 3-4, density 2-4.
- Premium consumer or brand page: variance 7-8, motion 5-7, density 3-4.
- Agency, creative, Awwwards, experimental: variance 8-10, motion 7-9, density 3-5.
- Public-sector, regulated, trust-first: variance 3-4, motion 1-3, density 4-6.
- Redesign preserve: match the existing system, then improve spacing, hierarchy, and states.
- Redesign overhaul: increase variance and motion only where it does not harm usability.

## System Choice

Use one design foundation per project. If the brief maps to an official system, use the official package when available and already appropriate:

- Microsoft or enterprise SaaS: Fluent UI.
- Google or Material product: Material.
- IBM-style analytics: Carbon.
- Shopify admin: Polaris.
- Atlassian surfaces: Atlaskit.
- GitHub/devtool surfaces: Primer.
- UK public sector: GOV.UK Frontend.
- US public sector: USWDS.
- Owned modern SaaS: existing component system, shadcn/ui, Radix, or Tailwind, depending on the repo.

If the brief is aesthetic rather than system-driven, be explicit in the implementation: glass, bento, editorial, brutalist, dark tech, kinetic type, and similar styles are approximations, not official systems.

## Anti-Default Rules

- Avoid AI-purple gradients, centered dark mesh heroes, three equal feature cards, generic glassmorphism, and repeated split sections unless the brief truly calls for them.
- Do not use one-hue palettes. Pick one accent and audit consistency across the page.
- Do not default to beige/brass/espresso premium-consumer palettes unless the brand requires it.
- Avoid card spam. Use cards only when grouping or elevation communicates hierarchy.
- Avoid an eyebrow above every section. Use at most one small uppercase label per three sections.
- Do not repeat the same section layout family throughout a page.
- Do not put cards inside cards or section shells inside floating cards.
- Do not use placeholder Latin, generic names, generic metrics, or vague AI copy.

## Layout Checks

- Hero content fits the initial viewport. CTA is visible without scrolling.
- Desktop headline is planned with the asset size and should not sprawl into accidental four-line layouts.
- Navigation stays on one line on desktop or intentionally collapses.
- Multi-column sections have explicit mobile fallbacks.
- Bento grids have exactly as many cells as content requires and include real visual variation.
- Buttons do not wrap on desktop.
- Text fits its container at mobile and desktop widths.
- Use CSS Grid for multi-column structure; avoid brittle flex percentage math.
- Prefer `min-height: 100dvh` over `height: 100vh` for full-height sections.

## Interaction And State Checks

- Buttons have hover, focus-visible, and active states.
- Forms use labels above inputs, not placeholder-as-label.
- Loading, empty, and error states match the surrounding layout.
- Motion uses transforms and opacity, not layout properties.
- Respect reduced motion where animation is non-essential.
- Check contrast for buttons, forms, labels, helper text, and overlays.

## Pre-Flight Audit

Before saying the UI is done, inspect:

- Visual direction matches the design read.
- Palette has one coherent accent and no default AI-purple or repeated beige-craft fallback.
- Typography has a clear scale, readable body width, and no clipped display text.
- Section layouts vary intentionally and do not repeat a template rhythm.
- CTAs have distinct intent, consistent labels, and readable contrast.
- Responsive behavior works for the smallest supported viewport.
- Meaningful images have alt text; decorative images are marked appropriately.
- Imports exist in the project dependencies or the install command is reported.
- Build, lint, tests, or browser checks ran according to the change risk.
