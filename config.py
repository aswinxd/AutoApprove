import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters
from pymongo import MongoClient


load_dotenv()

BOT_ID =7629699857
api_id  = int(getenv("API_ID"))
api_hash = getenv("API_HASH")
bot_token = getenv("BOT_TOKEN")
MONGO_URI = getenv("MONGO_URI", None)
MONGO_DB_NAME = getenv("DATABASE_NAME")
SUDOERS =1137799257
LOG_GROUP_ID =-1002271781032
mongo_client = MongoClient(MONGO_URI) 
db = mongo_client[MONGO_DB_NAME]  
welcome_collection = db[MONGO_DB_NAME]  