from strings.string import clone_command_instructions
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
import html
@Client.on_message(filters.command("start"))
async def privacy_command(client, message):
    bot_username = (await client.get_me()).username  
    group_invite_link = f"https://t.me/{bot_username}?startgroup=true"
    Help_button = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("powered by elite bots", url="https://t.me/NonoDas")],
            [InlineKeyboardButton("➕ Add Bot to Your Group", url=group_invite_link)]
        ]
    )
    await message.reply_text(
        clone_command_instructions,
        reply_markup=Help_button
    )

