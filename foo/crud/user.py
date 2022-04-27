from ..config.database import user_collection
from ..helpers.user import user_helper, hash_helper

from bson import ObjectId
from datetime import datetime

# Retrieve a user using id
async def get(id: str) -> dict:
    foo = await user_collection.find_one({"_id": ObjectId(id)})
    return foo

# Retrieve all users
async def get_all() -> list:
    foo = [] #empty array better than None :)
    async for iterator in user_collection.find():
        foo.append(user_helper(iterator))
    return foo

# Add user
async def insert_one(data: dict) -> dict:
    data = dict(data)
    data['secret'] = hash_helper(data['secret'])
    data['registerDate'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    user = await user_collection.insert_one(dict(data))
    callBackUser = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(callBackUser)

# Update user
async def update(id: str, data: dict):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if student:
        user_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True

# Delete user
async def delete(id: str):
    user = await student_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True