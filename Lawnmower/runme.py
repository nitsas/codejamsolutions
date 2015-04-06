#!/usr/bin/env python3
"""
Lawnmower problem
for Google Code Jam 2013
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/2270488/dashboard#s=p1

Author: 
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.3)

Date:
  May, 2012

Usage:
  python3 runme.py input_file
"""


import sys
# modules I've written:
from helpful import read_int, read_list_of_int


def read_lawn_pattern(file, num_rows):
    return list(read_list_of_int(file) for i in range(num_rows))


def we_can_mown_it_horizontally(pattern, i, j):
    row_i = pattern[i]
    if pattern[i][j] >= max(row_i):
        return True
    else:
        return False


def we_can_mown_it_vertically(pattern, i, j):
    column_j = list(zip(*pattern))[j]
    if pattern[i][j] >= max(column_j):
        return True
    else:
        return False


def is_possible_pattern(pattern):
    num_rows = len(pattern)
    num_columns = len(pattern[0])
    for i in range(num_rows):
        for j in range(num_columns):
            if not (we_can_mown_it_horizontally(pattern, i, j) or 
                    we_can_mown_it_vertically(pattern, i, j)):
                return False
    return True


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print('Usage: runme.py input_file')
            return 1
    with open(filename, 'r') as f:
        num_test_cases = read_int(f)
        for i in range(1, num_test_cases + 1):
            num_rows, num_columns = read_list_of_int(f)
            lawn_pattern = read_lawn_pattern(f, num_rows)
            print('Case #{0}:'.format(i), end=' ')
            if is_possible_pattern(lawn_pattern):
                print('YES')
            else:
                print('NO')
    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
