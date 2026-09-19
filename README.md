# marius93rm.github.io

Static photography portfolio for Marius, published with GitHub Pages.

## Site map

- `index.html` — landing page, selected work, profile, and contact form
- `people.html` — people and portrait gallery
- `wheels.html` — motorcycle and automotive gallery
- `world.html` — travel, landscape, and street gallery
- `contact.html` — contact details and Formspree form
- `assets/css/main.css` — shared visual system
- `assets/js/main.js` — navigation, scroll-to-top, and GLightbox initialization
- `assets/img/thumbs/` — optimized gallery thumbnails
- `assets/img/large/` — full-size lightbox images

The site uses vendored Bootstrap 5.3.3 and GLightbox. It has no dependency
installation or compilation step.

## Run locally

```bash
python3 -m http.server 8000
```

Open `http://127.0.0.1:8000/`.

## Validate

```bash
python3 scripts/validate_repo.py
```

The validator checks repo-local agent and skill configuration, required docs,
HTML links and assets, image alternative text, internal anchors, and baseline
`.gitignore` hygiene.

## Agent workspace

This project includes the curated repo-local operating layer from
[`marius93rm/unaSquadraFortissimi`](https://github.com/marius93rm/unaSquadraFortissimi):

- 22 specialist definitions in `.codex/agents/`
- 27 task-triggered skills in `.agents/skills/`
- project-specific rules in `AGENTS.md`
- selection and workflow guidance in `docs/`

Start with `AGENTS.md`, then consult `docs/agent-catalog.md` only when a task
benefits from a specialist. The configuration is intentionally repo-local and
does not require credentials or global installation.
