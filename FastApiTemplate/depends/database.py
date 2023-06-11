
from sqlmodel import Field, Session, SQLModel, create_engine

from core import config

engine = create_engine(config.DB_LINK)

# Dependency
def get_db_Session():
    with Session(engine) as session:
        yield session


def create_all_table():
       
    SQLModel.metadata.create_all(engine)