# Infinity BOTs <https://t.me/Infinity_BOTs>
# @ImJanindu

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import bot
from JESongBot import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), I'm Song Bot 🎵

Do /help for know about me!

A bot by **@Infinity_BOTs**
"""

help_text = """
I can download HQ songs from YouTube Music

**Syntax** - `/song [song name]`

A bot by *"@Infinity_BOTs**
"""

@bot.on_message(filters.command("start") & ~filters.edited)
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Source", url="https://github.com/ImJanindu/JESongBot"
                    ),
                    InlineKeyboardButton(
                        text="Dev", url="https://t.me/JEBotZ"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@bot.on_message(filters.command("help") & ~filters.edited)
async def start(client, message):
    await message.reply(help_text)

bot.start()
LOGGER.info("JESongBot is online.")
idle()
