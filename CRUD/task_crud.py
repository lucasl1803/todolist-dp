from sqlalchemy.orm import Session
import models, schemas, database
from models import TaskStatus


def get_tasks(db: Session):
    return db.query(models.Task).all()


def get_tasks_by_status(db: Session, status: TaskStatus):
    return db.query(models.Task).filter(models.Task.status == status).all()


def get_tasks_by_category(db: Session, category_id: int):
    return db.query(models.Task).filter(models.Task.category_id == category_id).all()


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        status=task.status,
        category_id=task.category_id,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task_data: schemas.TaskCreate):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return None

    for key, value in task_data.dict().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return False

    db.delete(task)
    db.commit()
    return True
