from fastapi import Depends, HTTPException
from ..helpers.response import Response, Error , ErrorException

from fastapi_jwt_auth import AuthJWT


def JWT_protect(Authorize: AuthJWT = Depends(AuthJWT)):
    try:
        Authorize.jwt_required()
    except:
        raise ErrorException("JWT required")
