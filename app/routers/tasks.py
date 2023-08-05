from .. import schemas, oauth2, models
from ..crud import create_task, read_tasks, read_task, delete_task
from ..database import get_db
from fastapi import  Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/tasks", #Define o prefixo da rota,
    tags=["Tasks"] #Define a tag da rota(que aparece na documentação)
)


# Rota para criar uma nova tarefa
@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.task)
def create_new_task(task: schemas.CreateTask, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return create_task(db, task)

# Rota para obter todas as tarefas cadastradas
@router.get("/", response_model=List[schemas.task])
def get_tasks(db: Session = Depends(get_db)):
    return read_tasks(db)

#Rota para ver uma tarefa desejada
@router.get("/{id}", response_model=schemas.task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    db_task = read_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task

# Rota para atualizar o status de uma tarefa
@router.patch("/{task_id}/", response_model=schemas.task)
def update_task_status(task_id: int, status: bool, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    if status == True:
        db_task.status = 'Concluido'
    else:
        db_task.status = 'Pendente'
    db.commit()
    db.refresh(db_task)
    return db_task

# Rota para excluir uma tarefa
@router.delete("/{task_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_by_id(task_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    db_task = read_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return delete_task(db, task_id)
