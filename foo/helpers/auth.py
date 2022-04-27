from ..config.database import user_collection
from ..helpers.user import hash_helper

async def auth_verify(username: str, secret: str):
    foo = await user_collection.find_one({"username": username})
    if foo and foo.get("secret", None) == hash_helper(secret):
        return foo

