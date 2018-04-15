from collections import Counter

def sanitize_board(input_board, acceptable_values):
    for l in input_board:
        for n, i in enumerate(l):
            if i not in acceptable_values:
                l[n] = '*'
    return input_board


def find_bad_cells(input_board, acceptable_values, x, y):

    MAX = (len(input_board))
    MIN = 1
    new_value = 0
    """
    print("Scanning: Row={} Column={}".format(x, y))
    for ln, lst in enumerate(input_board):
        for i, n in enumerate(lst):
    """