#!/usr/bin/env python3
"""
Getting the Digits problem
for Google Code Jam 2016
Round 1B

Link to problem description:
https://code.google.com/codejam/contest/11254486/dashboard#s=p0

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
from collections import Counter
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


def decrypt_phone(letter_string):
    digit_count = [0] * 10
    letter_count = Counter(letter_string)
    
    # letters that are present only in a single number
    digit_count[0] = letter_count['Z']
    digit_count[2] = letter_count['W']
    digit_count[4] = letter_count['U']
    digit_count[6] = letter_count['X']
    digit_count[8] = letter_count['G']
    
    # letters that are present in more than one numbers
    digit_count[1] = (letter_count['O'] - digit_count[0] - digit_count[2] -
                      digit_count[4])
    digit_count[3] = letter_count['R'] - digit_count[0] - digit_count[4]
    digit_count[5] = letter_count['F'] - digit_count[4]
    digit_count[7] = letter_count['V'] - digit_count[5]
    digit_count[9] = (letter_count['N'] - digit_count[1] - digit_count[7]) // 2
    
    sanity_check(digit_count)
    
    return assemble_phone_string(digit_count)


def sanity_check(digit_count):
    for n in digit_count:
        assert(n >= 0)


def assemble_phone_string(digit_count):
    parts = []
    for digit, count in zip('0123456789', digit_count):
        parts.append(digit * count)
    return ''.join(parts)


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        num_test_cases = read_int(f)
        test_cases = [line.strip('\n') for line in f]
    for i, tc in enumerate(test_cases, start=1):
        print('Case #{}: {}'.format(i, decrypt_phone(tc)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
