
from typing import Any, Dict, Optional
from sqlmodel import Session,SQLModel
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

class RecordExist(HTTPException):
    def __init__(self, status_code: int=409, detail: Any = None, headers: Dict[str, str] | None = None) -> None:
        
        super().__init__(status_code, detail, headers)
    

def create_model(db:Session,model:SQLModel):
    try:
        db.add(model)
        db.commit()
        db.refresh(model)
        return model
    except IntegrityError:
        raise RecordExist(detail="Record exist")

    

