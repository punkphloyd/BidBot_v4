import nextcord
from api_keys import server_id
from nextcord.ext import commands, tasks
from nextcord import Interaction
from nextcord.ui import Select, View
from SkyGodButtons import *
from AreaButtons import *
from SeaGodButtons import *
from DynaButtons import *
from HENMButtons import *
from datetime import date, time, datetime
import time
from Sheets import *
from utils import debug_mode


# BidButtons class - this defines the top level set of buttons with which users will be presented upon the /bid2 function
# Buttons for Sky / Sea / Dyna / Limbus / HNMs
# Future content can be added with additional buttons
class BidButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Sky", style=nextcord.ButtonStyle.red)
    async def sky_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Sky bids", ephemeral=True)
        self.value = "Sky"
        self.stop()

    @nextcord.ui.button(label="Sea", style=nextcord.ButtonStyle.grey)
    async def sea_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Sea bids", ephemeral=True)
        self.value = "Sea"
        self.stop()

    @nextcord.ui.button(label="Dynamis", style=nextcord.ButtonStyle.blurple)
    async def dyna_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Dynamis bids", ephemeral=True)
        self.value = "Dynamis"
        self.stop()

    @nextcord.ui.button(label="Limbus", style=nextcord.ButtonStyle.green)
    async def limbus_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Limbus bids", ephemeral=True)
        self.value = "Limbus"
        self.stop()

    @nextcord.ui.button(label="HNM", style=nextcord.ButtonStyle.red)
    async def hnm_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("HNM bids", ephemeral=True)
        self.value = "HNM"
        self.stop()

    @nextcord.ui.button(label="HENM", style=nextcord.ButtonStyle.blurple)
    async def henm_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("HENM bids", ephemeral=True)
        self.value = "HENM"
        self.stop()


# Bids class which contains the logic to implement bid functions either manual (/bid) or button-led (/bid2)
class Bids(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="bid_test", description="Test of bid function", guild_ids=[server_id])
    async def test_bid(self, interaction: Interaction):
        await interaction.response.send_message("bid_test - function scratch")
    #########################################  BID FUNCTION #########################################

    # Function to add user bids (manual input)
    # This requires users to add their character name, the item to be bid upon, and the number of points they wish to bid (or increase their existing bid)
    # Currently function is not intelligent enough to correct spelling errors etc., so user must specify item correctly
    @nextcord.slash_command(name="bid", description="Bidbot bid function", guild_ids=[server_id])
    async def bid(self, interaction: Interaction, player, item, points, level):
        # Temporary: make function only accessible to admins
        role = nextcord.utils.get(interaction.guild.roles, name="Admin")
        if role in interaction.user.roles:
            if debug_mode:
                print(f"{interaction.user.display_name} has the role {role} - may successfully use the /bid function")
        else:
            await interaction.send("You must be an admin to use this command")
            if debug_mode:
                print(f"{interaction.user.display_name} does not have the role {role} - may not use the /bid function")
            return

        if debug_mode:
            print("Bid Function Debugging")
        bid_time = datetime.now()
        bid_time_hm = bid_time.strftime("%H:%M")
        bid_time_date = bid_time.strftime("%d")
        bid_time_month = bid_time.strftime("%m")

        date_now = datetime.now()
        date_in = date_now.strftime("%Y%m%d")
        # Prefix to log file
        log_filename_pre = "./logs/bid_bot.log_"
        log_filename = log_filename_pre + date_in

        # Transform player and item to title case - matches google sheets
        player = player.title()
        bid_item = item.title()
        bid_points = int(points)
        bid_level = int(level)

        # Check player and item exist (achieved with check_bid and dummy 0 points)
        # Points check must occur at point of application (otherwise would be possible for players to submit multiple bids
        # that (individually) they have points for, but cumulatively they do not
        bid_success, message_out = check_bid(player, bid_item, 0)
        if bid_success:
            await interaction.response.send_message(f"{player} has successfully placed a pending bid of {points} points on {item} - Note the points check will occur at the time of application")
            bid = [bid_time_month, bid_time_date, bid_time_hm, player, bid_item, bid_points, bid_level]
            if debug_mode:
                print(f"Bid to be written: {bid}")
            bid_write(bid)

        else:
            await interaction.response.send_message(f"The attempt for {player} to bid {points} points on item {item} was unsuccessful\n {message_out}")
            # Print failure to log file
        print(f"{bid_time} - Bid success: {bid_success} \n Message out: {message_out}", file=open(log_filename, 'a'))

    ###################################### BUTTON BID FUNCTION ######################################
    # This function is the button entry equivalent of the /bid function
    # Due to the button implementation it is quite cumbersome, if this can be refactored and simplified this should be considered
    # Use of this function requires the user's Discord Display Name to match that of their character on the Google sheets (should be case-insensitive - to be tested)
    # Currently (21/09/23) this would require Unholy & Nuppy to change their display names if they wish to use this method
    @nextcord.slash_command(name="bid2", description="Content for items to bid on", guild_ids=[server_id])
    async def bid_buttons(self, interaction: Interaction, points, level):
        # Temporary: make function only accessible to admins
        role = nextcord.utils.get(interaction.guild.roles, name="Admin")
        if role in interaction.user.roles:
            if debug_mode:
                print(f"{interaction.user.display_name} has the role {role} - may successfully use the /bid function")
        else:
            await interaction.send("You must be an admin to use this command")
            if debug_mode:
                print(f"{interaction.user.display_name} does not have the role {role} - may not use the /bid function")
            return

        if debug_mode:
            print("Bid2 Function Debugging")

        view = BidButtons()  # Output for Sky/Sea etc. choice
        view2 = None  # To be re-assigned later, pending initial EG Area choice
        view3 = None  # To be re-assigned later, pending initial EG Area choice
        await interaction.response.send_message("Select the end game content for your item bid", view=view)
        await view.wait()




# run the cog within the bot
def setup(bot):
    bot.add_cog(Bids(bot))
