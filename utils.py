debug_mode = True   # Debug mode controls numerous print to terminal messages to assist with development and debugging of bot


# Function which converts an excel column letter to the corresponding number
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

