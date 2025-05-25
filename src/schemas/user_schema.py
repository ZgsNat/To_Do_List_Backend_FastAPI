from pydantic import BaseModel
from enum import Enum

class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    
class UserOut(BaseModel):
    id: int
    username: str
    email: str
    role: Role

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str