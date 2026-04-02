from fastapi.testclient import TestClient

from app import store
from app.main import app


def test_get_task_stats_returns_seeded_counts():
    store.reset()

    with TestClient(app) as client:
        response = client.get("/api/tasks/stats")

    assert response.status_code == 200
    assert response.json() == {
        "total": 6,
        "by_status": {
            "todo": 2,
            "in-progress": 2,
            "done": 2,
        },
        "by_assignee": {
            "Keaton": 2,
            "McManus": 2,
            "Fenster": 1,
            "Hockney": 1,
        },
    }


def test_task_stats_update_after_task_changes():
    store.reset()

    with TestClient(app) as client:
        created = client.post(
            "/api/tasks",
            json={
                "title": "Add stats endpoint tests",
                "description": "Cover aggregate endpoint behavior",
                "status": "todo",
                "assignee": "McManus",
            },
        )
        task_id = created.json()["id"]

        response = client.get("/api/tasks/stats")
        assert response.status_code == 200
        assert response.json() == {
            "total": 7,
            "by_status": {
                "todo": 3,
                "in-progress": 2,
                "done": 2,
            },
            "by_assignee": {
                "Keaton": 2,
                "McManus": 3,
                "Fenster": 1,
                "Hockney": 1,
            },
        }

        updated = client.patch(
            f"/api/tasks/{task_id}",
            json={"status": "done", "assignee": "Fenster"},
        )
        assert updated.status_code == 200

        response = client.get("/api/tasks/stats")
        assert response.status_code == 200
        assert response.json() == {
            "total": 7,
            "by_status": {
                "todo": 2,
                "in-progress": 2,
                "done": 3,
            },
            "by_assignee": {
                "Keaton": 2,
                "McManus": 2,
                "Fenster": 2,
                "Hockney": 1,
            },
        }

        deleted = client.delete("/api/tasks/2")
        assert deleted.status_code == 204

        response = client.get("/api/tasks/stats")

    assert response.status_code == 200
    assert response.json() == {
        "total": 6,
        "by_status": {
            "todo": 2,
            "in-progress": 2,
            "done": 2,
        },
        "by_assignee": {
            "Keaton": 2,
            "McManus": 1,
            "Fenster": 2,
            "Hockney": 1,
        },
    }
