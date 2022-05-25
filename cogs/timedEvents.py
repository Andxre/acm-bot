import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands.core import has_permissions
import re
import os

class TimedEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pingD.start()

    @tasks.loop(minutes = 720)
    async def pingD(self):
        userId = 755682652698443907
        channelId = 885016712381100063
        channel = self.bot.get_channel(channelId)
        msg = await channel.send(f'<@{userId}>')
        await msg.delete()

    @commands.command()
    async def stopPing(self, ctx):
        self.pingD.cancel()
        await ctx.channel.send("Disabled Pinging")
    
    @commands.command()
    async def startPing(self, ctx):
        self.pingD.start()
        await ctx.channel.send("Enabled Pinging")
    

def setup(bot):
    bot.add_cog(TimedEvents(bot))