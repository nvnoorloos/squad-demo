# Verbal — History

## What I Know

- This is a two-component demo app: Astro frontend + FastAPI backend
- The app is a Kanban-style task board
- API contract: /api/tasks (list, create), /api/tasks/{id} (get, update, delete), /api/tasks/stats (stats)
- Task model: id, title, description, status, assignee
- The project exists to demonstrate Squad for a blog post
- Stack diversity (JS/TS + Python) creates natural role specialization

## Learnings

### Routing in Practice (Issue #2 Triage)
- Backend API endpoints → McManus (FastAPI, Python domain)
- Triage pattern: analyze issue, assign `squad:{member}` label, post scope comment with acceptance criteria
- Keep triage comments action-oriented — scope, acceptance, and next step

### PR #3 Review (Task Stats Endpoint)
- API contract now includes: GET /api/tasks/stats → { total, by_status, by_assignee }
- Route ordering matters in FastAPI: static paths (/stats) must precede parameterized paths (/{task_id})
- store.py has a reset() function for test isolation and seed() has an idempotency guard
- Dev deps (httpx, pytest) live in main requirements.txt — acceptable for demo scope
- Pre-existing deprecation: on_event should migrate to lifespan handlers eventually
- McManus delivered a clean first PR — thorough tests covering CRUD-driven stat changes
- PR #3 merged. Issue #2 closed. Board is clear.
