from typing import Optional
from sqlmodel import SQLModel,Field
from pydantic import BaseModel




class User(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    disabled:bool = False    

class Userdb(User,table=True):
    password:str