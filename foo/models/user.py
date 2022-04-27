from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional

class User(BaseModel):
    id: str
    fullName: str
    username: str
    registerDate: str
    role: int

class RES_get_all(BaseModel):
    data: List[User]
    code: str
    message: str
class RES_get_one(BaseModel):
    data: List[User]
    code: str
    message: str

class REQ_add_public(BaseModel):
    username: str #make sure doesnt exist.
    fullName: str
    role: int
class REQ_add_private(REQ_add_public):
    secret: str
class RES_add(BaseModel):
    data: REQ_add_public
    code: str
    message: str