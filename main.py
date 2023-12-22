from Sheets import *
from api_keys import *

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

# Test