
from cgitb import text
from pydoc import classname
from unittest import result
from xml.dom.minidom import TypeInfo
from discord.ext import commands
import pandas as pd
from datetime import datetime, timedelta
from helper import getToken, getWorklog
import json

date = datetime.now()
year = date.year
month = date.month
day = date.day
FMT = '%H:%M'
hours = []

for i in getWorklog():
    with open(i, "r", encoding="utf-8") as jsonFile:
        js = json.load(jsonFile)
        for dayWork in js["kayıtlar"]:
            if dayWork.split(".")[2] and int(dayWork.split(".")[1]) == month:
                for task in js["kayıtlar"][dayWork]:
                    obj = js["kayıtlar"][dayWork][task]
                    tdelta = datetime.strptime(obj["bitiş saati"], FMT) - datetime.strptime(obj["başlangıç saati"], FMT)
                    hours.append(tdelta)

total = timedelta(hours=0, minutes=0)
for h in hours:
    total = total + h
result = (total.days * 4*6)+(total.seconds/60/60)
bot = commands.Bot(command_prefix="!", description="The description")

@bot.event
async def  on_ready():
    channel = bot.get_channel(962008063341117520)
    await channel.send(result)

@bot.command()
async def ping(ctx):
    await ctx.send("ping")
    

bot.run(getToken())