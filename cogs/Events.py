import nextcord
from api_keys import server_id, bot_secret_key
from nextcord.ext import commands
from nextcord import ui, Interaction
import requests
import logging

PHP_URL_ADD_EVENT = 'https://www.meltdownxi.com/admin/add_event.php'
PHP_URL_GET_EVENT_TYPES = 'https://www.meltdownxi.com/admin/get_event_types.php'
BOT_SECRET_KEY = bot_secret_key

# Setup logging
logging.basicConfig(level=logging.INFO)

class DatePickerView(ui.View):
    def __init__(self):
        super().__init__()
        self.month_select = nextcord.ui.Select(
            placeholder="Month",
            options=[nextcord.SelectOption(label=str(month)) for month in range(1, 13)],
            custom_id="month"
        )
        # Split the day options into two selects to avoid exceeding 25 options
        day_options_part1 = [nextcord.SelectOption(label=str(day)) for day in range(1, 16)]
        day_options_part2 = [nextcord.SelectOption(label=str(day)) for day in range(16, 32)]

        self.day_select_part1 = nextcord.ui.Select(
            placeholder="Day (1-15)",
            options=day_options_part1,
            custom_id="day_part1"
        )
        self.day_select_part2 = nextcord.ui.Select(
            placeholder="Day (16-31)",
            options=day_options_part2,
            custom_id="day_part2"
        )

        self.add_item(self.month_select)
        self.add_item(self.day_select_part1)
        self.add_item(self.day_select_part2)


class AddEventView(ui.View):
    def __init__(self, event_types, event_name):
        super().__init__()
        self.event_name = event_name
        self.date_picker = DatePickerView()
        for child in self.date_picker.children:
            self.add_item(child)

        self.event_type_select = nextcord.ui.Select(
            placeholder="Select Event Type",
            options=[nextcord.SelectOption(label=event_type['event_type']) for event_type in event_types],
            custom_id="event_type"
        )
        self.add_item(self.event_type_select)

    @nextcord.ui.button(label="Submit", style=nextcord.ButtonStyle.primary)
    async def submit_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        year = "2024"
        month = nextcord.utils.get(self.children, custom_id="month").values[0]

        # Check which day part is selected
        day_part1_select = nextcord.utils.get(self.children, custom_id="day_part1")
        day_part2_select = nextcord.utils.get(self.children, custom_id="day_part2")

        day = None
        if day_part1_select.values:
            day = day_part1_select.values[0]
        elif day_part2_select.values:
            day = day_part2_select.values[0]

        if not day:
            await interaction.response.send_message('Please select a day.', ephemeral=True)
            return

        event_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        event_type = nextcord.utils.get(self.children, custom_id="event_type").values[0]

        event_data = {
            'event_name': self.event_name,
            'event_date': event_date,
            'event_type': event_type,
            'secret_key': BOT_SECRET_KEY
        }
        logging.info(f"Sending data to PHP: {event_data}")

        response = requests.post(PHP_URL_ADD_EVENT, data=event_data)
        if response.status_code == 200:
            response_json = response.json()
            event_id = response_json.get('event_id')
            if event_id:
                await interaction.response.send_message(f'Event added successfully! Event ID: {event_id}', ephemeral=True)
            else:
                await interaction.response.send_message('Failed to get event ID.', ephemeral=True)
        else:
            await interaction.response.send_message(f'Failed to add event. Status code: {response.status_code}', ephemeral=True)


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="add_event", description="Add an event", guild_ids=[server_id])
    async def add_event(self, interaction: Interaction, event_name: str):
        logging.info("add_event command invoked.")
        response = requests.get(PHP_URL_GET_EVENT_TYPES)
        logging.info(f"PHP response status code for event types: {response.status_code}")
        if response.status_code == 200:
            event_types = response.json()
            logging.info(f"Fetched event types: {event_types}")
            # Ensure the event_name has the correct capitalization
            event_name = ' '.join([word if word.isupper() else word.capitalize() for word in event_name.split()])
            await interaction.response.send_message("Select the date for the event:", view=AddEventView(event_types, event_name), ephemeral=True)
        else:
            await interaction.response.send_message(f'Failed to fetch event types. Status code: {response.status_code}', ephemeral=True)


def setup(bot):
    bot.add_cog(Events(bot))