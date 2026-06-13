"""Service layer for the U.S. Census ACS 5-Year API with in-memory TTL caching."""

import time

import httpx

from app.config import settings

# Census variable codes
VAR_POPULATION = "B01003_001E"   # Total population
VAR_MEDIAN_INCOME = "B19013_001E"  # Median household income

_cache: dict[str, tuple[float, list[dict]]] = {}


async def fetch_state_data() -> list[dict]:
    """Fetch population and median household income for all U.S. states.

    Results are cached in memory for settings.cache_ttl_seconds.
    """
    cache_key = "states"
    now = time.monotonic()

    if cache_key in _cache:
        cached_at, data = _cache[cache_key]
        if now - cached_at < settings.cache_ttl_seconds:
            return data

    params = {
        "get": f"NAME,{VAR_POPULATION},{VAR_MEDIAN_INCOME}",
        "for": "state:*",
    }
    if settings.census_api_key:
        params["key"] = settings.census_api_key

    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(settings.census_base_url, params=params)
        response.raise_for_status()
        rows = response.json()

    # First row is the header: ["NAME", "B01003_001E", "B19013_001E", "state"]
    data = [
        {
            "name": row[0],
            "population": int(row[1]) if row[1] else None,
            "median_income": int(row[2]) if row[2] else None,
            "fips": row[3],
        }
        for row in rows[1:]
    ]
    data.sort(key=lambda s: s["name"])

    _cache[cache_key] = (now, data)
    return data
