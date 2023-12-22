from Sheets import *
from api_keys import *
import random
import time

# Get the current time as an integer
current_time = int(time.time())

# Set the random seed using the current time
random.seed(current_time)

# This main.py is currently setup as a test enrivonment for the Sheets.py functionality
# Tests how to implement she required sheets reading/writing

# Test function to return values from specific range of cells - bids is the Bids worksheet in the Google sheets
cell_list = bids.range("A1:A3")
print(cell_list)

# Standard font_colour dictionary for red text (only colour to be used in the bot)
red_colour = {'red': 1, 'blue': 0, 'green': 0}
blue_colour = {'red': 0, 'blue': 1, 'green': 0}
green_colour = {'red': 0, 'blue': 0, 'green': 1}
black_colour = {'red': 0.01, 'blue': 0.01, 'green': 0.01}

# Test the individual response for 'value' output on a single cell
for i in range(0, 3):
    print(cell_list[i].value)

print(get_font_color(6, 3, bids))
for row in range(1, 6):
    for col in range(1, 6):
        set_cell_red(bids, col, row)