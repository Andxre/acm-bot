import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions
import re
import os

class TimedEvents(commands.cog):
    def __init__(self, bot):
        self.bot = bot

'''
    @tasks.loop(minutes = 60)
    async def pingD(self):
        userId = ""
        await       
'''