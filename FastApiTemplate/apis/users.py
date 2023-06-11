from typing import  List
from fastapi import APIRouter,Request,Depends
from fastapi.responses import JSONResponse
from depends.Auths import AuthManager
from depends.database import get_db_Session
from sqlmodel import select,Session
from models.user import Userdb,User
from models.cruds import create_model

router = APIRouter()


@router.get('/users/',response_model=List[User])
async def users(
    request:Request,
    session:Session=Depends(get_db_Session),
    # user=Depends(AuthManager.get_user_from_cookie)
    ):

    stmnt = select(Userdb)
    result = session.exec(stmnt).all()
    return result

@router.post('/user/',response_model=User)
async def create_user(
    userdb:Userdb,
    session:Session=Depends(get_db_Session),
    # user=Depends(AuthManager.user)
    ):
    # user_dict = userdb.dict()
    user_dict = create_model(session,userdb)
    return user_dict


