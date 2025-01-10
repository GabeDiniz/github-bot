import discord
from discord.ext import commands
import asyncio

# Used for retrieving BOT_KEY from .env
from decouple import config

# Fetch Credentials from local .env variables 
# Constants
BOT_KEY = config('BOT_KEY')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print(f"{bot.user} has connected to Discord!")


bot.run(BOT_KEY)
