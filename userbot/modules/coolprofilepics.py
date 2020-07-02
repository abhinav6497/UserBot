#credits to the respective owner xD
#imported by @heyworld 
import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

import asyncio

from time import sleep

from userbot.events import register 

COLLECTION_STRING = [

  "Rashmika-Mandana-cute-wallpaper"

]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@register(outgoing=True, pattern="^.randompp(?: |$)(.*)")

async def main(event):

    await event.edit("`changing your Profile Pic...`\n\n`Check Your DP in 10 seconds.`")

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(3600) #Edit this to your required needs
