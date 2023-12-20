from Sheets import *

# This main.py is currently setup as a test enrivonment for the Sheets.py functionality
# Tests how to implement she required sheets reading/writing

# Test function to return values from specific range of cells - bids is the Bids worksheet in the Google sheets
cell_list = bids.range("A1:A3")
print(cell_list)

# Standard font_colour dictionary for red text (only colour to be used in the bot)
font_colour = {'red': 1, 'blue': 0, 'green': 0}

# Test the individual response for 'value' output on a single cell
for i in range(0, 3):
    print(cell_list[i].value)

# Test 'get_all_bids' function
bids_KO = get_all_bids("Kirin's Osode")
print(bids_KO)

# Test a new bid, selected one with a point already assigned
player = 'Faraday'
item = 'W Legs'
points = 5
level = 75

# Get the pre-existing number of points bid (if no bids, returns 0)
pre_bid = get_player_bid(player, item)
print(f"Pre bid: {pre_bid}")

# Get all bids associated with this item
bids_WL = get_all_bids(item)
print(f"W Legs Bids: {bids_WL}")

# Manually add a couple of test bids, to be posted either in red (x,1) or black (x,0)
bids_WL['Punkphloyd'] = [6, 1]
bids_WL['Steve'] = [3, 0]

# function to update bids with new bids dictionary (in this case adding the two new bids outlined above for punkphloyd and steve)
update_bids(item, bids_WL)
