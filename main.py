from fastapi import FastAPI

import docs_metadata

from routers.routeGroup1.foo import router as foo
from routers.routeGroup2.bar import router as bar


app = FastAPI(
    title="achaayb FastAPI boilerplate",
    description=docs_metadata.description,
    openapi_tags=docs_metadata.tags)

app.include_router(foo, prefix="/foo", tags=["foo"])
app.include_router(bar, prefix="/bar", tags=["bar"])

@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass

@app.get("/", tags=["root"], summary="main root endpoint, use to serve app.")
async def root():
    return {"message": "root"}