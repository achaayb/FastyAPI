from bson import ObjectId
from bson.errors import InvalidId

def safe_objectid(string: str) -> ObjectId:
    try:
        return ObjectId(string)
    except InvalidId:
        return None