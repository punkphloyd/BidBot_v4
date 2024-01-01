import os
debug_mode = True   # Debug mode controls numerous print to terminal messages to assist with development and debugging of bot
ephemeral = False

# Standard font_colour dictionary for differet text colours (only red colour to be used in the bot)
red_colour = {'red': 1, 'blue': 0, 'green': 0}
blue_colour = {'red': 0, 'blue': 1, 'green': 0}
green_colour = {'red': 0, 'blue': 0, 'green': 1}


# Function which converts an Excel column letter to the corresponding number
# E.g. A->1, B->2, Z->26, AA->27, AB->28 etc.
def letter_to_number(column_letter):
    result = 0
    for char in column_letter:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result


# Convert Excel column number to corresponding letter.
# 1->A, 2->B, 26->Z, 27->AA, 28->AB etc.
def number_to_letter(column_number):
    result = ""
    while column_number > 0:
        remainder = (column_number - 1) % 26
        result = chr(65 + remainder) + result
        column_number = (column_number - 1) // 26
    return result


data_dir = "./data/"
bid_close_filename = data_dir + "bid_close.tme"
logs_dir = "./logs/"
log_filename_pre = logs_dir + "bid_bot.log_"
bids_filename = data_dir + "bids.dat"


# Function to write bid out to bid datafile (will be called by both bid submission routines)
def bid_write(bid):
    # Check bid contains appropriate number of elements
    # Should contain:
    # Bid Month, Bid Date, Bid Time, Player, Item, Points
    # If not, print message and return out of function
    elements = len(bid)
    if elements != 7:
        print(f"Attempting to write a bid with an incorrect number of elements - should contain 7 elements, instead contains {elements}")
        return False
    else:
        if debug_mode:
            print(f"Writing bid to file - {bid} to {bids_filename}")
    # Check if bid file exists, if not then create
    # If exists, then append latest bid as a new line
    if os.path.exists(bids_filename):
        for item in bid:
            print(item + "\t", file=open(bids_filename, 'a'))
    else:
        print("# Month\tDate\tTime\tPlayer\tItem\tPoints\tPlayerLevel", file=open(bids_filename, 'w'))
        for item in bid:
            print(item + "\t", file=open(bids_filename, 'a'))
    return True
