import gspread
from google.oauth2 import service_account
from google.auth import exceptions
from googleapiclient.discovery import build
from utils import debug_mode, letter_to_number, number_to_letter
from datetime import datetime
from api_keys import *

# Set up credentials used to connect my bidbot google service to the google sheets api
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/spreadsheets"])

# Worksheet numbers within main google sheets (need to update if extra sheets added)
bids_index = 2
roster_index = 0
points_index = 4

# Use get_worksheet method to open the worksheet by index
bids = gspread.authorize(credentials).open_by_key(spreadsheet_id).get_worksheet(bids_index)
roster = gspread.authorize(credentials).open_by_key(spreadsheet_id).get_worksheet(roster_index)
points = gspread.authorize(credentials).open_by_key(spreadsheet_id).get_worksheet(points_index)

# These return embedded lists containing all the rows, and their entries
bids_values = bids.get_all_values()
roster_values = roster.get_all_values()
points_values = points.get_all_values()


# Function to get font text color from a specific cell (row/col definition) on a specific worksheet
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


# function to return the value from a single cell (specified by worksheet, row, and column)
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
# This bid has not been revisited since the sheets refactoring
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

    # Sort bid list based on number of points
    bid_list = dict(sorted(dicto.items(), key=lambda tmp_item: tmp_item[1][0], reverse=True))

    if debug_mode:
        print("Printing bid_list")
        print(bid_list)
    # Formatting dictionary for red
    red_colour = {'red': 1}

    # Lists to store bid point values and a 0/1 list for cells needing to be red-font
    values = []
    red_track = []
    for item in bid_list:
        values.append(item)
        values.append(bid_list[item][0])
        red_track.append(bid_list[item][1])
    print(values)
    values_list = [values]
    print(red_track)

    try:
        # Update values via the 'update' function
        request = bids.update(range_notation, values_list)
        # Set all cells in the specified row to black text (will convert only required ones to red text)
        remove_row_font_color(bids, row)
        # Update required entries to red ink
        red_col = 3         # Start at 3 (this represents the first column with a numerical bid value in it - column C)
        for iterator in red_track:
            if iterator == 1:
                red_col_let = number_to_letter(red_col)
                set_cell_red(bids, red_col_let, row)

            red_col = red_col + 2

    except exceptions.DefaultCredentialsError:
        print("Google Sheets API credentials not found. Please provide valid credentials.")

    return


# Set a colour (RGB dictionary defined) to a specific cell of a worksheet
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


# Colour the text of a single cell red, defined by sheet column row
def set_cell_red(sheet, col, row):
    # Test to check if col has been given as a number
    if isinstance(col, int):
        # Convert to letter
        number_to_letter(col)

    cell_range = f"{col}{row}"
    # Get the existing content of the cell
    existing_content = sheet.cell(row, sheet.find(col).col).value

    # Define the red color dictionary
    red_colour = {
        "textFormat": {
            "foregroundColor": {
                "red": 1,
                "green": 0,
                "blue": 0
            }
        }
    }

    # Update the cell content and apply the red color format
    sheet.update(cell_range, existing_content, 'USER_ENTERED', red_colour)

    return

# This function removes the font colour from a row (part of the 65+/65- management)
def remove_row_font_color(sheet, row):

    # Loop through columns B->Z and individually remove any font colour
    # This process will be slower than other methods but more reliable
    # If number of parallel bids expands above ~12 this will need to be expanded accordingly
    for letter in range(ord('B'), ord('Z') + 1):
        letter = chr(letter)
        cell = f"{letter}{row}"
        if debug_mode:
            print(f"Cell to remove colour: {cell}")
        remove_font_color_from_cell(sheet, row, letter)


# Removes font colour from a single cell
def remove_font_color_from_cell(worksheet, row, column):
    """
    Remove font color from the specified cell in the worksheet.
    :param worksheet: The worksheet object.
    :param row: Row index (1-based).
    :param column: Column index or column letter.
    """
    # Test to check if col has been given as a number
    if isinstance(column, int):
        # Convert to letter
        number_to_letter(column)
    cell_range = f"{column}{row}" # s

    # Get the existing cell properties
    cell_properties = worksheet.cell(row, worksheet.find(column).col)

    # Extract existing format if available
    existing_format = cell_properties.get('userEnteredFormat', {}).get('textFormat', {})

    # Modify the existing format to remove font color
    existing_format['foregroundColor'] = None

    # Apply the modified format
    worksheet.format(cell_range, {'userEnteredFormat': existing_format})

