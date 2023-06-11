from typing import Optional
from passlib import pwd
from passlib.context import CryptContext




class Password:
    def __init__(self, context: Optional[CryptContext] = None) -> None:
        if context is None:
            self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        else:
            self.context = context

    def verify(
        self, plain_password: str, hashed_password: str
        ):
        return self.context.verify(plain_password, hashed_password)

    def hash(self, password: str) -> str:
        return self.context.hash(password)

    def generate(self) -> str:
        return pwd.genword()