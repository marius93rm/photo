---
name: recent-research
description: Use when a decision depends on current information, market/community sentiment, recent releases, or external facts that may have changed.
---

# Recent Research

Use this skill when the answer may be time-sensitive or when recommendations depend on current external evidence.

## Workflow

1. State the exact question and time window.
2. When researching a product or vendor, start with its official documentation and dedicated documentation tools when available.
3. Prefer primary sources, official release notes, changelogs, issue trackers, and source repositories.
4. Use community sources only for sentiment, adoption clues, and reported pain points, or when the user explicitly requests them.
5. Separate facts, signals, and interpretation.
6. Include direct citations or links for claims that affect decisions.
7. Record the verification date, confidence, and documentation gaps.

## Guardrails

- Do not vendor heavy research tools into this repo.
- Do not treat social engagement as truth; treat it as a signal.
- Do not use stale memory for modern APIs, pricing, legal, security, or fast-moving product facts.
- Do not infer undocumented capabilities, availability, pricing, or migration requirements from model names.
