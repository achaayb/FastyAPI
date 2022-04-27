from fastapi import APIRouter, Depends, HTTPException
from ..helpers.response import Response, Error
from ..helpers.auth import auth_verify
from ..crud import auth as auth_crud
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


@router.post("/", summary="JWT authentication")
async def auth(user: auth_models.REQ_auth, Authorize: AuthJWT = Depends(AuthJWT)):
    #database auth verify (hash password first using hash helper)
    #user.username password
    foo = await auth_verify(user.username, user.secret)
    if not foo: Error("Invalid auth credentials")
    #end database auth verify

    data = {
        "_id": str(foo['_id']),
        "username": foo['username'],
        "role": foo.get("role", 0)
    }
    access_token = Authorize.create_access_token(subject=dumps(data))



    return Response(access_token, "JWT token generated")

@router.get('/', dependencies = [Depends(auth_dependencies.JWT_protect)])
def get(Authorize: AuthJWT = Depends(AuthJWT)):
    current_user = Authorize.get_jwt_subject()
    return Response(
        {"user": current_user},
        "success"
    )