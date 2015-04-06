#!/usr/bin/env python3
"""
Store Credit problem
for Google Code Jam Africa 2010
Qualification

Link to problem description: 
http://code.google.com/codejam/contest/351101/dashboard#s=p0

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
# non-standard modules:
from helpful import read_int, read_list_of_int


def choose_items(credit, prices):
    for i1, p in enumerate(prices):
        if credit > p:
            whats_left = credit - p
            for i2 in range(i1 + 1, len(prices)):
                if prices[i2] == whats_left:
                    return i1, i2


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
            credit = read_int(f)
            num_items = read_int(f)
            prices = read_list_of_int(f)
            index1, index2 = choose_items(credit, prices)
            index1, index2 = index1 + 1, index2 + 1
            print("Case #" + str(i) + ": " + str(index1) + " " + str(index2))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

