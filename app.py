#app file

"""TODO [] Webgui
    - [] Router register
    - [] App/db health
    - [] Statistics
"""

"""DOCS
    - DEPLOYMENT : https://www.uvicorn.org/deployment/
    - LIFESPAN : https://github.com/tiangolo/fastapi/issues/2943
    - CTX MANAGER : https://www.youtube.com/watch?v=-aKFBoZpiqA
"""
import uvicorn.workers
from os import environ
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from foo.config import metadata
from foo.main import router as rootRouter
from foo.routers.BP_crud import router as crudRouter
from foo.routers.BP_ws import router as wsRouter
from foo.routers.BP_jwt import router as jwtRouter
from foo.helpers.response import ErrorException

"""mongodb crud BP"""

app = FastAPI(
    title="FastyAPI",
    description=metadata.description,
    openapi_tags=metadata.tags,
    redoc_url=None,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
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

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(rootRouter, tags=["root"])
app.include_router(crudRouter, prefix="/crud", tags=["crud"])
app.include_router(wsRouter, prefix="/chat", tags=["websocket"])
app.include_router(jwtRouter, prefix="/jwt", tags=["jwt"])


@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    pass