import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
import html
from approver import app
from strings.string import (
    start_command_instructions, help_text, privacy_policy_text, 
    adminHelp_text, userHelp_text, ownerHelp_text, cloneHelp_text
)

@app.on_callback_query()
async def handle_callback_query(client, callback_query):
    data = callback_query.data

    if data == "help_command":
        buttons = [
            [InlineKeyboardButton("How to Clone", callback_data="clone")],
            [InlineKeyboardButton("Privacy Policy", callback_data="privacy_policy")],
            [InlineKeyboardButton("Admin Help", callback_data="admin_help")],
            [InlineKeyboardButton("User Help", callback_data="user_help")],
            [InlineKeyboardButton("Owner Help", callback_data="owner_help")],
        ]
        await callback_query.message.edit_text(
            help_text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif data == "clone":
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
    elif data == "privacy_policy":
        buttons = [
            [InlineKeyboardButton("What Information We Collect", callback_data="info_collect")],
            [InlineKeyboardButton("Why We Collect", callback_data="why_collect")],
            [InlineKeyboardButton("What We Do", callback_data="what_we_do")],
            [InlineKeyboardButton("What We Do Not Do", callback_data="what_we_do_not_do")],
            [InlineKeyboardButton("Right to Process", callback_data="right_to_process")],
            [InlineKeyboardButton("🔙", callback_data="help_command")],
        ]
        await callback_query.message.edit_text(
            privacy_policy_text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif data == "info_collect":
        text = """
We collect the following user data:\n
- First Name
- Last Name
- Username
- User ID
- Clone bot token which is protected by our security features."""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="privacy_policy")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "why_collect":
        text = """
We collect it for managing clone bots and avoiding spammers from groups and make chat clean
Also we use it for bot statistics"""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="privacy_policy")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "what_we_do_not_do":
        text = """
We do not sell your data to third party"""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="privacy_policy")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "right_to_process":
        text = """
You have all rights to process your data on this bot
If you want to delete your data contact @Drxew
Warning: 
While we delete your data federations you own and the admin rights on other federations will be lost
Contact us if you are sure about deleting your data. it cant be recoverd after."""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="privacy_policy")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )     

    elif data == "admin_help":
        buttons = [
            [InlineKeyboardButton("Administrators", callback_data="administrators")],
            [InlineKeyboardButton("Chat Rules", callback_data="chat_rules")],
            [InlineKeyboardButton("Flood", callback_data="flood")],
            [InlineKeyboardButton("Notes", callback_data="notes")],
            [InlineKeyboardButton("Anti service", callback_data="antiservice")],
            [InlineKeyboardButton("Chat filters", callback_data="chatfilters")],
            [InlineKeyboardButton("Locks", callback_data="chatlocks")],
            [InlineKeyboardButton("Word blocklist", callback_data="word_blocklist")],
            [InlineKeyboardButton("Welcome / greetings", callback_data="welcomes_greetings")],
            [InlineKeyboardButton("Markdown / Formatting", callback_data="markdown_formatting")],
            [InlineKeyboardButton("🔙", callback_data="help_command")],
        ]
        await callback_query.message.edit_text(
            adminHelp_text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif data == "chatlocks":
        text = """
Here is the help for Locks:

Commands: /lock | /unlock | /locks [No Parameters Required]

Parameters:
    messages | stickers | gifs | media | games | polls

    inline  | url | group_info | user_add | pin

You can only pass the "all" parameter with /lock, not with /unlock

Example:
    /lock all
    
 /lockforward ENABLE/DISABLE this will delete all the forward messages
 /lockfont ENABLE/DISABLE this will delete all the messages with fancy font or symbols """
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="admin_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "word_blocklist":
        text = """
Here is the help for Blacklist:

/blocklisted - Get All The Blacklisted Words In The Chat.
/blocklist [WORD|SENTENCE] - Blacklist A Word Or A Sentence.
/rmblocklist [WORD|SENTENCE] - Whitelist A Word Or A Sentence."""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="admin_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "markdown_formatting":
        text = """
Read the below text carefully to find out how formatting works!

Supported Fillings:

{name} - This will mention the user with their name.
{chat} - This will fill with the current chat name.

NOTE: Fillings only works in greetings module.


Supported formatting:
`
**Bold** : This will show as bold text.
~~strike~~: This will show as strike text.
__italic__: This will show as italic text.
--underline--: This will show as underline text.
`code words`: This will show as code text.
||spoiler||: This will show as Spoiler text.
[hyperlink](google.com): This will create a hyperlink (https://www.google.com/) text.
Note: You can use both markdown & html tags.`


Button formatting:

-> text ~ [button text, button link]


Example:

example button with markdown formatting ~ [button text, https://google.com]"""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="admin_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "welcomes_greetings":
        text = """
Here is the help for Greetings:

•/captcha [ENABLE|DISABLE] - Enable/Disable captcha.

•/setwelcome - Reply this to a message containing correct
format for a welcome message, check end of this message.

•/delwelcome - Delete the welcome message.
•/welcome - Get the welcome message.

SET_WELCOME ->

To set a photo or gif as welcome message. Add your welcome message as caption to the photo or gif. The caption muse be in the format given below.

For text welcome message just send the text. Then reply with the command 

The format should be something like below.


**Hi** {name} [{id}] Welcome to {chat}

~ #This separater (~) should be there between text and buttons, remove this comment also

button=[Duck, https://duckduckgo.com]
button2=[Github, https://github.com]


NOTES ->

Checkout markdownhelp to know more about formattings and other syntax."""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="admin_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "chatfilters":
        text = """
Here is the help for Filters:
•/filters To Get All The Filters In The Chat.
•/filter [FILTER_NAME] To Save A Filter(reply to a message).

Supported filter types are Text, Animation, Photo, Document, Video, video notes, Audio, Voice.

To use more words in a filter use.
•/filter Hey_there To filter "Hey there".

•/stop [FILTER_NAME] To Stop A Filter.
•/stopall To delete all the filters in a chat (permanently).

•You can use markdown or html to save text too.

•Checkout markdownhelp to know more about formattings and other syntax."""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="admin_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "antiservice":
        text = """
Here is the help for AntiService:

Plugin to delete service messages in a chat!

•/antiservice [enable|disable]"""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="admin_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "administrators":
        text = """
Here is the help for Adminstrator:
•/ban - Ban A User
•/dban - Delete the replied message banning its sender
•/tban - Ban A User For Specific Time
•/unban - Unban A User
•/warn - Warn A User
•/dwarn - Delete the replied message warning its sender
•/rmwarns - Remove All Warning of A User
•/warns - Show Warning Of A User
•/kick - Kick A User
•/dkick - Delete the replied message kicking its sender
•/purge - Purge Messages
•/purge [n] - Purge "n" number of messages from replied message
•/del - Delete Replied Message
•/pin - Pin A Message
•/mute - Mute A User
•/tmute - Mute A User For Specific Time
•/unmute - Unmute A User
•/report | @admins | @admin - Report A Message To Admins."""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="admin_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "chat_rules":
        text = """
Here is the help for Rules:

 • /rules: get the rules for this chat.

Admins only:
 • /setrules: Reply to a message to set the rules for the chat.
 • /clearrules: clear the rules for this chat."""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="admin_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "flood":
        text = """
Here is the help for Flood:

Anti-Flood system, the one who sends more than 10 messages in a row, gets muted for an hour (Except for admins).

• /flood [ENABLE|DISABLE] - Turn flood detection on or off."""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="admin_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "notes":
        text = """
Here is the help for Notes:
• /notes To Get All The Notes In The Chat.

• /save [NOTE_NAME] To Save A Note.

Supported note types are Text, Animation, Photo, Document, Video, video notes, Audio, Voice.

To change caption of any files use.
• /save [NOTE_NAME] [NEW_CAPTION].

#NOTE_NAME To Get A Note.

• /delete [NOTE_NAME] To Delete A Note.
• /deleteall To delete all the notes in a chat (permanently)."""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="admin_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "fed_admin":
        text = """
 Fed Admins:
 • /fban <user> <reason>: Fed bans a user
 • /sfban: Fban a user without sending notification to chats
 • /unfban <user> <reason>: Removes a user from a fed ban
 • /sunfban: Unfban a user without sending a notification
 • /fedadmins: Show Federation admin
 • /fedchats <Fed_ID>: Get all the chats that are connected in the Federation"""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="admin_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "owner_help":
        buttons = [
            [InlineKeyboardButton("Federation owner", callback_data="fed_owner")],
             [InlineKeyboardButton("🔙", callback_data="help_command")],
        ]
        await callback_query.message.edit_text(
            ownerHelp_text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif data == "fed_owner":
        text = """
fed Owner Only:
 • /newfed <fed_name>: Creates a Federation, One allowed per user
 • /renamefed <fed_id> <new_fed_name>: Renames the fed id to a new name
 • /delfed <fed_id>: Delete a Federation, and any information related to it. Will not cancel blocked users
 • /myfeds: To list the federations that you have created
 • /fedtransfer <new_owner> <fed_id>:To transfer fed ownership to another person
 • /fpromote <user>: Assigns the user as a federation admin. Enables all commands for the user under Fed Admins
 • /fdemote <user>: Drops the User from the admin Federation to a normal User""" 
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="owner_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )   
    elif data == "user_help":
        buttons = [
            [InlineKeyboardButton("General Commands", callback_data="general_commands")],
            [InlineKeyboardButton("Federation users", callback_data="fed_users")],
            [InlineKeyboardButton("How to Use", callback_data="how_to_use")],
            [InlineKeyboardButton("🔙", callback_data="help_command")],
        ]
        await callback_query.message.edit_text(
            userHelp_text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif data == "general_commands":
        text = """
General commands for users are 
• /info : to check your info and other users stats on this bot
• /chatinfo : it helps to check the info of a group (it is only available on groups which Hikaya or other clone bots are added)"""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="user_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "fed_users":
        text = """
User Commands:
• /fedinfo <Fed_ID>: Information about a federation.
• /fedadmins <Fed_ID>: List the admins in a federation.
• /joinfed <Fed_ID>: Join the current chat to a federation. A chat can only join one federation. Chat owners only.
• /leavefed: Leave the current federation. Only chat owners can do this.
• /fedstat: List all the federations that you have been banned in.
• /fedstat <user_ID>: List all the federations that a user has been banned in.
• /fedstat <Fed_ID>: Gives information about your ban in a federation.
• /fedstat <user_ID> <FedID>: Gives information about a user's ban in a federation.
• /chatfed: Information about the federation the current chat is in."""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="user_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "how_to_use":
        text = """
Fist you can clone the bot as yours and add it on group and read help to how to use commands
Features and still on update the bot will be better than now in future"""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙", callback_data="user_help")]]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )

@app.on_message(filters.command("start"))
async def privacy_command(client, message):
    Help_button = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Help and commands", callback_data="help_command")],
            [InlineKeyboardButton("➕ Create your own bot", callback_data="clone")]
        ]
    )
    await message.reply_text(
        start_command_instructions,
        reply_markup=Help_button
    )
