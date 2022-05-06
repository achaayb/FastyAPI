from os import environ
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from foo.config import metadata
from foo.main import router as RootRouter
#from foo.routers.auth import router as AuthRouter
from foo.routers.BP_crud import router as CrudRouter
#from foo.routers.chat import router as ChatRouter
from foo.helpers.response import ErrorException

app = FastAPI(
    title="achaayb FastAPI boilerplate",
    description=metadata.description,
    openapi_tags=metadata.tags,
    redoc_url=None
    )

@app.exception_handler(ErrorException)
def error_exception_handler(request: Request, exc: ErrorException):
    return JSONResponse(
        status_code=200,
        content={
            "code": "error",
            "message": exc.message
        }
    )

#app.include_router(AuthRouter, prefix="/auth", tags=[""])
app.include_router(RootRouter, tags=["root"])
app.include_router(CrudRouter, prefix="/crud", tags=["user"])
#app.include_router(ChatRouter, prefix="/chat")

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    pass