from ..databases.mongo import users_collection
print(f"--- {users_collection} {type(users_collection)}")


async def auth_verify(username, secret):
    foo = await users_collection.find_one({"username": username})
    return False if not foo else foo if foo['secret'] == secret else False #yanderedev fix this later