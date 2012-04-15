#!/usr/bin/env python3.2
"""
Dancing With the Googlers problem
for Google Code Jam 2012
Qualification

Link to problem description:
http://code.google.com/codejam/contest/1460488/dashboard#s=p1

author: 
Christos Nitsas
(chrisn654)

language:
Python 3.2.1

date:
April, 2012

usage:
$ python3.2 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
# non-standard modules:
from helpful import read_int, read_list_of_int


def compute_answer(totals, threshold, num_surprises):
    result = 0
    lowest_acceptable_total = max(2 * (threshold - 1) + threshold, 0)
    lowest_acceptable_with_surprise = max(2 * (threshold - 2) + threshold, 2)
    for total in totals:
        if total >= lowest_acceptable_total:
            result += 1
        elif num_surprises and total >= lowest_acceptable_with_surprise:
            result += 1
            num_surprises -= 1
    return result


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        num_cases = read_int(f)
        for i in range(1, num_cases + 1):
            input_list = read_list_of_int(f)
            n, s, p = input_list[0:3]
            totals = input_list[3:]
            print("Case #{0}: {1}".format(i, compute_answer(totals, p, s)))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

