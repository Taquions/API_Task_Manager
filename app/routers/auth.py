from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, utils, oauth2, schemas
from ..database import get_db

router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)

@router.post("/", response_model=schemas.Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first() #Faz a query no banco de dados e retorna o usuário com o email que foi passado
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")
    if not utils.verify(request.password, user.password): #Verifica se a senha que foi passada é igual a senha que está no banco de dados
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"} 