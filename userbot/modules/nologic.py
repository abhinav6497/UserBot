from telethon import events

import asyncio

import os

import sys

import random


from userbot.events import register

@register(pattern="^.logic(?: |$)(.*)")

async def _(event):
	
	if event.fwd_from:
		
		return
		
		await event.edit("`Ruk ek Kamal ki Fact Soch Raha hu....`")
		
		await asyncio.sleep(3)
		
		x=(random.randrange(1,7))
		
		if x==1 :
		    await event.edit("`\"Do you know, Some Mosquitoes became Ghosts, When we Kill them.\"`")
			
		if x==2 :
		    await event.edit("`\"Do you know, Mosquitoes has Teleportation Power?\"`")
		    
		if x==3 :
		    await event.edit("`\"Do you know, When you see a Bearded Goat, that means you juat saw a Intellligent Goat than you.\"`")
		    
		if x==3 :
		    await event.edit("`\"Do you know, when you give some rupess to Bus Conductor, He will give you a piece of paper, Called Ticket\"`")
		    
		if x==4 :
		    await event.edit("`\"Do you know, Bus are called Bus, Because they are Bus\"`")
		    
		if x==5 :
		    await event.edit("`\"Do you know, There's a Huge Difference between Cartoon and Anime\"`")
		    
		if x==6 :
		    await event.edit("`\"Do you know, You cant see Ghosts but Ghosts can see you\"`")
		 
		if x==7 :
		    await event.edit("`\"Do You Know, You can't See in the Dark\"`")