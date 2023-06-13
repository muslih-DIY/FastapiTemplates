from typing import Optional
from .base import BaseStrategy,MethodNotSupported
from ..token import decode_token


class JWTStratagy(BaseStrategy):

    def __init__(
            self,
            secret:str,
            lifetime_minutes: Optional[int]=1,
            algorithm: str = "HS256",
            ) -> None:
    
        self.secret  = secret
        self.lifetime_minutes = lifetime_minutes
        self.algorithm = algorithm

    def store(self, token, user, expiry_min):
        raise MethodNotSupported

    def validate(self, token)-> dict:
        payload =  decode_token(
            token,
            str(self.secret),
            algorithms=[self.algorithm]
            )
        return payload.get("sub")

    def clear(self, token):
        raise MethodNotSupported
    
    def get_tokens(self, user):
        raise MethodNotSupported