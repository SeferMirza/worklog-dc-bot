from cgitb import text
from pydoc import classname
from unittest import result
from discord.ext import commands
from datetime import datetime, timedelta
from helper import getToken, getWorklog
import json
import subprocess

date = datetime.now()
year = date.year
month = date.month
day = date.day
FMT = '%H:%M'
client = []
dic1 = {}

for i in getWorklog():
    with open(i, "r", encoding="utf-8") as jsonFile:
        js = json.load(jsonFile)
        musteriCalisma = timedelta(hours=0, minutes=0)

        #for client
        if js["müşteri"] not in client:
            client.append(js["müşteri"])
            dic1[js["müşteri"]] = timedelta(hours=0, minutes=0)

        #get all work hours
        for dayWork in js["kayıtlar"]:
            if int(dayWork.split(".")[2]) == year and int(dayWork.split(".")[1]) == (month):
                for task in js["kayıtlar"][dayWork]:
                    obj = js["kayıtlar"][dayWork][task]
                    tdelta = datetime.strptime(obj["bitiş saati"], FMT) - datetime.strptime(obj["başlangıç saati"], FMT)
                    musteriCalisma += tdelta
        dic1[js["müşteri"]] += musteriCalisma
total = 0
logByMusteri = {}
result = '```json\n{\n  "oranlar": {\n'
for clWorkHour in dic1:
    logByMusteri[clWorkHour] = ((dic1[clWorkHour].days * 24) + (dic1[clWorkHour].seconds/3600)) * 8/6
    total += (dic1[clWorkHour].days * 24) + (dic1[clWorkHour].seconds/3600)
    result += '     "' + str(clWorkHour) + '":' + str(((dic1[clWorkHour].days * 24) + (dic1[clWorkHour].seconds/3600))*8/6) + ',\n '

result += '},\n "total": '+str(total*8/6)+'\n'
result += '}\n```'
print(result)

bot = commands.Bot(command_prefix="!", description="The description")
#
@bot.event
async def  on_ready():
    channel = bot.get_channel(962008063341117520)
    await channel.send(result)
    exit()

@bot.command()
async def ping(ctx):
    await ctx.send("ping")

bot.run(getToken())