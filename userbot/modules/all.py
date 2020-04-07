# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""A Plugin to tagall in the chat for @UniBorg and cmd is `.all`"""

from telethon import events
from uniborg.util import admin_cmd

# @borg.on(events.NewMessage(pattern=r"\.all", outgoing=True))
#@borg.on(admin_cmd("all"))
@register(outgoing=True, pattern="^.all$")
async def all(e):
    if e.fwd_from:
        return
    await e.delete()
    mentions = "@all"
    chat = await e.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await bot.send_message(chat, mentions, reply_to=event.message.reply_to_msg_id)


