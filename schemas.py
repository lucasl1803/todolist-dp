from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import Optional   


class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    due_date: date | None = None
    status: TaskStatus = TaskStatus.TODO
    category_id: int


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    category: Optional[Category] = None  
    class Config:
        orm_mode = True
