# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting information about the social media. """

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version

from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.follow$")
async def follow(follow):
    """ For .follow command, check if the bot is running.  """
    await follow.edit(
                     "`FOLLOW ME ON` \n"
                     f"INSTAGRAM: https://www.instagram.com/abhinav_shinde \n"
                     f"FACEBOOK: https://www.facebook.com/abhinav.shinde.353803 \n"
                     )    
