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
from BattlefieldButtons import *
from datetime import date, time, datetime
import time
from Sheets import *
from utils import debug_mode, ephemeral, bids_filename, bid_close_filename, log_filename_pre, data_dir, bid_write
import os


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

    @nextcord.ui.button(label="Battlefields", style=nextcord.ButtonStyle.blurple)
    async def henm_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Battlefields bids", ephemeral=ephemeral)
        self.value = "Battlefields"
        self.stop()


# Bids class which contains the logic to implement bid functions either manual (/bid) or button-led (/bid2)
class Bids(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="bid_test", description="Test of bid function", guild_ids=[server_id])
    async def test_bid(self, interaction: Interaction):
        await interaction.response.send_message("bid_test - function scratch")

    # Function to allow admins to manually push bids from bids.dat to sheet
    # Used for debugging and development; debug_mode only
    @nextcord.slash_command(name="push_bids", description="Prints out contents of pending bids datafile", guild_ids=[server_id])
    async def push_bids(self, interaction: Interaction):
        if not debug_mode:
            await interaction.send("Debug_mode must be on for this function to be used")
            return

        # Function only accessible to admins
        role = nextcord.utils.get(interaction.guild.roles, name="Admin")
        if role in interaction.user.roles:
            if debug_mode:
                print(f"{interaction.user.display_name} has the role {role} - may successfully use the /print_bids function")
        else:
            await interaction.send("You must be an admin to use this command")
            if debug_mode:
                print(f"{interaction.user.display_name} does not have the role {role} - may not use the /push_bids function")
            return

        # Initiate manual bid pushing (same function as used in scheduler)
        # Generate appropriate log filename first
        date_push = datetime.now().strftime("%Y%m%d")
        time_push = datetime.now().strftime("%H:%M:%S")

        log_filename = log_filename_pre + date

        if debug_mode:
            print(f"It is {time_push}, the program will now examine the day's bids and push valid bids to sheet")
            await interaction.send(f"{time_push}: Bid push function activated - forces pushing of pending bids (in bids.dat) onto google sheets. Used for debugging and development only as this bypasses the scheduling/deadline elements.")

        # Check if bids.dat exists, it not then abort
        bids_exists = os.path.exists(bids_filename)
        if not bids_exists:
            if debug_mode:
                print(f"Bids file {bids_filename} did not exist, aborting function")
            await interaction.send(f"The bids file ({bids_filename}) does not exist. Aborting function.")
            return
        # Check if bids file is empty
        if os.path.getsize(bids_filename) == 0:
            await interaction.send("Bids file is currently empty")
            return

        # Presently unused code, will be required for implementation of push_bids to test delayed bids application
        # Once delayed push_bid functionality testing required, remove the commenting from the return lines in the elif/else segments
        # Check bid deadline file exists, otherwise return an error
        try:
            with open(bid_close_filename, 'r') as file:
                content = file.read()
                if not content:
                    print(f"Bid close timestamp file {bid_close_filename} does not exist")
                    await interaction.send(f"Bids close time file {bid_close_filename} cannot be found, or is empty.")
                    bid_ct = "19:00"  # Placeholder for debugging
                    # return

                numlines = len(file.readlines())
                if numlines != 1:
                    print(f"Too many lines in bid close file: {numlines} lines in {bid_close_filename}")
                    await interaction.send(f"Too many lines in bid close file: {numlines} lines in {bid_close_filename}")
                    bid_ct = "19:00"
                else:
                    bid_ct = file.read()
                    print(bid_ct)
        except FileNotFoundError:
            print(f"Bid close timestamp file {bid_close_filename} does not exist")
            await interaction.send(f"Bids close time file {bid_close_filename} cannot be found, or is empty.")
            bid_ct = "19:00"
            # return
        except Exception as e:
            print(f"An error occurred: {e}")
            bid_ct = "19:00"
        await interaction.send(f"Bid close time for {date_push} : {bid_ct}")

        # End of presently non-functional code-

        # If bids file exists and is not empty, open the file and loop through the contents line by line
        with open(bids_filename, "r") as bdf:
            line_no = 1
            for line in bdf:
                print(line)
                await interaction.send(f"Line no: {line_no} : {line}")
                bid_tmp = line

            # Check bid contains correct number of entries (7 items)
                if len(bid_tmp) != 7:
                    print(f"Bid: {bid_tmp} should be 7 items in length. It is {len(bid_tmp)}")
                    await interaction.send(f"Bid: {bid_tmp} should be 7 items in length. It is {len(bid_tmp)} - skipping bid.")
                    continue
                # Read bid entries
                player_tmp = bid_tmp[3]
                item_tmp = bid_tmp[4]
                points_tmp = int(bid_tmp[5])
                level_tmp = int(bid_tmp[6])

                # Check if level of bid submission is 65+ or not
                if level_tmp >= 65:
                    over65_tmp = True
                else:
                    over65_tmp = False

                # Including bid date/time and bid close time handling for future testing purposes, present implementation does not require
                date_tmp = int(bid_tmp[1])
                month_tmp = int(bid_tmp[0])
                bid_time_tmp = bid_tmp[2]
                bid_time_hour_tmp = int(bid_tmp[2][:2])
                bid_time_min_tmp = int(bid_tmp[2][-2:])

                # Check if bid was prior to bid window closing
                # Get date month and time
                date_now_tmp = datetime.now().strftime("%d")
                month_now_tmp = datetime.now().month
                # Get data for bid close time in appropriate format
                hour_close_tmp = int(bid_ct[:2])
                min_close_tmp = int(bid_ct[-2:])

                # Check if bid was input prior to window closure
                # If bid was input in previous month, (either new month > old month, or new month == 1), then bid is good
                if month_tmp < month_now_tmp or (month_now_tmp == 1 and month_tmp == 12):
                    bid_good = True
                else:
                    # If same month, check date
                    # If date is from at least 1 day prior, bid is good
                    if date_tmp < int(date_now_tmp):
                        bid_good = True
                    else:
                        # If bid is from same date, check timestamp again bid close timestamp
                        # If bid close hour is larger than bid application hour, bid is good
                        # Or if hours are equal, then bid close minute must exceed bid application minute
                        if bid_time_hour_tmp < hour_close_tmp or (bid_time_hour_tmp == hour_close_tmp and bid_time_min_tmp < min_close_tmp):
                            bid_good = True
                        else:
                            # If all previous tests have failed, bid has not been submitted prior to passage of
                            # at least one bid close window
                            # Therefore bid is not yet good and must remain on the stack
                            #bid_good = False
                            # Temporarily force bid_good as true
                            bid_good = True

                # Handle good / bad bids appropriately
                if not bid_good:
                    if debug_mode:
                        print(f"Bid not yet implemented, bid time: {bid_time_tmp}, bid window closed: {bid_ct} (Player: {player_tmp}, Item: {item_tmp}, Points: {points_tmp} ")
                        await interaction.send(f"Bid not yet implemented, bid time: {bid_time_tmp}, bid window closed: {bid_ct} (Player: {player_tmp}, Item: {item_tmp}, Points: {points_tmp} ")
                        print(f"{date} - Bid success: {bid_success} \n Message out: {message_out}", file=open(log_filename, 'a'))
                        return
                else:
                    # Check if bid is good using player, item, and points values
                    bid_success, message_out = check_bid(player_tmp, item_tmp, points_tmp)
                    if bid_success:
                        await interaction.send(f"Successful bid: {player_tmp} has bid {points_tmp} points on {item_tmp}")
                        # Print success to log file
                        print(f"{date} - Bid success: {bid_success} \n Message out: {message_out}", file=open(log_filename, 'a'))

                        # Code logic to apply and push new bid to sheet
                        # Copy logic from previous (non time-delay) routine for writing to sheets
                        # Get all existing bids on the corresponding item, and check if player already has an existing bid in place
                        # E.g., Fortitude Torque : Hammer bids 10, Shamrock	bids 7, and	Tasco bids 1
                        # This produces a dictionary which looks like:
                        # { 'Hammer': 10, 'Shamrock': 7, 'Tasco': 1 }
                        all_bids = get_all_bids(item_tmp)
                        if debug_mode:
                            print("Original bids: ")
                            print(all_bids)
                        ######
                        pre_bid = get_player_bid(player_tmp, item_tmp)

                        if pre_bid != 0:  # i.e., player has points already in this item
                            new_points = int(points_tmp) + int(pre_bid)
                            if over65_tmp:
                                all_bids[player_tmp] = [new_points, 0]
                            if not over65_tmp:
                                all_bids[player_tmp] = [new_points, 1]
                            if debug_mode:
                                print("Existing bids updated")
                                print(all_bids)
                        else:  # pre_points == 0 -> i.e. fresh bid on this item for this player
                            # Fresh bid - add new bid to this dictionary
                            if over65_tmp:
                                all_bids[player_tmp] = [points_tmp, 0]
                            if not over65_tmp:
                                all_bids[player_tmp] = [points_tmp, 1]
                            if debug_mode:
                                print("New bid added:")
                                print(all_bids)

                        # bid_conv function to convert all points values to integers (code reads as strings otherwise)
                        # all_bids = bid_conv(all_bids)
                        # Sort all bids by points
                        # all_bids = bid_sort(all_bids)

                        if debug_mode:
                            # Printing out in debug mode to ensure that column and row being obtained is the one expected
                            print("column/row for bid_item: ")
                            col, row = find_cell(item_tmp)
                            print(f"{col}{row}")

                            print("column/row for player: ")
                            colp, rowp = find_cell(player_tmp)
                            print(f"{colp}{rowp}")

                        if debug_mode:
                            print(f"Implementing new bids onto {item_tmp}")
                        if debug_mode:
                            print("Sorted bids: ")
                            print(all_bids)
                        print(f"{date_tmp}/{month_tmp} {bid_time_tmp} - Adding bids: {all_bids} onto {item_tmp}", file=open(log_filename, 'a'))
                        update_bids(item_tmp, all_bids)
                        # Otherwise, report to the player that the bid has failed and identify the diagnosed cause
                    else:
                        await interaction.send(f"The attempt for {player_tmp} to bid {points_tmp} points on item {item_tmp} was unsuccessful\n {message_out}")
                        # Print failure to log file
                        print(f"{bid_time_tmp} - Bid success: {bid_success} \n Message out: {message_out}", file=open(log_filename, 'a'))

    # Function to enable admins to print pending bids - used for debugging
    @nextcord.slash_command(name="print_bids", description="Prints out contents of pending bids datafile", guild_ids=[server_id])
    async def print_bids(self, interaction: Interaction):
        # Function only accessible to admins
        role = nextcord.utils.get(interaction.guild.roles, name="Admin")
        if role in interaction.user.roles:
            if debug_mode:
                print(f"{interaction.user.display_name} has the role {role} - may successfully use the /print_bids function")
        else:
            await interaction.send("You must be an admin to use this command")
            if debug_mode:
                print(f"{interaction.user.display_name} does not have the role {role} - may not use the /print_bids function")
            return

        # Check that the bids file exists
        if os.path.exists(bids_filename):

            # Check if bids file is empty
            if os.path.getsize(bids_filename) == 0:
                await interaction.send("Bids file is currently empty")
            else:
                # Open bids file
                with open(bids_filename, "r") as file:
                    line_no = 1
                    # Iterate line-by-line and print out to console and discord
                    for line in file:
                        line = line.strip()
                        print(line)
                        await interaction.send(f"Line {line_no}: {line}")
                        line_no = line_no + 1
        else:
            await interaction.send(f"Bids file ({bids_filename}) could not be located, please see logfile for debugging information")
            print(f"Bids file {bids_filename} could not be located for print_bids function")


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
        await interaction.response.send_message("Select the end game content for your item bid", view=view, ephemeral=ephemeral)
        await view.wait()

        player = interaction.user.display_name  # Get player name from discord user displayname
        player = player.title()
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
            bid_item = view3.drop
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

            bid_item = view3.drop
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

            bid_item = view3.drop
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
            if not view2.god == 'Dynamis-Lord' and not view2.god == 'Dynamis-Tav':
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
            if view.value == 'Dynamis' and not view2.god == 'Dynamis-Lord' and not view2.god == 'Dynamis-Tav':
                bid_item = str(view2.god) + " " + str(view3.drop)

            else:
                bid_item = view3.drop  # Has this been coded fully in DynaButtons.py? Need to check
            if debug_mode:
                print(bid_item)
        elif view.value == 'Battlefields':
            view2 = BattlefieldButtons()
            await interaction.followup.send("Which battlefield would you like to view?", view=view3)
            await view2.wait()

            if view2.god == "Waking":
                view3 = WTBButtons()
                await interaction.followup.send("Which Waking the Beast piece would you like to bid on?", view=view3)
                await view3.wait()

            elif view2.god == "Bahamut":
                view3 = BahamutButtons()
                await interaction.followup.send("Which Bahamutv2 piece would you like to bid on?", view=view3)
                await view3.wait()

            elif view2.god == "KS99":
                view3 = KS99Buttons()
                await interaction.followup.send("Which KS99 piece would you like to bid on?", view=view3)
                await view3.wait()
            else:
                print('This situation should never be reached')
                view3.drop = None
        else:
            print('This situation should never be reached')
            view3.drop = None

        if debug_mode:
            print(f"{player} has bid {bid_points} points on item {view3.drop} at {bid_time}")

        # Print bid details to log file
        print(f"{player} has bid {bid_points} points on item {view3.drop} at {bid_time}", file=open(log_filename, 'a'))

        # Check player and item exist (achieved with check_bid and dummy 0 points)
        # Points check must occur at point of application (otherwise would be possible for players to submit multiple bids
        # that (individually) they have points for, but cumulatively they do not
        bid_success, message_out = check_bid(player, bid_item, bid_points)
        if bid_success:
            await interaction.followup.send(f"{player} has successfully placed a pending bid of {points} points on {bid_item} - Note the points check will occur at the time of application")
            bid = [bid_time_month, bid_time_date, bid_time_hm, player, bid_item, bid_points, bid_level]
            if debug_mode:
                print(f"Bid to be written: {bid}")
            bid_write(bid)

        else:
            await interaction.followup.send(f"The attempt for {player} to bid {bid_points} points on item {bid_item} was unsuccessful\n {message_out}")
            # Print failure to log file
        print(f"{bid_time} - Bid success: {bid_success} \n Message out: {message_out}", file=open(log_filename, 'a'))


# run the cog within the bot
def setup(bot):
    bot.add_cog(Bids(bot))
