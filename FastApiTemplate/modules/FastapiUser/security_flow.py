
from typing import Any
from fastapi.security import HTTPBearer
from fastapi import Request


class BearerAccessFlow(HTTPBearer):
    pass

class BearerRefreshFlow(HTTPBearer):
    pass

class CookieFlow:
    def __init__(self,name) -> None:
        self.name = name
    
    async def __call__(self, request: Request) -> str:
        return request.cookies.get(self.name)
    