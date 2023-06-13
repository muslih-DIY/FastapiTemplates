
from abc import ABC,abstractmethod


class MethodNotSupported(Exception):
    pass

class BaseStrategy(ABC):
    """
    This implimentation having  three parts

    storage mechanism

    validation mechanism

    clear mechanism

    """
    @abstractmethod
    def store(self,token,user,expiry_min):
        pass

    @abstractmethod
    def validate(self,token):
        userid = 1
        return userid

    @abstractmethod
    def clear(self,token):
        pass 
    
    @abstractmethod
    def get_tokens(self,user):
        pass