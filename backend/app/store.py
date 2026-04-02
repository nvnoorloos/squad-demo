from collections import Counter

from app.models import Task, TaskStats, TaskStatus

_counter = 0
_tasks: dict[int, Task] = {}


def reset():
    """Reset the in-memory store."""
    global _counter
    _counter = 0
    _tasks.clear()


def _next_id() -> int:
    global _counter
    _counter += 1
    return _counter


def seed():
    """Populate store with sample tasks."""
    if _tasks:
        return
    create(title="Design the landing page", description="Create wireframes and mockups for the main landing page", status=TaskStatus.done, assignee="Keaton")
    create(title="Build REST API endpoints", description="Implement CRUD endpoints for the task board", status=TaskStatus.done, assignee="McManus")
    create(title="Connect frontend to API", description="Wire up fetch calls from Astro pages to the FastAPI backend", status=TaskStatus.in_progress, assignee="Keaton")
    create(title="Add input validation", description="Validate all user inputs on both client and server side", status=TaskStatus.in_progress, assignee="McManus")
    create(title="Write integration tests", description="Cover the main user flows with end-to-end tests", status=TaskStatus.todo, assignee="Fenster")
    create(title="Set up CI pipeline", description="Configure GitHub Actions for lint, test, and deploy", status=TaskStatus.todo, assignee="Hockney")


def list_all() -> list[Task]:
    return list(_tasks.values())


def get_stats() -> TaskStats:
    status_counts = Counter(task.status.value for task in _tasks.values())
    assignee_counts = Counter(task.assignee for task in _tasks.values())
    return TaskStats(
        total=len(_tasks),
        by_status={status.value: status_counts.get(status.value, 0) for status in TaskStatus},
        by_assignee=dict(assignee_counts),
    )


def get(task_id: int) -> Task | None:
    return _tasks.get(task_id)


def create(*, title: str, description: str = "", status: TaskStatus = TaskStatus.todo, assignee: str = "") -> Task:
    task = Task(id=_next_id(), title=title, description=description, status=status, assignee=assignee)
    _tasks[task.id] = task
    return task


def update(task_id: int, **fields) -> Task | None:
    task = _tasks.get(task_id)
    if task is None:
        return None
    data = task.model_dump()
    for k, v in fields.items():
        if v is not None:
            data[k] = v
    updated = Task(**data)
    _tasks[task_id] = updated
    return updated


def delete(task_id: int) -> bool:
    return _tasks.pop(task_id, None) is not None
