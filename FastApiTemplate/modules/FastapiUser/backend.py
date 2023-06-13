
from typing import List
from .token import decode_token,create_access_token,create_cookies_token,create_refresh_token
from .strategy.base import BaseStrategy
from .strategy.jwt import JWTStratagy
from .security_flow import BearerAccessFlow,BearerRefreshFlow,CookieFlow




class AuthenticationBackend:


    def __init__(
            self,
            strategy:BaseStrategy,
            flow
            ) -> None:
    
        self.backend = flow

    
    def 

        

    
    
