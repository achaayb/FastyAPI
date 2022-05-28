#crud model Boilerplate

from pydantic import BaseModel, Field
from typing import List, Optional

"""WARNING
    models are used for both input and output validation
    models define what the user can send to your endpoint
    models also define what the end user get to see
    TL;DR no response model == data leaks.
"""

"""NAMING STANDART
    1) RES or REQ followed by _
    2) PROTOCOL followed by _
    3) route_in_snake_case
    4) PATH parameters in CAPS 
        not followed by _ if at end of path
    EX: GET: /users/{id}/details
        REQ_GET_users_ID_details
"""

"""BASE MODELS
    define repetitive models
"""
class Crud(BaseModel):
    id: str = Field(alias='_id') #workaround pydantic _var
    key1: Optional[str]
    key2: Optional[str]
    key3: Optional[str]
class ID(BaseModel):
        id: str = Field(alias='_id')

"""RESPONSE MODELS
    define response models
"""
class RES_GET_(BaseModel):
    data: List[Crud]
    code: str
    message: str
class RES_POST_(BaseModel):
    data: str
    code: str
    message: str
class RES_GET_ID(BaseModel):
    data: Crud
    code: str
    message: str
class RES_PATCH_ID(BaseModel):
    data: Crud
    code: str
    message: str
class RES_DELETE_ID(BaseModel):
    data: ID
    code: str
    message: str

"""REQUEST MODELS
    define request models
"""
class REQ_POST_(BaseModel):
    key1: str
    key2: str
    key3: str
class REQ_PATCH_ID(BaseModel):
    key1: Optional[str]
    key2: Optional[str]
    key3: Optional[str]