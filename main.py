import discord
from discord.ext import commands
import asyncio

# Functions
from github_api import get_issues
from github_api import get_closed_issues

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


# CHANNEL_ID = "temporary-channel-id"
# TRACKED_REPO = "GabeDiniz/github_bot"   # repo path (i.e., username/repo)

# tracked_issues = set()

# # Track issues
# async def track_issues():
#   await bot.wait_until_ready()
#   channel = bot.get_channel(CHANNEL_ID)
#   if not channel:
#     print("Invalid channel ID")
#     return

#   while True:
#     issues = get_issues(TRACKED_REPO)
#     new_issues = [issue for issue in issues if issue["id"] not in tracked_issues]

#     for issue in new_issues:
#       tracked_issues.add(issue["id"])
#       await channel.send(f"New issue created: {issue['title']} - {issue['html_url']}")

#     await asyncio.sleep(60)  # Check every minute

# bot.loop.create_task(track_issues())


# # Track Closed issues
# async def track_closed_issues():
#   await bot.wait_until_ready()
#   channel = bot.get_channel(CHANNEL_ID)
#   if not channel:
#     print("Invalid channel ID")
#     return

#   closed_issues = set()

#   while True:
#     issues = get_closed_issues(TRACKED_REPO)
#     newly_closed = [issue for issue in issues if issue["id"] not in closed_issues]

#     for issue in newly_closed:
#       closed_issues.add(issue["id"])
#       await channel.send(f"Issue closed: {issue['title']} - {issue['html_url']}")

#     await asyncio.sleep(60)  # Check every minute

# bot.loop.create_task(track_closed_issues())


bot.run(BOT_KEY)
