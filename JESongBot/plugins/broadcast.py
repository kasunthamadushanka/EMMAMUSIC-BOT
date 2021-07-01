# Daisyxmusic (Telegram bot project)
# Copyright (C) 2021  Inukaasith
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
from JESongBot import bot
from pyrogram import filters
from pyrogram.types import Dialog
from pyrogram.types import Chat
from pyrogram.types import Message
from pyrogram.errors import UserAlreadyParticipant

SUDO_USERS = 1414582599

@bot.on_message(filters.command("broadcast") & filters.user(SUDO_USERS))
async def broadcast(_, message: Message):
        sent=0
        failed=0   
        wtf = await message.reply("`Starting a broadcast...`")
        if not message.reply_to_message:
            await wtf.edit("`Please reply to a message to broadcast!`")
            return
        lmao = message.reply_to_message.text
        async for dialog in bot.iter_dialogs():
            try:
                await bot.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`Broadcasting...` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
                #await wtf.edit(f"`broadcasting...` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats")
                
            
        await message.reply_text(f"`Broadcast Finished` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats")
