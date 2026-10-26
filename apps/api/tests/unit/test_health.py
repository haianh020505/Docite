"""tests/unit/test_health.py — Health endpoint smoke test.

Uses HTTPX TestClient; no database required.
Run:  pytest tests/unit/test_health.py -v
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert "version" in body


def test_health_schema():
    response = client.get("/health")
    body = response.json()
    assert set(body.keys()) == {"status", "version"}
