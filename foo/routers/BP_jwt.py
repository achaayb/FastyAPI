from fastapi import APIRouter, Depends, HTTPException
from ..helpers.response import Response, Error
from ..helpers.BP_jwt import auth_verify
from ..models import BP_jwt as jwt_models
from ..dependencies import BP_jwt as jwt_dependencies

from fastapi_jwt_auth import AuthJWT

from bson import ObjectId
from pydantic import BaseModel

from json import dumps

router = APIRouter(
    responses={404: {"description": "Not found"}}
)

"""DOCS
    - ws security : https://stackoverflow.com/questions/4361173/http-headers-in-websockets-client-api
    - ws security : https://www.freecodecamp.org/news/how-to-secure-your-websocket-connections-d0be0996c556/
    - ws security!: https://indominusbyte.github.io/fastapi-jwt-auth/advanced-usage/websocket/
"""

@AuthJWT.load_config
def get_config():
    return jwt_models.Settings()

@router.post("/", summary="JWT authentication")
async def auth(users: jwt_models.REQ_auth, Authorize: AuthJWT = Depends(AuthJWT)):
    foo = await auth_verify(users.username, users.secret)
    print (foo)
    print(type(foo))
    if not foo: Error("Invalid auth credentials")
    data = {
        "_id": str(foo['_id']),
        "username": foo['username']
    }
    access_token = Authorize.create_access_token(subject=dumps(data))
    return Response(access_token, "JWT token generated")

@router.get('/', dependencies = [Depends(jwt_dependencies.JWT_protect)])
def get(Authorize: AuthJWT = Depends(AuthJWT)):
    data = Authorize.get_jwt_subject()
    return Response(
        {"data": data},
        "success"
    )