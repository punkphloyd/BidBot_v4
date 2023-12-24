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
from utils import debug_mode, ephemeral


# BidButtons class - this defines the top level set of buttons with which users will be presented upon the /bid2 function
# Buttons for Sky / Sea / Dyna / Limbus / HNMs
# Future content can be added with additional buttons
class BidButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Sky", style=nextcord.ButtonStyle.red)
    async def sky_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Sky bids", ephemeral=ephemeral)
        self.value = "Sky"
        self.stop()

    @nextcord.ui.button(label="Sea", style=nextcord.ButtonStyle.grey)
    async def sea_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Sea bids", ephemeral=ephemeral)
        self.value = "Sea"
        self.stop()

    @nextcord.ui.button(label="Dynamis", style=nextcord.ButtonStyle.blurple)
    async def dyna_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Dynamis bids", ephemeral=ephemeral)
        self.value = "Dynamis"
        self.stop()

    @nextcord.ui.button(label="Limbus", style=nextcord.ButtonStyle.green)
    async def limbus_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Limbus bids", ephemeral=ephemeral)
        self.value = "Limbus"
        self.stop()

    @nextcord.ui.button(label="HNM", style=nextcord.ButtonStyle.red)
    async def hnm_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("HNM bids", ephemeral=ephemeral)
        self.value = "HNM"
        self.stop()

    @nextcord.ui.button(label="HENM", style=nextcord.ButtonStyle.blurple)
    async def henm_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("HENM bids", ephemeral=ephemeral)
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
        print(bid_points)
        bid_level = int(level)

        # Check player and item exist (achieved with check_bid and dummy 0 points)
        # Points check must occur at point of application (otherwise would be possible for players to submit multiple bids
        # that (individually) they have points for, but cumulatively they do not
        bid_success, message_out = check_bid(player, bid_item, bid_points)
        if bid_success:
            await interaction.response.send_message(f"{player} has successfully placed a pending bid of {points} points on {item} - Note the points check will occur at the time of application")
            bid = [bid_time_month, bid_time_date, bid_time_hm, player, bid_item, bid_points, bid_level]
            if debug_mode:
                print(f"Bid to be written: {bid}")
            # bid_write(bid)

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

        bid_points = int(points)
        bid_level = int(level)

        bid_time = datetime.now()
        bid_time_hm = bid_time.strftime("%H:%M")
        bid_time_date = bid_time.strftime("%d")
        bid_time_month = bid_time.strftime("%m")

        date_now = datetime.now()
        date_in = date_now.strftime("%Y%m%d")
        bid_time = datetime.now()  # Get time of bid
        bid_time_min = bid_time.minute
        # Correction to prevent 3-digit timestamps
        if bid_time_min < 10:
            zero = "0"
        else:
            zero = ""

        date_now = datetime.now()
        date_in = date_now.strftime("%Y%m%d")
        # Prefix to log file
        log_filename_pre = "./logs/bid_bot.log_"
        log_filename = log_filename_pre + date_in
        if debug_mode:
            print("Bid2 Function Debugging")

        view = BidButtons()  # Output for Sky/Sea etc. choice
        view2 = None  # To be re-assigned later, pending initial EG Area choice
        view3 = None  # To be re-assigned later, pending initial EG Area choice
        await interaction.response.send_message("Select the end game content for your item bid", view=view)
        await view.wait()

        player = interaction.user.display_name  # Get player name from discord user displayname
        if debug_mode:
            print(f"{bid_time.hour}{zero}{bid_time.minute} User running /bid2 is {player}")

        if view.value is None:
            if debug_mode:
                print("View value of none has been reached - this should not be encountered; please examine logs")
            print(f"{player} has attempted a bid at {datetime} which has produced a view.value == None result", file=open(log_filename, 'a'))

        # Each option produces multiple sub-options; the majority of the code below is arranging the button interface for users to access
        # User selects sky option in first button options
        elif view.value == 'Sky':
            if debug_mode:
                print("Sky has been selected")
            view2 = SkyButtons()
            await interaction.followup.send("Which sky boss would you like?", view=view2)
            await view2.wait()

            # User offered then choice of gods for bids
            if view2.god == 'Kirin':
                if debug_mode:
                    print("Kirin has been selected")
                view3 = KirinButtons()
                await interaction.followup.send("Which Kirin drops would you like to bid on?", view=view3)
                await view3.wait()
            elif view2.god == 'Genbu':
                if debug_mode:
                    print("Genbu has been selected")
                view3 = GenbuButtons()
                await interaction.followup.send("Which Genbu drops would you like to bid on?", view=view3)
                await view3.wait()
            elif view2.god == 'Byakko':
                if debug_mode:
                    print("Byakko has been selected")
                view3 = ByakkoButtons()
                await interaction.followup.send("Which Byakko drops would you like to bid on?", view=view3)
                await view3.wait()
            elif view2.god == 'Suzaku':
                if debug_mode:
                    print("Suzaku has been selected")
                view3 = SuzakuButtons()
                await interaction.followup.send("Which Suzaku drops would you like to bid on?", view=view3)
                await view3.wait()
            elif view2.god == 'Seiryu':
                if debug_mode:
                    print("Seiryu has been selected")
                view3 = SeiryuButtons()
                await interaction.followup.send("Which Seiryu drops would you like to bid on?", view=view3)
                await view3.wait()
        ###########################
        # User selects HENM option in first button options
        elif view.value == 'HENM':
            if debug_mode:
                print("HENM has been selected")
            view2 = HENMButtons()
            await interaction.followup.send("Which HENM  would you like?", view=view2)
            await view2.wait()
            if view2 == 'Rocs':
                if debug_mode:
                    print("Rocs has been selected")
                view3 = RocsButtons()
                await interaction.followup.send("Which Ruinous Rocs drops would you like to bid on?", view=view3)
                await view3.wait()
            elif view2 == 'Decapod':
                if debug_mode:
                    print("Decapods has been selected")
                view3 = RocsButtons()
                await interaction.followup.send("Which Despotic Decapods drops would you like to bid on?", view=view3)
                await view3.wait()

        ###########################
        # User selects sea option in first button options
        elif view.value == 'Sea':
            if debug_mode:
                print("Sea has been selected")
            view2 = SeaButtons()
            await interaction.followup.send("Which sea boss would you like?", view=view2)
            await view2.wait()
            if view2.god == 'AV':
                if debug_mode:
                    print("AV has been selected")
                view3 = AVButtons()
                await interaction.followup.send("Which Absolute Virtue drops would you like to bid on?", view=view3)
                await view3.wait()

            if view2.god == 'Love':
                if debug_mode:
                    print("JoL has been selected")
                view3 = LoveButtons()
                await interaction.followup.send("Which Love drops would you like to bid on?", view=view3)
                await view3.wait()

            if view2.god == 'Justice':
                if debug_mode:
                    print("JoJ has been selected")
                view3 = JusticeButtons()
                await interaction.followup.send("Which Justice drops would you like to bid on?", view=view3)
                await view3.wait()

            if view2.god == 'Hope':
                if debug_mode:
                    print("JoH has been selected")
                view3 = HopeButtons()
                await interaction.followup.send("Which Hope drops would you like to bid on?", view=view3)
                await view3.wait()

            if view2.god == 'Prudence':
                if debug_mode:
                    print("JoP has been selected")
                view3 = PrudenceButtons()
                await interaction.followup.send("Which Prudence drops would you like to bid on?", view=view3)
                await view3.wait()

            if view2.god == 'Fortitude':
                if debug_mode:
                    print("JoFort has been selected")
                view3 = FortitudeButtons()
                await interaction.followup.send("Which Fortitude drops would you like to bid on?", view=view3)
                await view3.wait()

            if view2.god == 'Temperance':
                if debug_mode:
                    print("JoT has been selected")
                view3 = TemperanceButtons()
                await interaction.followup.send("Which Temperance drops would you like to bid on?", view=view3)
                await view3.wait()

            if view2.god == 'Faith':
                if debug_mode:
                    print("JoFaith has been selected")
                view3 = FaithButtons()
                await interaction.followup.send("Which Faith drops would you like to bid on?", view=view3)
                await view3.wait()

            if view2.god == 'Ix\'aern':
                if debug_mode:
                    print("Ixaerns has been selected")
                view3 = IxaernButtons()
                await interaction.followup.send("Which Ix'Aern drops would you like to bid on?", view=view3)
                await view3.wait()
        ###########################

        # User selects dynamis option in first button options
        # They are then offered choice of Dyna Lord vs Dyna Tav vs Job Relics
        # Dyna Lord / Tav implementation not properly coded yet
        # If user selects Job they are offered choice from Head-Feet, Acc, Head-1 - Feet-1
        # This is then combined to, e.g., BRD Feet, or MNK Head -1 this should then match up with the spreadsheet (once punk has updated spreadsheet accordingly)

        elif view.value == 'Dynamis':
            if debug_mode:
                print("Dynamis has been selected")
            view2 = DynaButtons()
            await interaction.followup.send("Which dynamis drops would you like to view?", view=view2)
            await view2.wait()

            # Not Dyna-Lord / Dyna-Tav == Relic pieces
            if not view2.god == 'Dynamis-Lord' and not view2.god == 'Dyna-Tav':
                if debug_mode:
                    print("Job relic has been selected")
                view3 = RelicButtons()
                await interaction.followup.send("Which relic piece would you like to view?", view=view3)
                await view3.wait()

                if debug_mode:
                    relic_drop = str(view2.god) + " " + str(view3.drop)
                    print(f"{relic_drop}")
            elif view2.god == 'Dynamis-Lord':  # If User selects Dyna Lord button, bring up dyna lord drops
                view3 = DynaLButtons()
            else:  # Else, only other option is Dyna-Tav - bring up dyna tav
                view3 = DynaTButtons()

        # For relic, bid item is concatenation of job and piece (e.g. MNK Legs / RDM Head -1)
        if view.value == 'Dynamis' and not view2.god == 'Dynamis-Lord' and not view2.god == 'Dyna-Tav':
            bid_item = str(view2.god) + " " + str(view3.drop)

        else:
            bid_item = view3.drop  # Has this been coded fully in DynaButtons.py? Need to check
        if debug_mode:
            print(bid_item)

        if debug_mode:
            print(f"{player} has bid {bid_points} points on item {view3.drop} at {bid_time}")

        # Print bid details to log file
        print(f"{player} has bid {bid_points} points on item {view3.drop} at {bid_time}", file=open(log_filename, 'a'))

        # Check player and item exist (achieved with check_bid and dummy 0 points)
        # Points check must occur at point of application (otherwise would be possible for players to submit multiple bids
        # that (individually) they have points for, but cumulatively they do not
        bid_success, message_out = check_bid(player, bid_item, 0)
        if bid_success:
            await interaction.response.send_message(f"{player} has successfully placed a pending bid of {points} points on {bid_item} - Note the points check will occur at the time of application")
            bid = [bid_time_month, bid_time_date, bid_time_hm, player, bid_item, bid_points, bid_level]
            if debug_mode:
                print(f"Bid to be written: {bid}")
            bid_write(bid)

        else:
            await interaction.response.send_message(f"The attempt for {player} to bid {bid_points} points on item {bid_item} was unsuccessful\n {message_out}")
            # Print failure to log file
        print(f"{bid_time} - Bid success: {bid_success} \n Message out: {message_out}", file=open(log_filename, 'a'))


# run the cog within the bot
def setup(bot):
    bot.add_cog(Bids(bot))
