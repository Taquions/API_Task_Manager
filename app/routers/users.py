from .. import schemas, models, utils
from ..database import get_db
from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users", #Define o prefixo da rota
    tags=["Users"] #Define a tag da rota(que aparece na documentação)
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password) #Criptografa a senha
    user.password = hashed_password #Substitui a senha pela senha criptografada

    user = models.User(**user.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/{id}", response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")
    return user