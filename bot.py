import discord
from discord.ext import commands
import datetime
from datetime import timedelta
import time
import ImageGrab.py
import configparser

Snag = ImageGrab.ImageGrab(True)

config_read = configparser.ConfigParser()

TOKEN = 'NTA0Njk2Nzc3ODQ1NTA2MDc5.DrJBOg.4laYtgbGlZvuGPf8h5LLKbJxu5A'

client_id = 504696777845506079

client = commands.Bot(command_prefix='!')  # client object
# prefix character for issuing commands ie '!' when telling a music bot to !play
# Follow this link to add the bot to a server:
# https://discordapp.com/oauth2/authorize?client_id=504696777845506079&scope=bot


@client.event
async def on_ready():  # runs code in function when the bot is ready
    config_read.read('Configurations.ini')  # open the ini file for reading
    config_read.sections()

    if ('Time keeping' in config_read):  # if there is a section called "Time keeper" in the ini file
        print("Hello, world!")  # debug print
        daybox = datetime.date(config_read['Time keeper']['day_last'])

    Day_counter = datetime.date.today()  # pass the current date into a fluid variable

    if Day_counter - daybox == timedelta(0):  # if a day has passed
        # call up the script for posting the daily meme
        daybox = datetime.date.today()  # daybox now holds today's date so it can check for tomorrow

        config_read['Time keeping']['day_last'] = daybox  # reassign the day_last key with today's date
        config_read['Time keeping']['year'] = daybox.year  # reassign with the current year
        config_read['Time keeping']['month'] = daybox.month  # reassign with the current month
        config_read['Time keeping']['days'] = daybox.day  # reassign with the current day
        with open('Configurations.ini', 'w') as configfile:  # open the ini file for writing
            config_read.write(configfile)  # save changes

        Snag.GetMeme()  # time to shitpost

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
