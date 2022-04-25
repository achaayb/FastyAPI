from fastapi import FastAPI

from routers.public.foo import router as foo
from routers.public.bar import router as bar

tags_metadata = [
    {
        "name": "root",
        "description": "root endpoints",
    },
    {
        "name": "foo",
        "description": "first route endpoints",
    },
    {
        "name": "bar",
        "description": "second route endpoints"
    }
]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(foo)
app.include_router(bar)


@app.get("/", tags=["root"])
def root():
    return {"message": "root"}