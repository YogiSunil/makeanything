from __future__ import annotations

from fastapi.testclient import TestClient

from studyflow.app import app


def test_home_page_renders():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    assert "StudyFlow Coach Studio" in response.text
    assert "Planning Studio" in response.text


def test_api_plan_returns_valid_payload():
    client = TestClient(app)

    response = client.post(
        "/api/plan",
        json={
            "prompt": "plan my final project",
            "docs": ["spec.md::Return at least 5 tasks with fallback"],
        },
    )

    payload = response.json()
    assert response.status_code == 200
    assert len(payload["checklist"]) >= 5
    assert "is_valid" in payload
    assert "used_fallback" in payload
