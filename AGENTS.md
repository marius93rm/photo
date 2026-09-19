# Agent Operating Contract

This repository contains the static photography portfolio published at
`https://marius93rm.github.io`. Keep changes small, accessible, fast, and safe
to deploy directly from `main` with GitHub Pages.

## Project Context

- The site is plain HTML, CSS, and JavaScript; there is no package manager or build step.
- Entry points are `index.html`, `people.html`, `wheels.html`, `world.html`, and `contact.html`.
- Shared styling lives in `assets/css/main.css`.
- Shared behavior lives in `assets/js/main.js`.
- Bootstrap 5.3.3 and GLightbox are vendored under `assets/vendor/`.
- Gallery thumbnails live under `assets/img/thumbs/`; lightbox originals live under `assets/img/large/`.
- Contact forms post to Formspree. Phone numbers and email addresses are public user content; do not change them without explicit evidence or direction.

## First Principles

- Read this file before non-trivial work.
- Explore the relevant files before asking questions; use local evidence first.
- Prefer `rg` and `rg --files` for search.
- Preserve user work and avoid unrelated refactors.
- Use `apply_patch` for focused text edits.
- Do not add frameworks, build tooling, analytics, remote fonts, or third-party services unless the task requires them.
- Verify before reporting completion. State what was checked and any residual risk.

## Implementation Conventions

- Keep the site deployable as static files from the repository root.
- Preserve relative links so pages work both on GitHub Pages and under a local HTTP server.
- Reuse the shared CSS and JavaScript instead of adding page-local copies.
- When adding a gallery image, provide both thumbnail and large WebP variants, descriptive English `alt` text, explicit dimensions, and lazy loading except for the first visible image.
- Keep the first visible gallery image preloaded, eager, and high priority; keep later images lazy.
- Maintain keyboard access, visible focus, semantic labels, and accessible names for icon-only controls.
- Treat mobile navigation, GLightbox, contact submission, and all five page-to-page links as shared behavior.
- Do not edit minified vendor files for application behavior; change the shared project files instead.

## Verification

Run the repository checks from the root:

```bash
python3 scripts/validate_repo.py
```

For UI work, serve the site over HTTP rather than opening files directly:

```bash
python3 -m http.server 8000
```

Then verify the affected page at `http://127.0.0.1:8000/`. Use the repo-local
`browser-integration` skill before in-app browser automation.

## Repo-Local Agents and Skills

- Codex agent definitions live in `.codex/agents/`; routing is configured in `.codex/config.toml`.
- Repo-local skills live in `.agents/skills/` and are loaded only when their trigger matches the task.
- Use `docs/agent-catalog.md` to select specialists and `docs/agent-workflows.md` for orchestration guidance.
- Most tasks should remain single-agent. Use specialists when they materially reduce risk or create independent evidence.
- Preserve the checked-in model defaults from `docs/model-routing.md` unless task evidence justifies an override.

Useful combinations for this project:

- unfamiliar area: `context_manager` with `repo-discovery`
- UI implementation: `frontend_developer`, then `accessibility_tester` or `reviewer` as warranted
- visual redesign: `design-system-extraction`, then one frontend taste skill
- defect: `debugger`, `systematic-debugging`, and focused verification
- performance or SEO-related image work: `performance_optimizer` plus evidence-based checks
- deployment/configuration: `devops_engineer`, then `verification-loop`

Do not spawn agents reflexively or modify global machine configuration, credentials,
telemetry, providers, or personal absolute paths in this repository.
