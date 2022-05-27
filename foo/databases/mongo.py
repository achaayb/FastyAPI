from os import environ
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

"""DOCS
    MOTOR ASYNCIO LOOP : https://stackoverflow.com/questions/65542103/future-task-attached-to-a-different-loop
    MOTOR BUY FIX : https://github.com/tiangolo/fastapi/issues/2943 (اللهم لك الحمدُ كله وإليك يرجعُ الأمرُ كلهُ)
"""


MONGO_DETAILS = f"{environ['MONGO_URI']}:{environ['MONGO_PORT']}"

client = AsyncIOMotorClient(MONGO_DETAILS)
client.get_io_loop = asyncio.get_event_loop
database = client[environ['MONGO_DATABASE']]
debug_collection = database.get_collection("debug")
bocal_collection = database.get_collection("bocal")
crud_collection = database.get_collection("crud")
users_collection = database.get_collection("users")