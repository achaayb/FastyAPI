from os import environ
import motor.motor_asyncio

MONGO_DETAILS = environ['MONGO_URI']

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client[environ['MONGO_DATABASE']]

debug_collection = database.get_collection("debug")
bocal_collection = database.get_collection("bocal")
crud_collection = database.get_collection("crud")
users_collection = database.get_collection("users")