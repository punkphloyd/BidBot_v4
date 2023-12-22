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

# Test the addition of new bids, and the addition/persistence of font colours appropriately
# Add some bids to the W Legs entry, one 65+ one <65
# Also amended notique's bid to be <65 and confirm that this persists throughout the update

# Get existing bids
base_WL = get_all_bids("W Legs")
print(base_WL)

# Add new bids to base_WLegs
base_WL['Punkphloyd'] = [8, 1]
base_WL['Steve'] = [3, 0]

# Update spreadsheet to these bids
update_bids("W Legs", base_WL)