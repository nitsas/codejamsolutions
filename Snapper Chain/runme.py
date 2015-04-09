#!/usr/bin/env python3
"""
Snapper Chain problem
for Google Code Jam 2010
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/433101/dashboard#s=p0

Author: 
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.4)

Date:
  April, 2015

Usage:
  python3 runme.py input_file
"""


import sys
import argparse
import collections
# modules I've written:
from helpful import *


_program_description = \
'''TEMPLATE PROGRAM DESCRIPTION'''


_input_file_description = \
'''TEMPLATE INPUT FILE DESCRIPTION'''


TestCase = collections.namedtuple('TestCase', ['N', 'K'])


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


def compute_end_state_of_light_bulb(N, K):
    """
    Return "ON" if the light bulb is on after K finger snaps; "OFF" otherwise.
    
    The light bulb is connected to a power socket through N Snappers.
    
    We view the N Snappers as an N-digit binary number S. 
    - Imagine that each Snapper is a digit, the power socket is on the far 
      right (after the least significant digit) and the light bulb on the 
      far left (connected to the most significant digit). 
    - S starts starts off at 0 and every snap increases it by 1. S being
      N-digit means that the 2**N'th snap gets it back to 0. This means we
      must check K modulo 2**N.
    - The light bulb will be on only when all Snappers are on, i.e. all 
      digits are 1, i.e. S == (2**N) - 1.
    """
    if K % (2**N) == (2**N) - 1:
        return "ON"
    else:
        return "OFF"


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        T = read_int(f)
        test_cases = list(TestCase(*read_list_of_int(f)) for i in range(T))
    for i, tc in enumerate(test_cases, start=1):
        print("Case #{}: {}".format(i, compute_end_state_of_light_bulb(*tc)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
