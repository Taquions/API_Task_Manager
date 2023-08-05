from sqlalchemy.orm import Session
from . import schemas, models
from fastapi import Response, status


def create_task(db: Session, task: schemas.CreateTask, current_user: schemas.User):
    db_task = models.Task(**task.model_dump(), owner_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def read_tasks(db: Session, search: str):
    return db.query(models.Task).filter(models.Task.title.contains(search)).all()

def read_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    db.delete(db_task)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
