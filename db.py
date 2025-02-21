from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI, MONGO_DB_NAME

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]
user_bots_collection = db["user_bots"]

async def save_bot_token(user_id: int, bot_token: str):
    await user_bots_collection.update_one(
        {"user_id": user_id},
        {"$set": {"bot_token": bot_token, "connected": True}},
        upsert=True,
    )

async def get_bot_tokens():
    bots = await user_bots_collection.find({"connected": True}).to_list(None)
    return [bot["bot_token"] for bot in bots]

async def disconnect_bot_token(user_id: int):
    await user_bots_collection.update_one(
        {"user_id": user_id},
        {"$set": {"connected": False}}
    )
