---
title: "I Built an Open-Government Data Dashboard That's Actually Accessible — FastAPI + Census API + WCAG"
published: false
description: "CivicPulse fetches real U.S. Census Bureau data, caches it with a TTL layer, and renders it with Chart.js — all while meeting WCAG 2.1 AA accessibility standards."
tags: python, fastapi, accessibility, datascience
cover_image: ""
canonical_url:
---

There's a lot of government data out there. The U.S. Census Bureau alone has hundreds of API endpoints. The problem is, nobody can use them — the raw responses are arrays of arrays keyed by FIPS codes, the docs are a maze, and the data is impossible to interpret without context.

I built **CivicPulse** to solve that: a dashboard that fetches real Census data, normalizes it into something readable, caches it so you're not hammering a government API, and renders it with interactive charts. And it's accessible — actually accessible, not "we added alt text and called it a day" accessible.

---

## What it does

CivicPulse pulls two metrics from the ACS 5-Year API:
- **Total population** per state (`B01003_001E`)
- **Median household income** per state (`B19013_001E`)

These get normalized from raw FIPS-coded arrays into clean state-level records, cached in memory, and visualized with Chart.js bar charts + an accessible data table.

---

## Architecture

```
Census Bureau ACS API
        ↓
httpx async client
        ↓
TTL in-memory cache
        ↓
FastAPI router
        ↓
Jinja2 templates + Chart.js
```

### The cache layer

The cache is a TTL-based in-memory store. When you request data, it checks if the cached version is still fresh. If yes, returns it instantly. If not, fetches from the Census API, normalizes, caches, and returns.

Why not Redis? Because this is a single-service app serving a dashboard. Redis adds a container, a connection, and a failure mode for something that a Python dict with timestamps handles just fine. Know when to use infrastructure and when a data structure is enough.

### The async client

The Census API can be slow. Using `httpx` with async makes the FastAPI endpoints non-blocking — if one request is waiting on the Census Bureau, others can still be served.

---

## The accessibility story

This is the part that matters most to me. Most dashboards are inaccessible — they throw a canvas chart on the screen and call it done. Screen readers can't read canvas content. Keyboard users can't interact with it.

CivicPulse implements WCAG 2.1 AA compliance:

| Feature | Implementation |
|---|---|
| **Skip navigation** | Hidden link at the top jumps past the nav |
| **Semantic landmarks** | `<main>`, `<nav>`, `<header>`, `<footer>` |
| **ARIA live regions** | Data updates announce themselves to screen readers |
| **Data tables** | Chart data is also available as a sortable HTML table |
| **Keyboard navigation** | All interactive elements are reachable via Tab |
| **Sufficient contrast** | Color choices meet AA contrast ratios |

Why does this matter for a portfolio? Because accessibility is a legal requirement (ADA, Section 508) and a competitive advantage. If you can tell an interviewer you implemented ARIA live regions and skip-nav links, you're demonstrating awareness that most developers don't have.

---

## CI/CD pipeline

The project runs CI on every push:

1. **Linting** — code style checks
2. **Tests** — pytest with HTTPX for async endpoint testing
3. **SAST** — static analysis security testing
4. **Secret scanning** — prevent accidental credential commits
5. **Docker build** — verify the container builds cleanly

Security is a first-class CI concern, not an afterthought. The SAST and secret scanning jobs run *before* the code can be merged.

---

## Docker deployment

```bash
docker compose up --build
```

One command, the app is running. The Dockerfile is multi-stage for a clean production image.

---

## What I'd improve

- **More Census variables** — education levels, poverty rates, age distributions
- **State-level drill-down** — click a state to see county-level data
- **Historical comparison** — compare current year to 5 years ago
- **Export** — CSV/PDF download of the visualized data
- **Map visualization** — choropleth map instead of just bar charts

---

## The honest takeaway

This isn't a revolutionary project. It's a dashboard. But it demonstrates things that matter:

1. **API integration with real external services** — not mock data
2. **Caching strategy** — understanding when to cache and how long
3. **Accessibility compliance** — WCAG 2.1 AA, not just "we tried"
4. **CI/CD with security gates** — SAST and secret scanning in the pipeline
5. **Containerized deployment** — Docker Compose, reproducible builds

For a cybersecurity student, showing that you build accessible, secure, well-tested web applications is a differentiator.

---

*Source: [github.com/SSH-PuR66/CivicPulse](https://github.com/SSH-PuR66/CivicPulse)*
