"""command: .heroku"""


from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd
import importlib.util
import asyncio
import random
import importlib.util
from datetime import datetime
from random import randint
from asyncio import sleep
from os import execl
from asyncio import create_subprocess_shell as asyncSubprocess
from asyncio.subprocess import PIPE as asyncPIPE
import sys
import os
import io
import git
import heroku3
import json
from sample_config import Config

# ================= CONSTANT =================
HEROKU_API_KEY = Config.HEROKU_API_KEY
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
Heroku = heroku3.from_key(HEROKU_API_KEY)
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================

async def subprocess_run(cmd, heroku):
    subproc = await asyncSubprocess(cmd, stdout=asyncPIPE, stderr=asyncPIPE)
    stdout, stderr = await subproc.communicate()
    exitCode = subproc.returncode
    if exitCode != 0:
        await heroku.edit(
            '**An error was detected while running subprocess**\n'
            f'```exitCode: {exitCode}\n'
            f'stdout: {stdout.decode().strip()}\n'
            f'stderr: {stderr.decode().strip()}```')
        return exitCode
    return stdout.decode().strip(), stderr.decode().strip(), exitCode

  
@borg.on(admin_cmd(pattern="heroku ?(.*)"))
async def heroku_manager(heroku):
    await heroku.edit("`Processing...`")
    await asyncio.sleep(3)
    conf = heroku.pattern_match.group(1)
    result = await subprocess_run(f'heroku ps -a {HEROKU_APP_NAME}', heroku)
    if result[2] != 0:
        return
    hours_remaining = result[0]
    await heroku.edit('`' + hours_remaining + '`')
    return
