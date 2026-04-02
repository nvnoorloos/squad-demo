# McManus — History

## What I Know

- The backend is a FastAPI app in `/backend`
- Endpoints: GET/POST /api/tasks, GET/PATCH/DELETE /api/tasks/{id}, GET /api/health, GET /api/tasks/stats
- Task model: id, title, description, status (todo/in-progress/done), assignee
- In-memory store with seed data for demo purposes
- CORS configured for localhost:4321 (Astro dev server)
- Runs on port 8000 via uvicorn

## Learnings

- Added `GET /api/tasks/stats` in `backend/app/main.py`; define static routes before `/api/tasks/{task_id}` so FastAPI does not treat `stats` as a path parameter.
- Aggregate task-board stats live in `backend/app/store.py` via `get_stats()`, returning a `TaskStats` model from `backend/app/models.py`.
- Backend API tests now live in `backend/tests/` and run with `cd backend && .venv/bin/python -m pytest -q`.
- Seed data loading is idempotent in store.py so repeated FastAPI startup events do not duplicate demo data.
- store.py has a reset() function for test isolation.
- PR #3 merged. Issue #2 closed. Board is clear.
