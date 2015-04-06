#!/usr/bin/env python3
"""
Equal Sums problem
for Google Code Jam 2012
Round 1B

Link to problem description:
http://code.google.com/codejam/contest/1836486/dashboard#s=p2

author: 
Chris Nitsas
(nitsas)

language:
Python 3.2.1

date:
May, 2012

usage:
$ python3 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
import itertools
# non-standard modules:
from helpful import read_int, read_list_of_int


def all_subsets(numbers):
    for r in range(1, len(numbers) + 1):
        for subset in itertools.combinations(numbers, r):
            yield subset


def get_subsets_with_equal_sum(numbers):
    sums = dict()
    for subset in all_subsets(numbers):
        sum_of_subset = sum(subset)
        if sum_of_subset not in sums:
            sums[sum_of_subset] = subset
        else:
            return (subset, sums[sum_of_subset])
    return "Impossible"


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        T = read_int(f)
        for i in range(1, T + 1):
            values = read_list_of_int(f)
            numbers = values[1:]
            print("Case #{0}:".format(i))
            subsets = get_subsets_with_equal_sum(numbers)
            for subset in subsets:
                if subset is "Impossible":
                    print("Impossible")
                else:
                    for num in subset[:-1]:
                        print("{0}".format(num), end=" ")
                    print(subset[-1])
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

