# Squad Decisions

## Active Decisions

### DEC-001: Use Astro for frontend (2026-04-02)
- **By:** Verbal
- **Rationale:** Astro provides fast, content-focused SSR with minimal client JS. Perfect for a demo that needs to look good and be easy to understand.

### DEC-002: Use FastAPI for backend (2026-04-02)
- **By:** Verbal
- **Rationale:** FastAPI is lean, fast, and auto-generates OpenAPI docs. The Python + TypeScript split creates natural role diversity for the Squad team.

### DEC-003: In-memory storage for demo (2026-04-02)
- **By:** McManus
- **Rationale:** No database dependency keeps the demo simple. Seed data loads on startup. Can swap in SQLite/PostgreSQL later if needed.

### DEC-004: Kanban board as demo concept (2026-04-02)
- **By:** Verbal
- **Rationale:** A task board is visual, requires clear CRUD operations, and is meta — the Squad team manages tasks while building a task manager.

### DEC-005: Issue #2 assignment to McManus (2026-04-02)
- **By:** Verbal
- **Rationale:** Issue scope is purely backend API. McManus owns the Python/FastAPI domain. Requires TaskStats model, get_stats() helper, and GET /api/tasks/stats endpoint.

### DEC-006: Route ordering in FastAPI (2026-04-02)
- **By:** McManus
- **Rationale:** Static paths (/api/tasks/stats) must precede parameterized paths (/{task_id}) to prevent path parameters from consuming static route names.

### DEC-007: Keep dev dependencies in main requirements.txt (2026-04-02)
- **By:** Verbal
- **Rationale:** Acceptable for demo scope. Future growth may justify splitting into requirements-dev.txt.

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction
