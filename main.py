import discord
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import commands, tasks
import os
import logging
import uuid

bot = commands.Bot(command_prefix = '$')
token = "ODgzMDgzODY5MDA2NDkxNzE5.YTEx8Q.Riw0zg5PxxsItMPEKJNbEf16KDI" # Bot Token make ENV Variable 
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as {}!'.format(bot.user))
    print('Discord Py Version: {}'.format(discord.__version__))

@bot.event
async def on_message(message):
    if (message.author != bot.user):
        if (message.channel.id == 883091072543252500):
            await message.create_thread(name = f"{message.author.nick}'s thread")


bot.run(token)
    
