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
        await ctx.channel.send("DM sent.")

        os.remove("result.csv")
    
    
    @commands.command()
    @has_permissions(manage_roles=True, ban_members=True)
    async def spam(self, ctx, user, times):
        if (int(times) > 20):
            await ctx.channel.send("Stop it fool")
            return
        for i in range(int(times)):
            await ctx.channel.send(f'{user}')
            

def setup(bot):
    bot.add_cog(HelperCommands(bot))