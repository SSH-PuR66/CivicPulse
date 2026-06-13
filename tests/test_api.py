from fastapi.testclient import TestClient

from app.main import app
from app.services import census

client = TestClient(app)

FAKE_STATES = [
    {"name": "California", "population": 39000000, "median_income": 84000, "fips": "06"},
    {"name": "Texas", "population": 29000000, "median_income": 67000, "fips": "48"},
]


def test_health():
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


def test_states(monkeypatch):
    async def fake_fetch():
        return FAKE_STATES

    monkeypatch.setattr(census, "fetch_state_data", fake_fetch)
    res = client.get("/api/states")
    assert res.status_code == 200
    body = res.json()
    assert body["count"] == 2
    assert body["states"][0]["name"] == "California"


def test_states_upstream_failure(monkeypatch):
    async def failing_fetch():
        raise RuntimeError("boom")

    monkeypatch.setattr(census, "fetch_state_data", failing_fetch)
    res = client.get("/api/states")
    assert res.status_code == 502


def test_dashboard_page():
    res = client.get("/")
    assert res.status_code == 200
    assert "CivicPulse" in res.text
