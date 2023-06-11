from datetime import datetime,timedelta
import random
from jose import JWTError, jwt
from enum import Enum

JWT_ALGORITHM = "HS256"

class SessionType(Enum):
    COOKIE  = 2
    REFRESH = 3
    ACCESS  = 4

def create_access_token(
        data:dict,
        secret,
        expires_min: int,
        algorithm: str = JWT_ALGORITHM
        ):
    
    data["type"]=SessionType.ACCESS.value
    return generate_token(data,expires_min)
    
def create_cookies_token(
        data:dict,
        secret,
        expires_min: int,
        algorithm: str = JWT_ALGORITHM
        ):
    
    data["type"]=SessionType.COOKIE.value
    return generate_token(data,expires_min)

def create_refresh_token(
        data:dict,
        secret,
        expires_min: int,
        algorithm: str = JWT_ALGORITHM
        ):
    
    data["type"]=SessionType.REFRESH.value
    return generate_token(data,expires_min)

def generate_token(
        data,
        secret,
        expires_min: int,
        algorithm: str = JWT_ALGORITHM
        ):
    payload = data.copy()
    if expires_min:
        expire = datetime.utcnow() + timedelta(minutes=expires_min)
        payload["exp"] = expire
    payload.update({"rand":random.randrange(10,50)})
    return jwt.encode(payload, str(secret), algorithm=algorithm)

def decode_token(token,secret,algorithms:list=[JWT_ALGORITHM]):
    return jwt.decode(
        token, 
        str(secret),
        algorithms=algorithms)

    