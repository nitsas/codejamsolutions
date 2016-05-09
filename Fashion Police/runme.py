#!/usr/bin/env python3
"""
Fashion Police problem
for Google Code Jam 2016
Round 1C

Link to problem description:
https://code.google.com/codejam/contest/4314486/dashboard#s=p2

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
from collections import namedtuple, defaultdict
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


TestCase = namedtuple('TestCase', ['J', 'P', 'S', 'K'])
Outfit = namedtuple('Outfit', ['j', 'p', 's'])


def outfits(tcase):
    J, P, S, K = tcase
    outfits_ = []
    
    jacket_pants = defaultdict(lambda: 0)
    jacket_shirt = defaultdict(lambda: 0)
    pants_shirt = defaultdict(lambda: 0)
    
    for j in range(1, J + 1):
        for p in range(1, P + 1):
            for s in range(1, S + 1):
                if jacket_pants[(j, p)] >= K:
                    continue
                if jacket_shirt[(j, s)] >= K or pants_shirt[(p, s)] >= K:
                    continue
                outfits_.append(Outfit(j, p, s))
                jacket_pants[(j, p)] += 1
                jacket_shirt[(j, s)] += 1
                pants_shirt[(p, s)] += 1
    
    left = []
    for j in range(1, J+1):
        for p in range(1, P + 1):
            for s in range(1, S + 1):
                if jacket_pants[(j, p)] < K and jacket_shirt[(j, s)] < K and pants_shirt[(p, s)] < K and (Outfit(j, p, s) not in outfits_):
                    left.append('{} {} {}'.format(j, p, s))
                    # print('{} {} {}'.format(j, p, s))
                    # print('  k: {}'.format(K))
                    # print('  jp: {}'.format(jacket_pants[(j, p)]))
                    # print('  js: {}'.format(jacket_shirt[(j, s)]))
                    # print('  ps: {}'.format(pants_shirt[(p, s)]))
    if left:
        print('--- combinations left ---')
        for comb in left:
            print(comb)
        print('------')
    
    return outfits_


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        num_test_cases = read_int(f)
        test_cases = []
        for i in range(num_test_cases):
            test_cases.append(TestCase(*read_list_of_int(f)))
    for i, tc in enumerate(test_cases, start=1):
        outfits_ = outfits(tc)
        print('Case #{}: {}'.format(i, len(outfits_)))
        for outfit in outfits_:
            print(' '.join(map(str, outfit)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
