from fastapi import APIRouter

router = APIRouter(
    responses={404: {"description": "Not found"}}
)

@router.get("/", summary="GET users")
async def root():
    return {"message" : "available"}