import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.FastAPI

debug_collection = database.get_collection("debug")
user_collection = database.get_collection("users")