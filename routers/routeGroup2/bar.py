from fastapi import APIRouter

router = APIRouter(
    responses={404: {"description": "Not found"}}
)

@router.get("/", summary="API KEY not Required example")
async def root():
    return {"message": "/bar/root"}
