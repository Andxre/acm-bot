from discord.ext import commands

class ProfanityListener(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.enabled = True
        self.bannedWords = self.populateList()
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if (self.enabled and 
            self.containsProfanity(message.content) and 
            message.webhook_id == None):
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
        return {"profanity1", "profanity2"}
    
    def containsProfanity(self, message):
        for word in self.bannedWords:
            if word in message:
                return True
        return False

    def formatProfanity(self, message):
        editedMsg = message
        split = editedMsg.split(" ")
        # Ew Nested For Loop
        for splitWord in split:
            for word in self.bannedWords:
                if (word in splitWord): 
                    editedMsg = editedMsg.replace(splitWord, "*profanity*")
        return editedMsg

def setup(bot):
    bot.add_cog(ProfanityListener(bot))
