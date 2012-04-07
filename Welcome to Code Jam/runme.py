#!/usr/bin/env python3.2
"""
Welcome to Code Jam problem
for Google Code Jam 2009
Qualification Round
(http://code.google.com/codejam/contest/dashboard?c=90101#s=p2)

author: 
Christos Nitsas
(chrisn654)

language:
Python 3.2.1

date:
April, 2012

usage:
$ python3 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
# non-standard modules:
from helpful import read_int


# Count the times the suquence of letters in substring appears in string. 
# Letters of substring can appear scattered. Use dynamic programming.
def count_matches_smart(substring, string):
    if not string:
        return 0
    suffix_matches_after_position = {}
    suffix_matches_after_position[substring[-1]] = find_letter_matches_after_position(substring[-1], string)
    for suffix in suffixes(substring, -2):
        suffix_matches_after_position[suffix] = find_suffix_matches_after_position(suffix, string, suffix_matches_after_position[suffix[1:]])
    return suffix_matches_after_position[substring][0]


# Generator. Return all suffixes of string. Only get suffixes starting 
# on or before position index (in string).
def suffixes(string, index=-1):
    for i in range(index, -len(string) - 1, -1):
        yield string[i:]


# Return a "number of matches after position" table for letter (in string),
# given nothing. Use find_suffix_matches_after_position().
# (position interpreted as in slice notation)
def find_letter_matches_after_position(letter, string):
    magic = [1 for pos in range(len(string) + 1)]
    return find_suffix_matches_after_position(letter, string, magic)


# Return a "number of matches after position" table for suffix (in string), 
# given the "number of matches after position table" for suffix[1:]. 
# (position interpreted as in slice notation)
def find_suffix_matches_after_position(suffix, string, rest_pattern_matches_after_position):
    matches_after_position = [0 for p in range(len(string))]
    for pos in rfindall(suffix[0], string):
        if pos + 1 < len(rest_pattern_matches_after_position):
            matches_after_pos = rest_pattern_matches_after_position[pos + 1]
            for i in range(pos + 1):
                matches_after_position[i] += matches_after_pos
    return matches_after_position


# Generator. Find all occurences of substring in string. Higher indices first.
def rfindall(substring, string):
    pos = string.rfind(substring)
    while pos != -1:
        yield pos
        pos = string.rfind(substring, 0, pos)


def main():
    if len(sys.argv) != 2:
        print("Usage: runme.py input_file")
        return 1
    with open(sys.argv[1], "r") as f:
        N = read_int(f)   # not needed
        for i, line in enumerate(f):
            count = count_matches_smart("welcome to code jam", line)
            print("Case #" + str(i + 1) + ": " + str(count).zfill(4)[-4:])
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

