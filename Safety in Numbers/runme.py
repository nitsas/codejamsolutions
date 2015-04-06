#!/usr/bin/env python3
"""
Safety in Numbers problem
for Google Code Jam 2012
Round 1B

Link to problem description:
http://code.google.com/codejam/contest/1836486/dashboard#s=p0

Author: 
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.2)

Date:
  May, 2012

Usage:
  python3 runme.py input_file
"""


import sys
# modules I've written:
from helpful import read_int, read_list_of_int


def get_votes_needed_for_each_contestant(point_values):
    X = sum(point_values)
    votes_needed = []
    for Ji in point_values:
        votes_needed.append(max(100 * (2.0 / len(point_values) - (Ji / X)), \
                                0.0))
    percentage_votes_left = 100.0 - sum(votes_needed)
    non_zeroes = sum(map(lambda x: x > 0.0, votes_needed))
    percentage_to_add_to_each = percentage_votes_left / non_zeroes
    for i in range(len(votes_needed)):
        if votes_needed[i] > 0.0:
            votes_needed[i] += percentage_to_add_to_each
    return votes_needed


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print('Usage: runme.py input_file')
            return 1
    with open(filename, 'r', encoding='utf-8') as f:
        num_test_cases = read_int(f)
        for i in range(1, num_test_cases + 1):
            values = read_list_of_int(f)
            num_contestants = values[0]
            point_values = values[1:]
            votes_needed = get_votes_needed_for_each_contestant(point_values)
            print('Case #{0}:'.format(i), end=' ')
            for vi in votes_needed[:-1]:
                print('{0}'.format(vi), end=' ')
            print(votes_needed[-1])
    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
