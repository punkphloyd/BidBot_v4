import gspread
from google.oauth2 import service_account
from google.auth import exceptions
from googleapiclient.discovery import build
from utils import debug_mode, letter_to_number, number_to_letter
from datetime import datetime
from api_keys import *

# Set up credentials
credentials = service_account.Credentials.from_service_account_file("C:\\Users\\jarya\\PycharmProjects\\BidBot_v2/\\sheets_creds_v3.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])

bids_index = 2  # Worksheet number within main google sheets (need to update if extra sheets added)
roster_index = 0
points_index = 4

# Use get_worksheet method to open the worksheet by index
bids = gspread.authorize(credentials).open_by_key(spreadsheet_id).get_worksheet(bids_index)
roster = gspread.authorize(credentials).open_by_key(spreadsheet_id).get_worksheet(roster_index)
points = gspread.authorize(credentials).open_by_key(spreadsheet_id).get_worksheet(points_index)

bids_values = bids.get_all_values()
roster_values = roster.get_all_values()
points_values = points.get_all_values()


# Function to get font text color from a specific cell
def get_font_color(row, col, worksheet):
    service = build("sheets", "v4", credentials=credentials)
    sheet = service.spreadsheets()

    # Specify the fields parameter to request only the formatting information
    fields = "sheets(data.rowData.values(userEnteredFormat.textFormat.foregroundColor))"
    result = sheet.get(spreadsheetId=spreadsheet_id, ranges=[f"{worksheet.title}!{chr(ord('A') + col - 1)}{row}"], fields=fields).execute()

    # Extract the formatting information
    try:
        font_color = result['sheets'][0]['data'][0]['rowData'][0]['values'][0]['userEnteredFormat']['textFormat']['foregroundColor']
        if any(key == 'red' for key in font_color.keys()):
            return 1
        else:
            return 0
    except KeyError:
        return 'N/A'


def read_cell(row, col, worksheet):
    # Get the value from the specified cell
    value = worksheet.cell(row, col).value
    print(f"Value at cell ({row}, {col}): {value}")
    return value


# Function to check that the player bidding is present on the roster
def check_roster(player):
    player_present = False
    for rows in roster_values:
        if rows:
            if rows[0] == player:
                player_present = True
                break

    return player_present


# Check if item is present on the bids list
def check_item(item):
    item_present = False
    for rows in bids_values:
        if rows:
            if rows[0] == item:
                item_present = True
                break

    return item_present


# Check that a player has a sufficient number of points to place their bid
def check_points(player, points_in):
    has_points = False
    player_points = 0
    for rows in points_values:
        if rows:
            if rows[0] == player:
                if int(rows[4]) >= int(points_in):
                    has_points = True
                    if debug_mode:
                        print(f"{player} has  {rows[4]} points, this is greater than the {points_in} required - SUCCESS")
                    break
                else:
                    has_points = False
                    if debug_mode:
                        print(f"{player} does not have at least {points_in} points; they only have {rows[4]} points - FAIL")
    return has_points


# Single function to carry out all checks and collect any errors accordingly
def check_bid(player, item, points_in):
    # Date format to add to log file name (YYYYMMDD)
    date_now = datetime.now()
    date = date_now.strftime("%Y%m%d")
    time = date_now.strftime("%H:%M:%S")

    # Prefix to log file
    log_filename_pre = "./logs/bid_bot.log_"
    log_filename = log_filename_pre + date
    # Should produce a log file unique to each day - will need to factor in some sort of cleanup routine on the system (probably via cron)
    # So that only 1 week of log files are retained

    bid_success = False
    # Check if player exists in roster, otherwise failed bid
    player_present = check_roster(player)
    if player_present:
        # If player exists in roster, check item exists in biddable sheet, otherwise failed bid
        item_present = check_item(item)
        if item_present:
            # If player and item exist, check that bid is valid
            # (i.e. a whole integer >= 1 and the player has sufficient points), otherwise failed bid
            valid_points = points.isnumeric()
            has_points = check_points(player, points_in)
            if valid_points and has_points:
                if debug_mode:
                    print("All conditions met for bid - SUCCESS")
                bid_success = True
                valid_bid = "Bid successful"
                return bid_success, valid_bid
            else:
                if not valid_points:
                    points_not_valid = "You did not enter an acceptable input for points, please only enter integers greater than or equal to one"
                    bid_success = False
                    if debug_mode:
                        print(f"{points_in} is not an acceptable input")
                    return bid_success, points_not_valid
                elif not has_points:
                    points_not_present = f"{player} does not have at least {points_in} points to fulfill this bid"
                    bid_success = False
                    if debug_mode:
                        print(f"{player} does not have at least {points_in} points")
                    return bid_success, points_not_present

        else:
            item_not_present = f"{item} is not present on the biddable items list"
            if debug_mode:
                print(f"{item} is not an present on the biddable items list")
            bid_success = False
            return bid_success, item_not_present
    else:
        player_not_present = f"{player} is not present on the roster"
        bid_success = False
        if debug_mode:
            print(f"{player} is not present on the roster")
        return bid_success, player_not_present

    if bid_success:
        print(f" {time}: Bid success = {bid_success}", file=open(log_filename, 'a'))


# Function to return the existing number of points bid by a player on an item (if any)
def get_player_bid(player, item):
    pre_bid = 0
    all_bids = get_all_bids(item)
    if player in all_bids.keys():
        pre_bid = all_bids[player][0]
        if debug_mode:
            print("Player has a bid")

    return pre_bid


# Function to return all the bids against any item in pairs of "Player: Bid", held in a dictionary, key is player name, values is list of [points, 65+/<65]
# Keys = Player Names
# Values = Points, 1 or 2  (1 = 65+, 2 = no 65+)
# If empty, return None
def get_all_bids(item):
    all_bids = {}
    row_no = 0
    col_no = 1
    for row in bids_values:
        row_no = row_no + 1
        if row[0] == item:
            if len(row) == 1:
                return None
            else:
                bid_pairs_len = len(row) - 1 # Number of bid name+points cells is the total row length, less one for the item name
                print(f"length:{bid_pairs_len}")
                # Run over the length of the list and use every odd entry as a name (key) with the following even entry as the points bid (value)
                for i in range(1, bid_pairs_len+1, 2):
                    col_no = col_no + 2
                    col_letter = number_to_letter(col_no)
                    fon_col = get_font_color(row_no, col_no, bids)
                    print(f"{col_letter}{row_no}: {row[i+1]}")
                    if len(row[i+1].strip()) != 0:
                        bid_val_pair = [int(row[i+1]), fon_col]
                        all_bids[row[i]] = bid_val_pair

    return all_bids


# Function which will work out the cell ID (e.g., B7) for the given text
# Should only be used for item labels (possibly player labels also, but with caution)
# For items in bids and players on roster this should always be column 'A'
# However function is kept generic to allow for future requirements
# Response currently unknown if attempting to findcell with content that appears in more than one cell (e.g. a player name on the bids sheet)
def find_cell(text):
    not_item = False
    not_player = False
    # Start at A1 (1,1)
    row_num = 1
    col_num = 1
    # Check players on roster sheet first
    for row in roster_values:                              # Check each row in roster sheet values
        if text in row:                                 # When saught text found within row, define col_num as the index within the row and +1 (count from 0 vs 1)
            col_num = row.index(text) + 1
            break
        row_num = row_num + 1
        if row == roster_values[len(roster_values)-1]:
            not_player = True

    if not_player:
        row_num = 1
        col_num = 1
        for row in bids_values:
            if text in row:
                col_num = row.index(text) + 1
                break
            row_num = row_num + 1
            if row == bids_values[len(bids_values)-1]:
                not_player = True

    # if the result cannot be found in either items list or players list then simply return 0, 0
    # Can consider implementing further error catch/response later - but this should (in theory) never be encountered...
    if not_item and not_player:
        return 0, 0
    else:
        col_num = chr(ord('@')+col_num)
        return col_num, row_num


# This function updates the array of bids to reflect the new bid
def update_bids(item, dicto):

    # Find cell for item
    col, row = find_cell(item)
    updated_cell = str(col) + str(row)
    col_no = letter_to_number(col)
    if debug_mode:
        print(f"Col: {col} - Row: {row}")
    num_col = 2*len(dicto)+1
    let_col = number_to_letter(num_col)
    range_notation = f'B{row}:{let_col}{row}'
    print(f"range_notation: {range_notation}")
    if col != 'A':
        if debug_mode:
            print("Column is not A - should this be A?")
    else:
        # Cell to begin inserting updated bids from
        updated_cell = "B"+str(row)
        if debug_mode:
            print(f"Updated cell: {updated_cell}")

    # Convert dictionary to list to update spreadsheet
    # List needs to be 2-d to work with 'request' line below
    #bid_list = [list(functools.reduce(lambda x, y: x + y, dicto.items()))]
    bid_list = dict(sorted(dicto.items(), key=lambda tmp_item: tmp_item[1][0], reverse=True))
    #
    if debug_mode:
        print("Printing bid_list")
        print(bid_list)
    red_colour = {'red': 1}

    values = []
    red_track = []
    for item in bid_list:
        values.append(item)
        values.append(bid_list[item][0])
        red_track.append(bid_list[item][1])
    print(values)
    values_list = [values]
    print(red_track)
    # Execute request for spreadsheet update
    #
    #request = bids.update(spreadsheetId=spreadsheet_id, range=f"Bids!{updated_cell}", valueInputOption="RAW", body={"values": values}).execute()
    try:
        # Update values
        request = bids.update(range_notation, values_list)
        # Set all row to black text
        remove_row_font_color(bids, row)
        # Update required entries to red ink
        red_col = 3
        for iterator in red_track:
            if iterator == 1:
                red_col_let = number_to_letter(red_col)
                set_cell_red(bids, red_col_let, row)

            red_col = red_col + 2

    #col_tally = 3
    #for item in red_track:
    #    if item == 1:
    #        # Update colour of cell corresponding to {col_tally}{row} (e.g. C7, E7, etc.) to red
    #        set_cell_colour(bids, col_tally, row, red_colour)
    #    col_tally = col_tally + 2
    except exceptions.DefaultCredentialsError:
        print("Google Sheets API credentials not found. Please provide valid credentials.")


    return


def set_cell_colour(sheet, col, row, colour):
    body = {
        'requests': [
            {
                'updateCells': {
                    'rows': [
                        {
                            'values': [
                                {
                                    'userEnteredFormat': {
                                        'textFormat': {
                                            'foregroundColor': colour
                                        }
                                    }
                                }
                            ]
                        }
                    ],
                    'fields': 'userEnteredFormat.textFormat.foregroundColor',
                    'start': {
                        'sheetId': sheet.id,
                        'rowIndex': row,  # Convert 'A1' to row index
                        'columnIndex': col  # Convert 'A' to column index
                    }
                }
            }
        ]
    }

    # Make the update request
    request = bids.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body)
    response = request.execute()


def set_cell_red(sheet, col, row):
    cell_range = f"{col}{row}"
    red_colour = {"userEnteredFormat": {"textFormat": {"foregroundColor": {"red": 1, "green": 0, "blue": 0}}}}
    sheet.format(cell_range, red_colour)
    return


def remove_row_font_color(sheet, row):
    tmplock = 0
    if tmplock == 1:
        try:

            # Prepare the update request to clear font color formatting
            request = {
                'requests': [
                    {
                        'updateCells': {
                            'range': {
                                'sheetId': sheet.id,
                                'startRowIndex': row,  # Adjust as needed
                                'endRowIndex': row,  # Adjust as needed
                                'startColumnIndex': 0,  # Adjust as needed
                                'endColumnIndex': 10  # Adjust as needed
                            },
                            'fields': 'userEnteredFormat.textFormat.foregroundColor'
                        }
                    }
                ]
            }

            # Make the update request
            request = sheet.batchUpdate(spreadsheetId=spreadsheet_id, body=request)
            response = request.execute()

            print(f"Font color formatting removed from the row: {row}")

        except exceptions.DefaultCredentialsError:
            print("Google Sheets API credentials not found. Please provide valid credentials.")

    else:
        range_to_update = f"B{row}:Z{row}"
        format_req = {
            "userEnteredFormat": {
                "textFormat": {"foregroundColor": None}  # Set foregroundColor to None for default black color
            }
        }
        requests = [
            {
                'repeatCell': {
                    'range': f'{sheet.title}!B{row}:Z{row}',
                    'cell': {'userEnteredFormat': {'textFormat': {'foregroundColor': None}}},
                    'fields': 'userEnteredFormat.textFormat.foregroundColor'
                }
            }
        ]

        sheet.batch_update(requests)
