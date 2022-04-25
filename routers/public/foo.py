#route boilerplate for dependency and an HTTPException

from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import verify_secret

router = APIRouter(
    prefix="/foo",
    tags=["foo"],
    dependencies=[Depends(verify_secret)],
    responses={404: {"description": "Not found"}}
)

@router.get("/", tags=["bar"])
async def read_users():
    return {"message": "/foo/root"}
