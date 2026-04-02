# Squad Demo — Task Board

A full-stack **Task Board** application demonstrating [Squad](https://github.com/bradygaster/squad) managing a diverse AI development team across two different tech stacks.

| Component | Stack | Location |
|-----------|-------|----------|
| Frontend  | [Astro](https://astro.build) · TypeScript · CSS | `frontend/` |
| Backend   | [FastAPI](https://fastapi.tiangolo.com) · Python · Pydantic | `backend/` |

## The Squad Team

This repo ships with a pre-configured Squad team. Each member specialises in a different part of the codebase:

| Name | Role | Domain |
|------|------|--------|
| **Keaton** | Frontend Engineer | Astro pages, components, layouts, CSS |
| **McManus** | Backend Engineer | FastAPI endpoints, Pydantic models, Python |
| **Fenster** | QA & Test Engineer | pytest, integration tests, edge cases |
| **Hockney** | DevOps & Infra | Docker, CI/CD, GitHub Actions |
| **Verbal** | Tech Lead | Architecture, code review, decisions |
| **Scribe** | Memory Manager | Session logging (automatic) |

> The frontend/backend split creates natural role diversity — Keaton works in TypeScript/Astro while McManus works in Python/FastAPI. Different languages, different frameworks, one team.

## Quick Start

### Prerequisites

- **Node.js** 18+ and **npm**
- **Python** 3.11+ and **pip**
- **Squad CLI**: `npm install -g @bradygaster/squad-cli`

### 1. Start the backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API runs at **http://localhost:8000**. Open http://localhost:8000/docs for the interactive Swagger UI.

### 2. Start the frontend

```bash
cd frontend
npm install
npm run dev
```

The app runs at **http://localhost:4321**.

### 3. Use Squad

```bash
# In the project root
squad
```

Then talk to the team:

```
squad > Team, let's add a dark/light theme toggle
squad > @McManus, add a /api/tasks/stats endpoint
squad > @Fenster, write tests for the task CRUD endpoints
squad > @Hockney, set up a Dockerfile for the backend
```

## Project Structure

```
squad-demo/
├── frontend/                 # Astro application
│   ├── src/
│   │   ├── pages/
│   │   │   └── index.astro   # Main task board page
│   │   ├── layouts/
│   │   │   └── Layout.astro  # Base HTML layout
│   │   └── components/
│   │       └── TaskCard.astro # Task card component
│   ├── package.json
│   └── astro.config.mjs
├── backend/                  # FastAPI application
│   ├── app/
│   │   ├── main.py           # FastAPI app & endpoints
│   │   ├── models.py         # Pydantic models
│   │   └── store.py          # In-memory data store
│   └── requirements.txt
├── .squad/                   # Squad team state (committed)
│   ├── team.md               # Roster
│   ├── routing.md            # Who handles what
│   ├── decisions.md          # Architectural decisions
│   └── agents/               # Individual agent charters & history
└── README.md
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/tasks` | List all tasks |
| `POST` | `/api/tasks` | Create a task |
| `GET` | `/api/tasks/{id}` | Get a single task |
| `PATCH` | `/api/tasks/{id}` | Update a task |
| `DELETE` | `/api/tasks/{id}` | Delete a task |
| `GET` | `/api/health` | Health check |

## License

MIT
