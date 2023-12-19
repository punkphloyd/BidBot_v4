debug_mode = True


def letter_to_number(column_letter):
    """
    Convert Excel column letter to corresponding number.
    Example: 'A' -> 1, 'B' -> 2, 'Z' -> 26, 'AA' -> 27, 'AB' -> 28, and so on.
    """
    result = 0
    for char in column_letter:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result


def number_to_letter(column_number):
    """
    Convert Excel column number to corresponding letter.
    Example: 1 -> 'A', 2 -> 'B', 26 -> 'Z', 27 -> 'AA', 28 -> 'AB', and so on.
    """
    result = ""
    while column_number > 0:
        remainder = (column_number - 1) % 26
        result = chr(65 + remainder) + result
        column_number = (column_number - 1) // 26
    return result

