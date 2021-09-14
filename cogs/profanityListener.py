from discord import ChannelType
from discord.ext import commands

class ProfanityListener(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.enabled = True
        self.bannedWords = self.populateList()

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if (self.containsProfanity(after.content)):
            await after.delete()
            await after.channel.send(f"<@{after.author.id}>, please stop the profanity!")
    
    @commands.Cog.listener()
    async def on_thread_join(self, thread):
        await thread.join()

    @commands.Cog.listener()
    async def on_message(self, message):

        if (self.enabled):

            if (message.channel.type == ChannelType.public_thread):
                if (self.containsProfanity(message.content)):
                    await message.delete()
                    await message.channel.send((f"<@{message.author.id}>, please stop the profanity!"))


            elif (self.containsProfanity(message.content) and message.webhook_id == None):
                channel = self.bot.get_channel(message.channel.id)
                webhook = await message.channel.create_webhook(name = 'deleteThis')
                await message.delete()
            
                if (message.channel == channel):
                    await webhook.send(
                        content = self.formatProfanity(message.content),
                        username = message.author.display_name,
                        avatar_url = message.author.avatar.url
                    )

                    await webhook.delete()
        
    @commands.command()
    async def toggleProfanity(self, ctx):
        self.enabled = not self.enabled
        message = "Listening for Profanity" if self.enabled else "Not Listening for Profanity"
        await ctx.channel.send(message)
    
    def populateList(self):
        # TODO: Could pull a word list from a JSON file
        return {"fuck", "shit", "bitch", "cocksucker", "piss", "tits", 
                "motherfucker", "pussy"}
    
    def containsProfanity(self, message):
        for word in self.bannedWords:
            if word in message.lower():
                return True
        return False

    def formatProfanity(self, message):
        editedMsg = message.lower()
        split = editedMsg.split(" ")
        for splitWord in split:
            for word in self.bannedWords:
                if (word in splitWord): 
                    editedMsg = editedMsg.replace(splitWord, "*profanity*")
        return editedMsg

def setup(bot):
    bot.add_cog(ProfanityListener(bot))
