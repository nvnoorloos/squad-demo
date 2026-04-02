# McManus — History

## What I Know

- The backend is a FastAPI app in `/backend`
- Endpoints: GET/POST /api/tasks, GET/PATCH/DELETE /api/tasks/{id}, GET /api/health
- Task model: id, title, description, status (todo/in-progress/done), assignee
- In-memory store with seed data for demo purposes
- CORS configured for localhost:4321 (Astro dev server)
- Runs on port 8000 via uvicorn
