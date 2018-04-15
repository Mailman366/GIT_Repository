import sys

if __name__ == "__main__":
    raise ImportError("This module is import only!")

TEST_BOARD = [
    [3, 0, 4, 0, 9, 0, 0, 5, 0],
    [0, 0, 7, 3, 5, 0, 2, 0, 4],
    [9, 5, 0, 0, 1, 4, 6, 0, 8],
    [5, 0, 0, 1, 6, 0, 8, 4, 0],
    [0, 0, 1, 9, 2, 5, 0, 0, 6],
    [2, 7, 6, 0, 0, 0, 0, 1, 9],
    [4, 2, 0, 0, 0, 9, 1, 6, 0],
    [0, 9, 5, 2, 0, 6, 0, 0, 3],
    [0, 6, 0, 8, 0, 1, 9, 2, 0]

]

TEST_BOARD_SMALL = [
    [0, 1, 3],
    [4, 0, 9],
    [6, 0, 5]

]


def print_board(board):
    """"
    Prints a pretty version of the board
    """
    if len(board) == 9 or len(board) == 3:
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

