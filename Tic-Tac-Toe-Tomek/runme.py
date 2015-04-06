#!/usr/bin/env python3
"""
Tic-Tac-Toe-Tomek problem
for Google Code Jam 2013
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/2270488/dashboard

author: 
Christos Nitsas
(chrisn654)

language:
Python 3.2.3

date:
May, 2012

usage:
$ python3 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
# non-standard modules:
from helpful import read_int


def read_test_case(file):
    game_board = []
    for i in range(4):
        game_board.append(file.readline().rstrip())
    file.readline() # consume empty line
    return game_board


def compute_game_status(game_board):
    four_tuples = extract_four_tuples(game_board)
    for four_tuple in four_tuples:
        if is_all_x(four_tuple):
            return "X won"
        elif is_all_o(four_tuple):
            return "O won"
    if has_a_dot(game_board):
        return "Game has not completed"
    else:
        return "Draw"


def extract_four_tuples(game_board):
    # first extract all rows:
    four_tuples = game_board
    # then extract all columns:
    four_tuples.extend(list(map("".join, zip(*game_board))))
    # last, extract the diagonals:
    four_tuples.append("".join((game_board[i][i] for i in range(4))))
    four_tuples.append("".join((game_board[i][3-i] for i in range(4))))
    return four_tuples
    

def is_all_x(four_tuple):
    if (('O' in four_tuple) or ('.' in four_tuple)):
        return False
    else:
        return True


def is_all_o(four_tuple):
    if (('X' in four_tuple) or ('.' in four_tuple)):
        return False
    else:
        return True


def has_a_dot(game_board):
    if ('.' in "".join(game_board)):
        return True
    else:
        return False


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        num_test_cases = read_int(f)
        for i in range(1, num_test_cases + 1):
            test_case = read_test_case(f)
            print("Case #{0}:".format(i), end=" ")
            print(compute_game_status(test_case))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

