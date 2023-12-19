from Sheets import *
from utils import *

cell_list = bids.range("A1:A3")

print(cell_list)

font_color = {'red': 1, 'blue': 0, 'green': 0}

for i in range(0,3):
    print(cell_list[i].value)


bids_KO = get_all_bids("Kirin's Osode")
print(bids_KO)

#for item in bids_KO:
#    print(item)
#    if len(bids_KO[item][1]) > 0:
#        colour = next(iter(bids_KO[item][1]))
#        print(f"Bid for {item} is {colour}")

player = 'Faraday'
item = 'W Legs'
points = 5
level = 75

pre_bid = get_player_bid(player, item)
print(f"Pre bid: {pre_bid}")


bids_WL = get_all_bids(item)
print(f"W Legs Bids: {bids_WL}")

bids_WL['Punkphloyd'] = [6, 1]
bids_WL['Steve'] = [3, 0]

update_bids(item, bids_WL)
