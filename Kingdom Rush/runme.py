#!/usr/bin/env python3
"""
Kingdom Rush problem
for Google Code Jam 2012
Round 1A

Link to problem description:
http://code.google.com/codejam/contest/1645485/dashboard#s=p1

author: 
Chris Nitsas
(nitsas)

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
from operator import itemgetter, attrgetter
# non-standard modules:
from helpful import read_int, read_list_of_int
from KingdomRushLevel import KingdomRushLevel


def read_levels(file, num_lvls):
    return [KingdomRushLevel(*read_list_of_int(file)) for i in range(num_lvls)]


def min_needed_num_levels(levels):
    levels.sort(key=attrgetter('two_stars_req'))
    stars, num_levels_completed = 0, 0
    i = 0
    while i < len(levels):
        if stars >= levels[i].two_stars_req:
            stars += 2 - levels[i].rating
            levels[i].completed()
            num_levels_completed += 1
            i += 1
        else:
            for j in range(len(levels) - 1, i - 1, -1):
                if levels[j].rating == 0 and levels[j].one_star_req <= stars:
                    levels[j].completed(1)
                    num_levels_completed += 1
                    stars += 1
                    break
            else:
                return "Too Bad"
    return num_levels_completed
    

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
            num_levels = read_int(f)
            levels = read_levels(f, num_levels)
            print("Case #{0}: {1}".format(i, min_needed_num_levels(levels)))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

