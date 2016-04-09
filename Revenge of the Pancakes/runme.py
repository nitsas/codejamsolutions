#!/usr/bin/env python3
"""
Revenge of the Pancakes problem
for Google Code Jam 2016
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/6254486/dashboard#s=p1

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


class OptimalNumFlipsCalculator:
    def __init__(self):
        self.cache = { '+': 0, '-': 1 }
        self.flip_pluses_minuses = str.maketrans('+-', '-+')
    
    def optimal_num_flips(self, stack):
        #
        # no need to touch trailing +'s
        stack = stack.rstrip('+')
        if len(stack) == 0:
            return 0
        #
        # fetch answer from cache if available
        if stack in self.cache:
            return self.cache[stack]
        #
        # - last char is a '-', so we'll need to flip up to the end for sure
        # - might as well have everything before it be a '-' too when we flip
        num_flips = 1 + self._optimal_num_flips_to_all_minus(stack[:-1])
        #
        # cache and return answer
        self.cache[stack] = num_flips
        return num_flips
    
    def _optimal_num_flips_to_all_minus(self, stack):
        return self.optimal_num_flips(stack.translate(self.flip_pluses_minuses))
    
    def _flip(stack, i=None):
        if i is None:
            i = len(stack)
        return stack[:i][::-1].translate(flip_pluses_minuses) + stack[i:]


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
        stacks = [line.strip('\n') for line in f]
    calculator = OptimalNumFlipsCalculator()
    for i, si in enumerate(stacks, start=1):
        print('Case #{}: {}'.format(i, calculator.optimal_num_flips(si)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
