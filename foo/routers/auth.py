from fastapi import APIRouter, Depends, HTTPException
from ..helpers.response import Response, Error
from ..helpers.auth import users_verify, bocal_verify
from ..models import auth as auth_models
from ..dependencies import auth as auth_dependencies

from fastapi_jwt_auth import AuthJWT

from bson import ObjectId
from pydantic import BaseModel

from json import dumps

router = APIRouter(
    responses={404: {"description": "Not found"}}
)


@AuthJWT.load_config
def get_config():
    return auth_models.Settings()


@router.post("/bocal", summary="JWT authentication")
async def auth(user: auth_models.REQ_auth, Authorize: AuthJWT = Depends(AuthJWT)):
    foo = await bocal_verify(user.username, user.secret)
    if not foo: Error("Invalid auth credentials")
    data = {
        "_id": str(foo['_id']),
        "username": foo['username'],
        "role": foo.get("role", 0)
    }
    access_token = Authorize.create_access_token(subject=dumps(data))
    return Response(access_token, "JWT token generated")

@router.post("/users", summary="JWT authentication")
async def auth(users: auth_models.REQ_auth, Authorize: AuthJWT = Depends(AuthJWT)):
    foo = await users_verify(users.username, users.secret)
    if not foo: Error("Invalid auth credentials")
    data = {
        "_id": str(foo['_id']),
        "username": foo['username'],
        "role": foo.get("role", 0)
    }
    access_token = Authorize.create_access_token(subject=dumps(data))
    return Response(access_token, "JWT token generated")

@router.get('/', dependencies = [Depends(auth_dependencies.JWT_protect)])
def get(Authorize: AuthJWT = Depends(AuthJWT)):
    data = Authorize.get_jwt_subject()
    return Response(
        {"data": data},
        "success"
    )