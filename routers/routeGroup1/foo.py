from fastapi import APIRouter, Depends, HTTPException

from .dependenciesL import api_key

router = APIRouter(
    dependencies=[Depends(api_key)],
    responses={404: {"description": "Not found"}}
)

@router.get("/", summary="API KEY Required example")
async def root():
    return {"message": "/foo/root"}
