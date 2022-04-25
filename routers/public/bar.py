#route boilerplate for simple route

from fastapi import APIRouter

router = APIRouter(
    prefix="/bar",
    tags=["bar"],
    responses={404: {"description": "Not found"}}
)

@router.get("/", tags=["bar"])
async def read_users():
    return {"message": "/foo/route"}
