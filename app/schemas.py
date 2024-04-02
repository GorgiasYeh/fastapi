from typing import Optional
from pydantic import BaseModel

class BaseUser(BaseModel):
    userName : str
    email : str
    password : str

class CreateUser(BaseUser):
    pass

class LoginUser(BaseModel):
    userName : str
    password : str
    
    
class User(BaseUser):
    pass

    class Config:
        from_attributes = True
        
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
    
class InfoPydantic(BaseModel):
    # id: int
    deviceName: str
    power: Optional[int] = None
    trackingModeColor: Optional[str] = None
    connected: str
    connectStatus: str
    step: Optional[int] = None
    lockMode: str

    class Config:
        from_attributes = True