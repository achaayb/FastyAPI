from fastapi import APIRouter, Depends
from ..helpers.response import Response, Error
from ..crud import user as user_crud
from ..models import user as user_models
from ..dependencies import auth as auth_dependencies

from bson import ObjectId

router = APIRouter(
    responses={404: {"description": "Not found"}},
    dependencies = [Depends(auth_dependencies.JWT_protect)]
)

@router.get("/", summary="GET users", response_model=user_models.RES_get_all)
async def get_all():
    foo = await user_crud.get_all()
    return Response(foo,"Users fetched") if foo else Error("Users fetch failed")

@router.get("/{user_id}", summary="GET specific user", response_model=user_models.RES_get_one)
async def get_one(user_id: str):
    foo = await user_crud.get(ObjectId(user_id))
    if foo:
        foo['_id'] = str(foo['_id'])
        return Response(foo,"User fetched")
    else:
        Error("User fetch failed")

@router.post("/add", summary="ADD user", response_model=user_models.RES_add)
async def add(request: user_models.REQ_add_private):
    foo = await user_crud.insert_one(request)
    return Response(foo,"User inserted successfully") if foo else Error("User insertion failed")
