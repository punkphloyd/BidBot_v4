from Sheets import *
from utils import *
from api_keys import *
import random
import time
import nextcord
from nextcord.ext import commands, tasks
import os
from nextcord import Interaction


# Get the current time as an integer
current_time = int(time.time())

# Set the random seed using the current time
random.seed(current_time)

# This main.py is currently setup as a test enrivonment for the Sheets.py functionality
# Tests how to implement she required sheets reading/writing

# Definition requirements to allow bot to interact appropriately in discord
# If anything needs to be updated (e.g. admin-only commands) this would be adjusted accordingly
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

# Bot line - runs the bot
bot = commands.Bot(command_prefix="!", intents=intents)


# Bot start function - prints out to terminal to aid debugging if debug_mode is true
# Also opens logging file appropriately
@bot.event
async def on_ready():

    # Date format to add to log file name (YYYYMMDD)
    date_now = datetime.now()
    date = date_now.strftime("%Y%m%d")
    time_hhmmss = date_now.strftime("%H:%M:%S")

    if debug_mode:
        print(f"Bot connection commenced - test bot {ver}")
        print("------------------------------")
        # Check if logs directory exists, and create if it does not
    logs_dir_exists = os.path.exists(logs_dir)
    if not logs_dir_exists:
        os.makedirs(logs_dir)

    # Log file name = pre + date
    log_filename = log_filename_pre + date
    # Should produce a log file unique to each day - will need to factor in some sort of cleanup routine on the system (probably via cron)
    # So that only 1 week of log files are retained

    # Check if log file already exists, if so open as append; otherwise open to write
    if os.path.exists(log_filename):
        log_file = open(log_filename, 'a')
    else:
        log_file = open(log_filename, 'w')

    # Print opening line to log file
    print(f"Bot starting at {time_hhmmss}", file=log_file)
    # Testing bot capability to print out to server channel
    channel = bot.get_channel(bids_channel_id)
    print(channel)
    if debug_mode:
        await channel.send(f"Bot starting up in debug mode. {time_hhmmss} - {date} ; log: {log_filename}")
    else:
        await channel.send("Bot starting up! Please place your bids")


# Slash Command: Ping
@bot.slash_command(name='ping', description='Replies with Pong!')
async def ping(ctx):
    await ctx.send('Pong!')


# Bot fail/disconnect function - prints out to terminal to aid debugging if debug_mode is true
# Report failure to log file
@bot.event
async def on_disconnect():

    # Date format to add to log file name (YYYYMMDD)
    date_now = datetime.now()
    date = date_now.strftime("%Y%m%d")
    time_hhmmss = date_now.strftime("%H:%M:%S")

    if debug_mode:
        print(f"Bot connection failure - test bot {ver}")
        print("------------------------------")
    logs_dir_exists = os.path.exists(logs_dir)
    if not logs_dir_exists:
        os.makedirs(logs_dir)

    # Log file name = pre + date
    log_filename = log_filename_pre + date
    # Should produce a log file unique to each day - will need to factor in some sort of cleanup routine on the system (probably via cron)
    # So that only 1 week of log files are retained

    # Check if log file already exists, if so open as append; otherwise open to write
    if os.path.exists(log_filename):
        log_file = open(log_filename, 'a')
    else:
        log_file = open(log_filename, 'w')

    # Print opening line to log file
    print(f"Bot disconnect at {time_hhmmss}", file=log_file)

# Bot close function - prints out to terminal to aid debugging if debug_mode is true
# Report close to log file
@bot.event
async def on_close():
    # Date format to add to log file name (YYYYMMDD)
    date_now = datetime.now()
    date = date_now.strftime("%Y%m%d")
    time_hhmmss = date_now.strftime("%H:%M:%S")
    if debug_mode:
        print(f"Bot closed - test bot {ver}")
        print("------------------------------")
    logs_dir_exists = os.path.exists(logs_dir)
    if not logs_dir_exists:
        os.makedirs(logs_dir)

    # Log file name = pre + date
    log_filename = log_filename_pre + date
    # Should produce a log file unique to each day - will need to factor in some sort of cleanup routine on the system (probably via cron)
    # So that only 1 week of log files are retained

    # Check if log file already exists, if so open as append; otherwise open to write
    if os.path.exists(log_filename):
        log_file = open(log_filename, 'a')
    else:
        log_file = open(log_filename, 'w')

    # Print opening line to log file
    print(f"Bot closed at {time_hhmmss}", file=log_file)


# Simple test command - remove prior to pushing production version
@bot.slash_command(guild_ids=[server_id], name="test", description="Slash commands test")
async def test(interaction: Interaction):
    player = interaction.user.display_name  # Get player name from discord user displayname
    await interaction.response.send_message(f"Hello, this is a test output initiatied by {player}")


# Load relevant cogs to support bot
bot.load_extension("cogs.Bids")

# Run bot from main
if __name__ == '__main__':
    bot.run(BOT_TOKEN)