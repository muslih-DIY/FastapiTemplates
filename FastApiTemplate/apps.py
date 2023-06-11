from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from apis import docs,users
from views import index
from depends import Auths
from core import config
from models.user import Userdb
from depends.database import create_all_table  

app = FastAPI()

# # Set all CORS enabled origins
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
app.mount("/static", StaticFiles(directory=config.ROOT / "static"), name="static")

routes = (
    index.router,
    docs.router,
    Auths.router,
    users.router,
)
for route in routes:
    app.include_router(route)

@app.on_event('startup')
async def startup():
    create_all_table()

    