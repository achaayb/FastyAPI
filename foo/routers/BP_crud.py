#crud route Boilerplate

"""TODO [x] Smart returns
    - Smart returns. return database values without database reading
    - EX: on a success edit, return new values directly from input if update succeeds
    - this reduces database stress
    - return nothing for now
    - Smart returns standarts
        [x] POST: return inserted data
        [x] DELETE: return deleted _id
        [x] PATCH: return _id and updated valued
"""

"""TODO [] Crud metadata
    - POST: Creation date
    - DELETE: Softdelete, DELETE date
    - PATCH: PATCH date
"""

"""TODO [] Testing
    - [x] manual
    - [] automated
"""

"""DOCS
    - pymongo return values : https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html
    - pymongo collection level operations : https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html
    - pydantic exporting models : https://pydantic-docs.helpmanual.io/usage/exporting_models/
"""

from fastapi import APIRouter, Depends, Request
from ..databases.mongo import crud_collection
from ..helpers.response import Response, Error
from ..helpers.misc import safe_objectid
from ..models import BP_crud as crud_models
from bson import ObjectId

router = APIRouter(
    responses={404: {"description": "Not found"}},
)

@router.get("/", summary="retrieve all records", response_model=crud_models.RES_GET_)
async def get_all():
    #find an alternative to a forloop.
    #how many requests does this spit out?
    #does this even await??
    foo = [] 
    async for iterator in crud_collection.find():
        #cast _id (ObjectId) cuz pydantic dumb.
        #implement casting in the model. or spit as is.
        iterator['_id'] = str(iterator['_id']) 
        foo.append(iterator)
    return Response(foo,"Users fetched") if foo else Error("Users fetch failed")

@router.get("/{id}", summary="retrieve record", response_model=crud_models.RES_GET_ID)
async def get_one(id: str):
    #safcasting insures a valid objectid or None
    foo = await crud_collection.find_one({"_id": safe_objectid(id)})
    if foo:
        foo['_id'] = str(foo['_id'])
        return Response(foo,"User fetched")
    Error("User fetch failed")


@router.post("/", summary="insert record", response_model=crud_models.RES_POST_)
async def add(request: crud_models.REQ_POST_):
    #cast request class to dict
    #asign values to dict //request['key'] = value
    foo = await crud_collection.insert_one(request.dict())
    bar = request.dict()
    bar['_id'] = str(foo.inserted_id)
    return Response(str(bar),"User inserted successfully") if foo.inserted_id else Error("User insertion failed")

@router.delete("/{id}", summary="hard delete record", response_model=crud_models.RES_DELETE_ID)
async def delete(id: str):
    #safcasting insures a valid objectid or None
    foo = await crud_collection.delete_one({"_id": safe_objectid(id)})
    return Response({"_id": id},"User deleted") if foo.deleted_count else Error("User delete failed")

@router.patch("/{id}", summary="patch record", response_model=crud_models.RES_PATCH_ID)
async def patch(id: str,data: crud_models.REQ_PATCH_ID):
    #exclude_unset ignores keys with non given values
    #if not set, $set will update values to None
    bar = data.dict(exclude_unset=True)
    foo = await crud_collection.update_one({ "_id" : safe_objectid(id)},
                                            {"$set": bar})
    bar['_id'] = id
    return Response(bar,"User patched") if foo.modified_count else Error("User patch failed")