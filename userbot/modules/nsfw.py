# Imported from Rin :D




import nekos
from asyncio import sleep
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^\.pgif(?: |$)(.*)")
async def pussyg(e):
    await e.edit("`Finding some pussy gifs...`")
    await sleep(2)
    target = 'pussy'
    await bot.send_file(e.chat_id, nekos.img(target))
   

@register(outgoing=True, pattern="^\.pjpg(?: |$)(.*)")
async def pussyp(e):
    await e.edit("`Finding some pussy pics...`")
    await sleep(2)
    target = 'pussy_jpg'
    await bot.send_file(e.chat_id, nekos.img(target))
    

CMD_HELP.update({
    'nsfw':
    "`.pgif`"
    "\nUsage: Get pussy gif.\n"
    "`.pjpg`"
    "\nUsage: Get pussy image."
})
