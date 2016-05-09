#!/usr/bin/env python3
"""
Senate Evacuation problem
for Google Code Jam 2016
Round 1C

Link to problem description:
https://code.google.com/codejam/contest/4314486/dashboard#s=p0

Author:
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.4)

Date:
  May, 2016

Usage:
  python3 runme.py input_file
"""


import sys
import argparse
from string import ascii_uppercase
# modules I've written:
from helpful import *


_program_description = \
'''TEMPLATE PROGRAM DESCRIPTION'''


_input_file_description = \
'''TEMPLATE INPUT FILE DESCRIPTION'''


def parse_args():
    """
    Parse the command line arguments and return them in a namespace.
    """
    parser = argparse.ArgumentParser(description=_program_description)
    parser.add_argument('input_file', help=_input_file_description)
    #parser.add_argument('-v', '--verbose', action='store_true',
    #                    default=False, help='show progress')
    args = parser.parse_args()
    return args


class Party:
    def __init__(self, name, count):
        self.name = name
        self.count = count
    def __str__(self):
        return self.name


def evacuation_plan(parties):
    # parties are sorted from largest to smallest
    plan_steps = []
    # - part 1: evacuate from 1st party until it's equal in number to the 2nd one
    while parties[0].count > parties[1].count + 1:
        plan_steps.append('{}{}'.format(parties[0], parties[0]))
        parties[0].count -= 2
    if parties[0].count == parties[1].count + 1:
        plan_steps.append('{}'.format(parties[0]))
        parties[0].count -= 1
    else:
        assert(parties[0].count == parties[1].count)
    # - part 2: evacuate all parties except for the first two
    for i in range(2, len(parties)):
        while parties[i].count > 1:
            plan_steps.append('{}{}'.format(parties[i], parties[i]))
            parties[i].count -= 2
        if parties[i].count == 1:
            plan_steps.append('{}'.format(parties[i]))
            parties[i].count -= 1
        else:
            assert(parties[i].count == 0)
    # - part 3: evacuate senators from the first two parties in pairs
    #           (i.e. one from the 1st party paired with one from the 2nd one)
    while parties[0].count > 0:
        plan_steps.append('{}{}'.format(parties[0], parties[1]))
        parties[0].count -= 1
        parties[1].count -= 1
    for party in parties:
        assert(party.count == 0)
    return ' '.join(plan_steps)


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        num_test_cases = read_int(f)
        test_cases = []
        for tci in range(num_test_cases):
            num_parties = read_int(f)
            counts = read_list_of_int(f)
            parties = []
            for name, count in zip(ascii_uppercase, counts):
                parties.append(Party(name, count))
                parties.sort(key=lambda p: p.count, reverse=True)
            test_cases.append(parties)
    for i, tc in enumerate(test_cases, start=1):
        print('Case #{}: {}'.format(i, evacuation_plan(tc)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
