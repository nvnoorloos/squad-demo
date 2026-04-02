# FastAPI Aggregate Stats Endpoint

## Pattern

When adding aggregate endpoints to the demo backend, keep counting logic in `backend/app/store.py`, return a dedicated Pydantic response model from `backend/app/models.py`, and place literal routes before dynamic `/{id}` routes in `backend/app/main.py`.

## Why

This keeps API contracts explicit, avoids route shadowing, and lets tests verify the endpoint through the public HTTP surface while the store remains the single source of truth.

## Example

- `TaskStats` defines `total`, `by_status`, and `by_assignee`
- `get_stats()` uses the in-memory task store to build counts
- `GET /api/tasks/stats` returns `store.get_stats()`
