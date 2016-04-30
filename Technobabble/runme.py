#!/usr/bin/env python3
"""
Technobabble problem
for Google Code Jam 2016
Round 1B

Link to problem description:
https://code.google.com/codejam/contest/11254486/dashboard#s=p2

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


def max_possible_num_of_fakes(topics):
    return len(topics) - min_num_of_originals(topics)


def min_num_of_originals(topics):
    """
    The number of originals is at least as big as max(number of
    different first words, number of different second words).
    """
    first_words = set(topic[0] for topic in topics)
    second_words = set(topic[1] for topic in topics)
    
    return max(len(first_words), len(second_words))


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        num_test_cases = read_int(f)
        test_cases = []
        for i in range(num_test_cases):
            num_topics = read_int(f)
            topics = [read_list_of_str(f) for j in range(num_topics)]
            test_cases.append(topics)
    for i, tc in enumerate(test_cases, start=1):
        print('Case #{}: {}'.format(i, max_possible_num_of_fakes(tc)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
