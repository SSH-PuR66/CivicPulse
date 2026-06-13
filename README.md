# CivicPulse

Live dashboard of U.S. Census ACS data (population & median household income by state).
Built with FastAPI, Chart.js, Docker, and GitLab CI/CD (SAST + secret detection).
WCAG-conscious: skip links, ARIA live regions, semantic tables.

## Quick start
1. `cp .env.example .env`
2. `pip install -r requirements.txt`
3. `uvicorn app.main:app --reload`
4. Open http://localhost:8000
