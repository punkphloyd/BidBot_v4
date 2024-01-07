from datetime import datetime, time, timedelta
import os
import random

from utils import debug_mode
from api_keys import *
from nextcord.ext import commands, tasks
from Sheets import *
from utils import *

# Time to apply bids, and generate the next day's bid closure time
# This application time ensures bids will not be updated mid-event, and only 'take effect' the following day
bid_application_time = time(hour=23, minute=50)

# Two processes above (bid close time generation & bid application time) could probably be combined into a single time
# And managed via a single function
# TO DO: Consider amalgamation of these two functions


class Scheduler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.apply_bids.start()         # Start the scheduler for time based functions

        if debug_mode:
            print(f"{bid_application_time} is the bid action time")

    def cog_unload(self):
        if debug_mode:
            print(f"Bid scheduler unloaded at {datetime.now()}")
        self.apply_bids.cancel()

    # Function to apply bids at appropriate time
    # This function reads through the recorded bids (stored in text file and populated via the /bid /bid2 functions of the main
    # bot logic); checks them against bid window close timestamps, and then populates the active bids onto the spreadsheet accordingly
    @tasks.loop(time=bid_application_time)
    async def apply_bids(self):
        # Generate appropriate log filename first
        date = datetime.now()
        date = date.strftime("%Y%m%d")
        log_filename = log_filename_pre + date

        if debug_mode:
            print(f"It is {bid_application_time}, the program will now examine the day's bids and push valid bids to sheet")

        # Check if data directory exists, it not then create it (should exist)
        data_dir_exists = os.path.exists(data_dir)
        if not data_dir_exists:
            if debug_mode:
                print(f"Data directory {data_dir} did not exist, creating now")
            os.makedirs(data_dir)

        channel = self.bot.get_channel(bids_channel_id)
        await channel.send(f"Activating bids from {date} and generating bid close time for next day")
        # Initialise bid close time (bid_ct) and bid close file (bcf) prior to definition / reading
        bid_ct = 0
        bcf = None

        # Check bid deadline file exists, otherwise return an error
        bid_close_file = data_dir + "bid_close.tme"
        if os.path.exists(bid_close_file):
            bcf = open(bid_close_file, 'r')
            print(f"{bid_close_file} opened for reading", file=open(log_filename, 'a'))
        else:
            if debug_mode:
                print(f"Bid close timestamp file {bid_close_file} does not exist")
            await channel.send("Bid close timestamp file could not be found - see logs for further information")
            print(f"Error - unable to find bid deadline file {bid_close_file}", file=open(log_filename, 'a'))
            return
        # Read contents of bid close file (should be single line containing a single timestamp)
        numlines = len(bcf.readlines())
        if numlines != 1:
            if debug_mode:
                print(f"Too many lines in bid close file: {numlines} lines in {bcf}")
        for line in bcf:
            if debug_mode:
                print(line)
            bid_ct = line
        bcf.close()

        print(f"Bid close time for {date}: {bid_ct}", file=open(log_filename, 'a'))

        if debug_mode:
            print(f"Bid close time is : {bid_ct}")
        await channel.send(f"Bid close time for today was {bid_ct}")
        date_tmrw = datetime.now() + timedelta(days=1)
        print(f"Generating bid close time for {date_tmrw}", file=open(log_filename, 'a'))
        bc_file = open(bid_close_file, 'w')

        random_time = random.randint(0, 180)
        random_hour = int(random_time / 60)
        random_min = (random_time - 60 * random_hour)

        bid_close_hour = 16 + int(random_hour)
        bid_close_min = 0 + int(random_min)
        # Need this segment to prevent 3 digit timestamps from occurring for minutes returned with single digits
        if random_min < 10:
            zero = "0"
        else:
            zero = ""

        print(f"{bid_close_hour}{zero}{bid_close_min}", file=bc_file)  # Write bid close timestamp to file

        # Bids reading and action routine
        # Get bids data file
        bids_data_file = data_dir + "/bids.dat"
        bdf = None
        if os.path.exists(bids_data_file):
            bdf = open(bids_data_file,'r')
        else:
            if debug_mode:
                print(f"Failed to open bids data file: {bids_data_file}")
            await channel.send("Bids data file could not be opened - please see logs for further details")
            print(f"{date}: {time} - Failed to open bid file: {bids_data_file}", file=open(log_filename, 'a'))
            return

        # Cycle through bids data file and check if bid is good or bad
        # If bid is good, apply it to google sheets and move to next bid
        # If bid is bad, respond accordingly
        for line in bdf:
            if debug_mode:
                print(line)
            bid = line
            # Check if bid contains correct number of line items
            if len(bid) != 7:
                if debug_mode:
                    print(f"Bid: {bid} should be 7 items in length. It is {len(bid)}")
                print(f"Bid: {bid} should be 7 items in length. It is {len(bid)}", file=open(log_filename, 'a'))
                continue

            player = bid[3]
            item = bid[4]
            points = bid[5]
            level = int(bid[6])
            # Check level to determine 65+ or <65 (bids <65 will be recorded in red)
            if level >= 65:
                over65 = True
            else:
                over65 = False

            date = int(bid[1])
            month = int(bid[0])
            bid_time = bid[2]
            bid_time_hour = int(bid[2][:2])
            bid_time_min = int(bid[2][-2:])

            # Check if bid was prior to bid window closing
            # Get date month and time
            date_now = datetime.now().strftime("%d")
            month_now = datetime.now().month
            # Get data for bid close time in appropriate format
            hour_close = int(bid_ct[:2])
            min_close = int(bid_ct[-2:])

            # Check if bid was input prior to close of window
            # If bid was input in previous month, (either new month > old month, or new month == 1), then bid is good
            if month < month_now or (month_now == 1 and month == 12):
                bid_good = True
            else:
                # If same month, check date
                # If date is from at least 1 day prior, bid is good
                if date < int(date_now):
                    bid_good = True
                else:
                    # If bid is from same date, check timestamp again bid close timestamp
                    # If bid close hour is larger than bid application hour, bid is good
                    # Or if hours are equal, then bid close minute must exceed bid application minute
                    if bid_time_hour < hour_close or (bid_time_hour == hour_close and bid_time_min < min_close):
                        bid_good = True
                    else:
                        # If all previous tests have failed, bid has not been submitted prior to passage of
                        # at least one bid close window
                        # Therefore bid is not yet good and must remain on the stack
                        bid_good = False

            # Handle good/bad bids appropriately
            # Good bids are applied and removed from datafile
            # Bad bids are not pushed to sheet, remain on datafile for next day's application window(2350)

            if not bid_good:
                if debug_mode:
                    print(f"Bid not yet implemented, bid time: {bid_time}, bid window closed: {bid_ct} (Player: {player}, Item: {item}, Points: {points} ")
                return
            else:
                # Check if bid is good using player, item, and points values
                bid_success, message_out = check_bid(player, item, points)
                if bid_success:
                    await channel.send(f"Successful bid: {player} has bid {points} points on {item} as a pending bid")
                    # Print success to log file
                    print(f"{date} - Bid success: {bid_success} \n Message out: {message_out}", file=open(log_filename, 'a'))

                    # Copy logic from previous (non time-delay) routine for writing to sheets
                    # Get all existing bids on the corresponding item, and check if player already has an existing bid in place
                    # E.g., Fortitude Torque : Hammer bids 10, Shamrock	bids 7, and	Tasco bids 1
                    # This produces a dictionary which looks like:
                    # { 'Hammer': 10, 'Shamrock': 7, 'Tasco': 1 }
                    all_bids = get_all_bids(item)
                    if debug_mode:
                        print("Original bids: ")
                        print(all_bids)

                    pre_bid = get_player_bid(player, item)

                    if pre_bid != 0:  # i.e., player has points already in this item
                        new_points = int(points) + int(pre_bid)
                        all_bids[player] = new_points
                        if debug_mode:
                            print("Existing bids updated")
                            print(all_bids)
                    else:  # pre_points == 0 -> i.e. fresh bid on this item for this player
                        # Fresh bid - add new bid to this dictionary
                        all_bids[player] = points
                        if debug_mode:
                            print("New bid added:")
                            print(all_bids)

                    # bid_conv function to convert all points values to integers (code reads as strings otherwise)
                    #all_bids = bid_conv(all_bids)
                    # Sort all bids by points
                    #all_bids = bid_sort(all_bids)

                    if debug_mode:
                        # Printing out in debug mode to ensure that column and row being obtained is the one expected
                        print("column/row for bid_item: ")
                        col, row = find_cell(item)
                        print(f"{col}{row}")

                        print("column/row for player: ")
                        colp, rowp = find_cell(player)
                        print(f"{colp}{rowp}")

                    if debug_mode:
                        print(f"Implementing new bids onto {item}")
                    if debug_mode:
                        print("Sorted bids: ")
                        print(all_bids)
                    print(f"{date}/{month} {bid_time} - Adding bids: {all_bids} onto {item}", file=open(log_filename, 'a'))
                    update_bids(item, all_bids)
                # Otherwise, report to the player that the bid has failed and identify the diagnosed cause
                else:
                    await channel.send(f"The attempt for {player} to bid {points} points on item {item} was unsuccessful\n {message_out}")
                    # Print failure to log file
                    print(f"{bid_time} - Bid success: {bid_success} \n Message out: {message_out}", file=open(log_filename, 'a'))


# Function to run the cog within the bot
def setup(bot):
    bot.add_cog(Scheduler(bot))
