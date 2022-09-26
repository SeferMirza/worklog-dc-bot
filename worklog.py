#f654ca4d0f8211ed08f50e0fa1f783dc5d8d555cca4024b19a1fd8ff20e63263 public key
#1023875181346816031 app Id
#MTAyMzg3NTE4MTM0NjgxNjAzMQ.GlNcY6.ttgv_pFF6mOlraxfMLZpdr5S8jrAcxwLTXOumE token
#https://discord.com/channels/950662581679431690/962008063341117520 kanal bağlantısı
from cgitb import text
from pydoc import classname
from unittest import result
from xml.dom.minidom import TypeInfo
from discord.ext import commands
import bs4
import requests
import pandas as pd
#urls = [
#    "https://www.codewars.com/users/SeferMirza",
#    "https://www.codewars.com/users/cihandeniz",
#    "https://www.codewars.com/users/alptuncs"
#]
bot = commands.Bot(command_prefix="!", description="The description")
#
#data = []
#for url in urls:
#    xdata = "```yaml\n"
#    page = requests.get(url)
#    soup = bs4.BeautifulSoup(page.content,'html.parser')
#    results = soup.find_all("div",class_="stat")
#    for res in results:
#        if "Name:" in res.text:
#            xdata += res.text.replace("Name:", "Name: ") + "\n"
#        if "Rank:" in res.text:
#            xdata += res.text.replace("Rank:", "Rank: ") + "\n"
#        if "Honor:" in res.text:
#            xdata += res.text.replace("Honor:", "Honor: ") + "\n"
#        if "Total Completed Kata:" in res.text:
#            xdata += res.text.replace("Total Completed Kata:", "Total Completed Kata: ") + "\n"
#        if "Total Languages Trained:" in res.text:
#            xdata += res.text.replace("Total Languages Trained:", "Total Languages Trained: ") + "\n"
#        if "Highest Trained:" in res.text:
#            xdata += res.text.replace("Highest Trained:", "Highest Trained: ")
#
#    xdata += "\n```"
#    data.append(xdata)
#
@bot.event
async def  on_ready():
    channel = bot.get_channel(962008063341117520)
    #for i in range(len(urls)):
    #    await channel.send(data[i])
    await channel.send("test")
    print("ready")

@bot.command()
async def ping(ctx):
    await ctx.send("ping")
    

bot.run("MTAyMzg3NTE4MTM0NjgxNjAzMQ.GlNcY6.ttgv_pFF6mOlraxfMLZpdr5S8jrAcxwLTXOumE")