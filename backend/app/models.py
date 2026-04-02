from pydantic import BaseModel
from enum import Enum


class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in-progress"
    done = "done"


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    status: TaskStatus = TaskStatus.todo
    assignee: str = ""


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None
    assignee: str | None = None


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus
    assignee: str
