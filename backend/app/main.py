from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models import Task, TaskCreate, TaskStats, TaskUpdate
from app import store

app = FastAPI(title="Squad Demo – Task Board API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4321", "http://127.0.0.1:4321"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    store.seed()


@app.get("/api/tasks", response_model=list[Task])
def list_tasks():
    return store.list_all()


@app.get("/api/tasks/stats", response_model=TaskStats)
def get_task_stats():
    """Return aggregate task board statistics."""
    return store.get_stats()


@app.get("/api/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = store.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/api/tasks", response_model=Task, status_code=201)
def create_task(body: TaskCreate):
    return store.create(
        title=body.title,
        description=body.description,
        status=body.status,
        assignee=body.assignee,
    )


@app.patch("/api/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, body: TaskUpdate):
    task = store.update(
        task_id,
        title=body.title,
        description=body.description,
        status=body.status,
        assignee=body.assignee,
    )
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/api/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if not store.delete(task_id):
        raise HTTPException(status_code=404, detail="Task not found")


@app.get("/api/health")
def health():
    return {"status": "ok"}
