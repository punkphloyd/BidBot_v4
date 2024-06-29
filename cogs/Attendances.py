import nextcord
from api_keys import server_id, bot_secret_key
from nextcord.ext import commands
from nextcord import ui, Interaction
import requests
import logging

PHP_URL_GET_PLAYERS = 'https://www.meltdownxi.com/admin/get_players.php'
PHP_URL_GET_EVENTS = 'https://www.meltdownxi.com/admin/get_events.php'
PHP_URL_CHECK_ATTENDANCES = 'https://www.meltdownxi.com/admin/check_attendance.php'
PHP_URL_ADD_ATTENDANCES = 'https://www.meltdownxi.com/admin/add_attendance.php'


BOT_SECRET_KEY = bot_secret_key

# Setup logging
logging.basicConfig(level=logging.INFO)


class Attendances(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[server_id], name="add_attendance", description="Update attendance for a player")
    async def add_attendance(self, interaction: nextcord.Interaction, player_name: str, time_spent: float, event_id: int):
        logging.info("add_attendance command invoked.")

        # Check time_spent is valid
        if time_spent < 0 or time_spent > 4.5 or time_spent % 0.5 != 0:
            await interaction.response.send_message("Invalid time spent. It should be between 0.0 and 4.5 in 0.5 increments.", ephemeral=True)
            return
        time_spent = 2*time_spent   # Converts the time supplied (hours) into points (2 points per hour)
        # Verify player_name and event_id
        response = requests.post(PHP_URL_CHECK_ATTENDANCES, data={"player_name": player_name, "event_id": event_id, "secret_key": BOT_SECRET_KEY})
        if response.status_code != 200:
            await interaction.response.send_message("Error contacting the server.", ephemeral=True)
            return

        result = response.json()
        if not result['player_exists'] or not result['event_exists']:
            await interaction.response.send_message("Invalid player name or event ID.", ephemeral=True)
            return

        # Submit attendance update
        response = requests.post(PHP_URL_ADD_ATTENDANCES, data={"player_id": result['player_id'], "event_id": event_id, "points": time_spent, "secret_key": BOT_SECRET_KEY})
        if response.status_code == 200:
            await interaction.response.send_message("Attendance updated successfully.", ephemeral=True)
        else:
            await interaction.response.send_message("Failed to update attendance.", ephemeral=True)


def setup(bot):
    bot.add_cog(Attendances(bot))
