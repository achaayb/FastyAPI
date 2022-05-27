from fastapi import APIRouter
from .helpers.response import Response

router = APIRouter(
    responses={404: {"description": "Not found"}}
)

@router.get("/", summary="API test")
async def root():
    return Response("","FastyAPI live!")
