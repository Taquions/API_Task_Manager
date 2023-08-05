from pydantic import BaseModel, EmailStr
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: str
    

class UserBase(BaseModel):
    name: str
    email: EmailStr
    

class CreateTask(TaskBase):
    pass

class CreateUser(UserBase):
    password: str
    pass

class task(TaskBase):
    id: int
    status: str

    class Config:
        from_attributes = True

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None
