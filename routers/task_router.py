from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
import CRUD.task_crud as task_crud
import schemas
from schemas import TaskStatus

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Task])
def list_tasks(
    status: TaskStatus | None = None,
    category_id: int | None = None,
    db: Session = Depends(get_db),
):
    if status:
        return task_crud.get_tasks_by_status(db, status)
    if category_id:
        return task_crud.get_tasks_by_category(db, category_id)
    return task_crud.get_tasks(db)


@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return task_crud.create_task(db, task)


@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, data: schemas.TaskCreate, db: Session = Depends(get_db)):
    updated = task_crud.update_task(db, task_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return updated


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = task_crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"message": "Tarefa removida com sucesso!"}
