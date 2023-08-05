from fastapi import FastAPI , Depends
from typing import List
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import users, tasks, auth


models.Base.metadata.create_all(bind=engine) #Cria as tabelas no banco de dados

app = FastAPI()
app.include_router(users.router) #Adiciona as rotas do arquivo users.py
app.include_router(tasks.router)
app.include_router(auth.router)


@app.get("/")
async def root(db: Session = Depends(get_db)):
    return {"message": "Welcome to my task manager!"}

