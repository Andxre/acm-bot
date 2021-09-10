import discord
from discord.ext.commands import has_permissions
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '$')
token = os.getenv("TOKEN")
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as {}!'.format(bot.user))
    print('Discord Py Version: {}'.format(discord.__version__))
    loadCogs()

@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")

def loadCogs():
    for f in os.listdir("cogs"):
        if f.endswith('.py'):
            cogName = f.split('.')[0]
            bot.load_extension(f"cogs.{cogName}")
            print(f"Cog: {cogName} has been loaded.")
        
bot.run(token)