import re
import asyncio
import importlib
import logging
from pathlib import Path
from pyrogram import Client, idle, filters
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid
from pymongo import MongoClient
from approver import LOGGER, app
from strings import string 
from approver.plugins import ALL_MODULES
from config import api_id, api_hash, MONGO_URI, MONGO_DB_NAME

mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client["cloned"]
mongo_collection = mongo_db[MONGO_DB_NAME]

async def init():
    await app.start()

    # Load main modules
    plugins_path = Path("approver/plugins")
    for module_path in plugins_path.glob("*.py"):
        module_name = module_path.stem
        importlib.import_module(f"approver.plugins.{module_name}")
    LOGGER("Hikaya modules").info("Successfully imported all modules.")
    await restart_clones()

    await idle()
    await app.stop()

async def restart_clones():
    LOGGER("Clone acceptor").info("Restarting all cloned bots...")
    bots = list(mongo_db.bots.find())
    for bot in bots:
        bot_token = bot['token']
        try:
            ai = Client(
                f"{bot['username']}", api_id, api_hash,
                bot_token=bot_token,
                plugins={"root": "approver.cp"}
            )
            await ai.start()
            LOGGER("Clone Manager").info(f"Started cloned bot @{bot['username']}")
        except (AccessTokenExpired, AccessTokenInvalid) as e:
            LOGGER("Clone Manager").error(f"Failed token remoked @{bot['username']}")
        except Exception as e:
            LOGGER("Clone Manager").exception(f"Error @{bot['username']} :{e}")

@app.on_message(filters.command("clone") & filters.private)
async def clone(client, message):
    await message.reply_text(string.cloneHelp_text)

@app.on_message((filters.regex(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}')) & filters.private)
async def on_clone(client, message):  
    try:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        bot_token = re.findall(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}', message.text, re.IGNORECASE)
        bot_token = bot_token[0] if bot_token else None
        bot_id = re.findall(r'\d[0-9]{8,10}', message.text)
        bots = list(mongo_db.bots.find())
        bot_tokens = None  

        for bot in bots:
            bot_tokens = bot['token']

        forward_from_id = message.forward_from.id if message.forward_from else None
        if bot_tokens == bot_token and forward_from_id == 93372553:
            await message.reply_text("it is already cloned")
            return

        if not forward_from_id != 93372553:
            msg = await message.reply_text("wait a minute")
            try:
                ai = Client(
                    f"{bot_token}", api_id, api_hash,
                    bot_token=bot_token,
                    plugins={"root": "approver.cp"},
                )
                
                await ai.start()
                bot = await ai.get_me()
                details = {
                    'bot_id': bot.id,
                    'is_bot': True,
                    'user_id': user_id,
                    'name': bot.first_name,
                    'token': bot_token,
                    'username': bot.username
                }
                mongo_db.bots.insert_one(details)
                await msg.edit_text(f"cloned @{bot.username}.")
            except BaseException as e:
                logging.exception("Error while cloning bot.")
                await msg.edit_text(f"⚠<b>Bot Error:</b>\n\n<code>{e}</code>\n\n")
    except Exception as e:
        logging.exception("Error while handling message.")

@app.on_message(filters.command("deleteclone") & filters.private)
async def delete_cloned_bot(client, message):
    try:
        bot_token = re.findall(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}', message.text, re.IGNORECASE)
        bot_token = bot_token[0] if bot_token else None
        bot_id = re.findall(r'\d[0-9]{8,10}', message.text)

        mongo_collection = mongo_db.bots
        
        cloned_bot = mongo_collection.find_one({"token": bot_token})
        if cloned_bot:
            mongo_collection.delete_one({"token": bot_token})
            await message.reply_text("removed")
        else:
            await message.reply_text("token not in cloned list")
    except Exception as e:
        await message.reply_text("An error occurred while deleting the cloned bot.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
