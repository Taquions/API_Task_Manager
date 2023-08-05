
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, nullable = False)
    title = Column(String, nullable= False)
    description = Column(String, nullable=False)
    status = Column(String, server_default='Pendente', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)

class User (Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, nullable=False, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)