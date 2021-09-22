import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions
import re
import os

class HelperCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(manage_roles=True, ban_members=True)
    async def collectEmails(self, ctx):
        pattern = '^\w+@\w+.\w+$'
        emails = []
        async for msg in ctx.channel.history(limit=300):
            result = re.fullmatch(pattern, msg.content)
            if (result != None):
                emails.append(result.string)
        
        with open("result.csv", "w") as f:
            for idx, val in enumerate(emails):
                if (idx != len(emails) - 1):
                    f.write(f'{val},')
                else:
                    f.write(val)

        await ctx.author.send(file = discord.File("result.csv"))

        os.remove("result.csv")


def setup(bot):
    bot.add_cog(HelperCommands(bot))