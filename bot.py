import discord
from discord.ext import commands
import datetime
from datetime import timedelta
import time
import ImageGrab.py

TOKEN = " "

client = commands.Bot(command_prefix='!')  # client object
# prefix character for issuing commands ie '!' when telling a music bot to !play

Daybox = datetime.date(2018, 10, 15)


@client.event
async def on_ready(daybox=Daybox):  # runs code in function when the bot is ready
    Day_counter = datetime.date.today()  # pass the current date into a fluid variable

    if Day_counter - daybox == timedelta(0):  # if a day has passed
        # call up the script for posting the daily meme
        daybox = datetime.date.today()  # daybox now holds today's date so it can check for tomorrow
        ImageGrab.main2()

    print('I am ready, my dudes. ')  # debug notification: bot is ready


@client.event
async def on_message(message): # when someone messages a command
    author = message.author # returns who wrote the message as a string
    content = message.content # returns the content of the message

 #  print("{}: {}".format(author, content)) # prints the message to the console with the format "author: content"

#@client.event
#async def on_message_delete(message): # 
  #  author = message.author
  #  content = message.content

    #channel = message.channel
    #await client.send_message(channel, "{}; {}".format(author, content))
    #sends a message with details of a deleted message

#@client.event
#async def
    
    
client.run(TOKEN) # run the bot
