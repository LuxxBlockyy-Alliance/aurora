from asyncio import run
import discord
from discord.ext import tasks
import asyncio  # Janosch hat das await vergessen
import sys
import os

try:
    bot = discord.Bot(intents=discord.Intents.all())
except RuntimeError as e:
    print("[[bold yellow]![/bold yellow]] > Closing session")
    sys.exit(0)

bot.load_extension("cogs.gpt")
bot.load_extension("cogs.admin")


async def get_server_count():
    return int(len(bot.guilds))

bot.run(os.getenv("token"))
