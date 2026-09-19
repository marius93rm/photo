---
name: performance-audit
description: Use when investigating latency, slow UI, bundle size, memory, database slowness, or Core Web Vitals.
---

# Performance Audit

Use this skill for measurement-led performance work.

## Workflow

1. Define the metric and threshold that matters.
2. Reproduce or collect evidence before optimizing.
3. Identify likely bottleneck category: algorithm, rendering, network, database, build, memory, or infrastructure.
4. Recommend changes by impact, confidence, effort, and risk.
5. Verify with the same metric where feasible.

## Checks

- Frontend: LCP, INP, CLS, bundle size, render churn, image loading.
- Backend: p95 latency, query count, slow queries, cache hit rate, payload size.
- Runtime: CPU, memory growth, event-loop blocking, concurrency limits.

Do not micro-optimize code without a plausible user or system impact.

