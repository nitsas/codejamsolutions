#!/usr/bin/env python3
"""
Counting Sheep problem
for Google Code Jam 2016
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/6254486/dashboard#s=p0

Author:
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.4)

Date:
  April, 2016

Usage:
  python3 runme.py input_file
"""


import sys
import argparse
# modules I've written:
from helpful import *


_program_description = \
'''TEMPLATE PROGRAM DESCRIPTION'''


_input_file_description = \
'''TEMPLATE INPUT FILE DESCRIPTION'''


def last_num_before_sleep(start_num):
    if start_num == 0:
        return 'INSOMNIA'
    unseen_digits = set('0123456789')
    start_num = abs(start_num)
    current_num = 0
    while len(unseen_digits) > 0:
        current_num += start_num
        unseen_digits -= set(str(current_num))
    return current_num


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


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        num_test_cases = read_int(f)
        numbers = [int(line) for line in f]
    for i, nsi in enumerate(numbers, start=1):
        print('Case #{}: {}'.format(i, last_num_before_sleep(nsi)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
