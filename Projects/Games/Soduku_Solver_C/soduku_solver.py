import sys
import argparse
from test_board import TEST_BOARD_EASY
from chris_awesome_solution import sanitize_board, find_bad_cells

# Constants
ACCEPTABLE_VALUES = [i for i in range(1, 10)]  # This returns 1 - 9

"""
def print_board(board):
    print('=====================================')
    for row in board:
        for i in range(1, 3):
            print("={},{},{}=".format(str(row[i]), str(row[i+1]), str(row[i+2])))
    return
"""

def print_board(board):
    """"
    Prints a pretty version of the board
    """
    if len(board) == 9:
        for i in range(len(board)):
            if i % 3 == 0:
                print("-"*(3*len(board)-2))

            for x in range(len(board[i])):
                if x % 3 == 0:
                    print("| ", end="")
                print(board[i][x], end=" ")
            print("|")
            #print(str(board[i]))
        print("-" * (3 * len(board) - 2))
    else:
        raise Exception("List is not 9 items long!")

if __name__ == "__main__":
    active_board = TEST_BOARD_EASY
    active_board = sanitize_board(active_board, ACCEPTABLE_VALUES)
    print_board(active_board)

    sys.exit(0)
