---
name: design-system-extraction
description: Use when extracting, documenting, auditing, or reconciling a frontend codebase's visual language and design tokens into a durable DESIGN.md.
---

# Design System Extraction

Use this skill to turn scattered frontend evidence into a semantic design contract without requiring the app to build.

This repo-local workflow is informed by `google-labs-code/stitch-skills`, commit `0337446dadde6f8c94210444e2aa9d546126480f` (Apache-2.0), especially its source-first design-system extraction and `DESIGN.md` patterns. It is tool-agnostic: do not install Stitch, add credentials, or require an MCP server unless the user explicitly asks for that integration.

## Evidence Order

Prefer intentional sources before incidental overrides:

1. Token, theme, and component-library configuration.
2. Global CSS, font declarations, and framework configuration.
3. Repeated component and page patterns.
4. Rendered screenshots or browser inspection, when available.
5. Comments and history that explain design intent.

Record both the intended system and what actually ships when they differ.

## Workflow

1. Detect the framework, styling approach, entry points, and authoritative theme files.
2. Extract colors by semantic role; typography by family, scale, weight, leading, and tracking; spacing and sizing scales; shape, elevation, motion, layout, and breakpoints.
3. Sample important primitives and their hover, focus, active, disabled, loading, empty, error, and responsive states.
4. Consolidate near-duplicates only when their roles are genuinely equivalent. Preserve meaningful exceptions.
5. Translate raw values into functional language: describe what a token communicates and where it is used.
6. Cross-check against rendered behavior when feasible, then cite the files or screenshots supporting each major conclusion.

## DESIGN.md Contract

If the user requests a persistent artifact, update the repository's existing design document or create `DESIGN.md` at the root. Include:

- project identity, audience, atmosphere, density, and visual intent
- semantic color roles with exact values
- typography, spacing, shape, elevation, and motion rules
- component anatomy and interaction states
- layout, responsive, accessibility, and content rules
- approved exceptions and explicit anti-patterns
- confirmed facts, inferred patterns, and unresolved decisions as separate sections

Keep the document useful to both designers and implementers. Avoid raw CSS dumps, invented brand decisions, fabricated product data, and universal aesthetic bans that are not supported by the project.

## Verification

- Every exact value traces to a source file or rendered observation.
- Token names describe roles rather than hues alone.
- The document covers state and responsive behavior, not only the default desktop view.
- Existing conventions win over personal taste unless the user requested a redesign.
- Any generated or updated `DESIGN.md` is linked from the relevant project docs when it becomes a maintained contract.

