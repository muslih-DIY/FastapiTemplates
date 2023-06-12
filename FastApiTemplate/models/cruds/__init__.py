
from typing import Any, Dict,List
from sqlmodel import Session,SQLModel,select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException,APIRouter,Depends
from depends.database import get_db_Session

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

    


def get_crud_router(
        model:SQLModel,
        operation:str="CRUD",
        pk:str='id',
        pk_type:str ='int',
        route_prefix='/api',
        new_model:SQLModel=None,
        select_model:SQLModel=None,
        update_model:SQLModel=None
        ):
    """
    operation = CRUD
    operation = CRU

    operation = CRD

    operation = CR

    """
    modelname = model.__name__.lower()
    new_model = new_model or model
    select_model = select_model or model
    update_model = update_model or model
    router = APIRouter(
        prefix=route_prefix,
        tags=[model.__name__]
    )

    if 'R' in operation:

        @router.get(f'/{modelname}s/',response_model=List[select_model])
        async def getall(
            session:Session=Depends(get_db_Session),
            # user=Depends(AuthManager.get_user_from_cookie)
            ):

            stmnt = select(model)
            result = session.exec(stmnt).all()
            return result
    
    if 'C' in operation:

        @router.post(f'/{modelname}/',response_model=new_model)
        async def create(
            model_instant:new_model,
            session:Session=Depends(get_db_Session),
            # user=Depends(AuthManager.user)
            ):
            # user_dict = userdb.dict()
            
            model_dict = create_model(session,model(**model_instant.dict(exclude_none=True)))
            return model_dict
    
    if 'R' in operation:

        @router.get(f'/{modelname}/{"{pk}"}',response_model=select_model)
        async def get(
            keys:pk_type,
            session:Session=Depends(get_db_Session),
            # user=Depends(AuthManager.user)
            ):

            return session.get(model,keys) 
    if 'D' in operation:

        @router.delete(f'/{modelname}/{"{pk}"}')
        async def delete(
            keys:pk_type,
            session:Session=Depends(get_db_Session),
            # user=Depends(AuthManager.user)
            ):
            model_instance = session.get(model,keys) 
            session.delete(model_instance)
            session.commit()
            return 
    if 'U' in operation:
        @router.put(f'/{modelname}/{"{pk}"}',response_model=select_model)
        async def update(
            pk:pk_type,
            model_instant:update_model,
            session:Session=Depends(get_db_Session),
            # user=Depends(AuthManager.user)
            ):
            model_dict = model_instant.dict(exclude_none=True)

            current_model = session.get(model,pk)
            for k,v in model_dict.items():
                setattr(current_model,k,v)
            session.add(current_model) 
            session.commit()
            session.refresh(current_model)
            return current_model
               
    return router
