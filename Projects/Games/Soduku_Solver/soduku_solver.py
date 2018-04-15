import sys
import argparse
from test_board import TEST_BOARD, TEST_BOARD_SMALL, print_board
from JimmysAwesomeSolutionTM import solve


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-s', '--solution', choices=['chris', 'jimmy'], help='Choose a solution to use')
    return parser.parse_args()



if __name__ == "__main__":
    """
    Currently working on TEST_BOARD_SMALL which is a 3x3 board.
    """
    #print_board(TEST_BOARD_SMALL)

    #print_board(TEST_BOARD)

    ARGS = parse_arguments()
    if ARGS.solution == 'chris':
        pass
        # ARGS.solution(TEST_BOARD)
    elif ARGS.solution == 'jimmy':
        solve(TEST_BOARD)
        # ARGS.solution(TEST_BOARD)




    sys.exit(0)

