#!/usr/bin/env python3
"""
Consonants problem
for Google Code Jam 2013
Round 1C

Link to problem description:
https://code.google.com/codejam/contest/2437488/dashboard#s=p0

author: 
Chris Nitsas
(nitsas)

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
import re
# non-standard modules:
from helpful import read_int, read_list_of_str


def match_positions(string, n):
    num_consecutive_consonants = 0
    for i in range(len(string)):
        if string[i] in 'aeiou':
            # encountered a vowel
            num_consecutive_consonants = 0
        else:
            # encountered a consonant
            num_consecutive_consonants += 1
            if num_consecutive_consonants >= n:
                # found another match
                yield i - n + 1


def compute_n_value(name, n):
    n_value = 0
    leftmost_position = 0
    for mi in match_positions(name, n):
        # We want to count the number of substrings that start on 
        # leftmost_position or later and contain match mi:
        # - there are (mi - leftmost_position + 1) different options for the 
        #   start position of the substring 
        # - and (len(name) - mi - n + 1) different options for its end position
        n_value += (mi - leftmost_position + 1) * (len(name) - mi - n + 1)
        leftmost_position = mi + 1
    return n_value


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
            name, num = read_list_of_str(f)
            n = int(num)
            print("Case #{0}:".format(i), end=" ")
            print(compute_n_value(name, n))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

