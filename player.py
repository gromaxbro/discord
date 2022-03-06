
import datetime
import asyncio
import pytz
import threading
import time
import discord
from discord.ext import commands
from requests import get
import json

bot = commands.Bot(command_prefix='!')

aware_us_centrald = datetime.datetime.now(pytz.timezone('US/Central'))

async def timer():
    await bot.wait_until_ready()# replace with channel ID that you want to send to
    msg_sent = False
    tyt = aware_us_centrald.hour + 2
    print(tyt)
    while True:
        aware_us_central = datetime.datetime.now(pytz.timezone('US/Central'))
        # print(aware_us_central.second)
        if tyt == 24:
            tyt = 0
            print(tyt)
        if aware_us_central.hour == tyt:
            print("done")
                content = get("https://meme-api.herokuapp.com/gimme").text
                data = json.loads(content,)
                meme = discord.Embed(Color = discord.Color.random()).set_image(url=f"{data['url']}")
                chee = bot.get_channel(949697019004481616)
                await chee.send(embed=meme)
            tyt = aware_us_central.hour + 2
            print(tyt)
        else:
            msg_sent = False
        await asyncio.sleep(1)

bot.loop.create_task(timer())
bot.run('OTQ3OTMyNTQwODc3MDEzMDcy.Yh0c-Q.oLE4DY_d6hwt7LD__QwFzmNkMKY')
    
