from sqlalchemy.orm import Session
from . import schemas, models
from fastapi import Response, status


def create_task(db: Session, task: schemas.CreateTask):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def read_tasks(db: Session):
    return db.query(models.Task).all()

def read_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    db.delete(db_task)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
