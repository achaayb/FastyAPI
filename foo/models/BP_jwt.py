from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List

class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    authjwt_access_token_expires = False
    authjwt_algorithm = "HS512"

class REQ_auth(BaseModel):
    username: str
    secret: str