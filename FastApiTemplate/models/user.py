from typing import Optional
from sqlmodel import SQLModel,Field
from pydantic import BaseModel


class UserCreate(SQLModel):
    name: str = Field(unique=True)
    disabled:bool = False
    password:str

class UserUpdate(SQLModel):
    disabled:bool = False
    password:str

class UserSelect(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    disabled:bool = False    

class User(UserSelect,table=True):
    password:str

