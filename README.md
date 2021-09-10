# acm-bot
SU ACM Bot
-- 
This bot was created for the SeattleU ACM Discord Server. 
## How to add a feature?
This bot is built on discord.py using a [cog-based architecture](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html). To add a new feature to the bot, create a new file under the cogs folder and the bot should take care of the rest. 
## How to Develop locally?
1. Create a new discord bot through the [Discord Developer Portal](https://discord.com/developers/applications).
2. Generate a bot token 
3. Store the token as an Env Variable using `echo TOKEN={generated-bot-token}`
4. Run the bot (This bot requires [discord.py v2.0.0a](https://github.com/Rapptz/discord.py)) using `python3 main.py` 

