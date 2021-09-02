import discord
from discord.ext.commands import has_permissions
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '$')
token = os.getenv("TOKEN")
bot.remove_command('help')

channels = {883095312263155712}

@bot.event
async def on_ready():
    print('Logged in as {}!'.format(bot.user))
    print('Discord Py Version: {}'.format(discord.__version__))

@bot.event
async def on_message(message):
    if (message.author != bot.user and message.content[0] != "$"):
        if (message.channel.id in channels):
            name = message.author.nick if message.author.nick != None else message.author.name
            await message.create_thread(name = f"{name}'s thread")
    await bot.process_commands(message)

@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def unlisten(ctx, channel):
    channels.remove(int(channel))
    await ctx.channel.send(f"Stopped listening to channel {channel}!")

@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def listen(ctx):
    channels.add(int(ctx.channel.id))
    await ctx.channel.send("Listening...")

@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")

bot.run(token)
    
