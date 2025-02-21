import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
import html
from approver import app
from strings.string import (
    start_command_instructions, cloneHelp_text
)

@app.on_callback_query()
async def handle_callback_query(client, callback_query):
    data = callback_query.data
    if data == "clone":
        buttons = [
            [InlineKeyboardButton("Step-by-Step Guide", callback_data="clone_steps")],
            [InlineKeyboardButton("🔙", callback_data="help_command")],
        ]
        await callback_query.message.edit_text(
            cloneHelp_text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif data == "clone_steps":
        await callback_query.message.edit_text(
"""To clone a bot. follow these steps:\n

Go to @BotFather on Telegram.\n
Use the `/newbot` command to create a new bot and get the bot token.\n

Forward it to @HikayaHelpBot from @botfather with tag.\n
Once cloned, you can manage your bot via this bot, and it will work just like the original.\n
If you need to delete a cloned bot, use `/deleteclone` <bot_token>
                             """,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔙", callback_data="clone")]]
            ),
            parse_mode=ParseMode.MARKDOWN,
        )

@app.on_message(filters.command("start"))
async def privacy_command(client, message):
    Help_button = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕ Add to your group ", url="https://t.me/?startgroup=true")],
            [InlineKeyboardButton("➕ Create your own bot", callback_data="clone")]
        ]
    )
    await message.reply_text(
        start_command_instructions,
        reply_markup=Help_button
    )
