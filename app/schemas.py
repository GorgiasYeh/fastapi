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