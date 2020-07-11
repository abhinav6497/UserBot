# thenku phoenix-chan for url
import os
import json
import aiohttp
import asyncio
import random
from urllib.parse import quote as urlencode
from telethon import events
from userbot.events import register
from userbot import CMD_HELP

_pats = []

@register(outgoing=True, pattern=r'\.(l?[gp]?)pat(?:(?: \n?|\n)([\s\S]+))?')
async def pat(e):
    global _pats
    switch = e.pattern_match.group(1)
    caption = e.pattern_match.group(2)
    url = 'https://headp.at/js/pats.json'
    if not _pats:
        async with aiohttp.ClientSession() as session:
            async with session.post(url) as raw_resp:
                resp = await raw_resp.text()
        _pats = json.loads(resp)
    pats = _pats
    if 'g' in switch:
        pats = [i for i in pats if os.path.splitext(i)[1] == '.gif']
    elif 'p' in switch:
        c = lambda j:os.path.splitext(j)[1] in ['.png', '.jpg', '.jpeg']
        pats = [i for i in pats if c(i)]
    pat = random.choice(pats)
    link = f'https://headp.at/pats/{urlencode(pat)}'
    if 'l' in switch:
        caption = f'{caption or ""}\n\n{link}'
    await asyncio.wait([
        e.respond(caption, file=link, reply_to=e.reply_to_msg_id),
        e.delete()
    ])

    
    CMD_HELP.update({
    'pat':
    '.pat\
\nUsage: sends random pat pics & gifs.'
})
