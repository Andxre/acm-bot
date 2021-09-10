from discord.ext.commands import has_permissions
from discord.ext import commands


class ThreadListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channels = {883095312263155712}
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if (message.author != self.bot.user and message.content[0] != "$"):
            if (message.channel.id in self.channels):
                name = message.author.nick if message.author.nick != None else message.author.name
                await message.create_thread(name = f"{name}'s thread")

    @commands.command()
    @has_permissions(manage_roles=True, ban_members=True)
    async def unlisten(self, ctx):
        self.channels.remove(int(ctx.channel.id))
        await ctx.channel.send(f"Stopped listening to this channel...")

    @commands.command()
    @has_permissions(manage_roles=True, ban_members=True)
    async def listen(self, ctx):
        self.channels.add(int(ctx.channel.id))
        await ctx.channel.send("Listening...")

def setup(bot):
    bot.add_cog(ThreadListener(bot))