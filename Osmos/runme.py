#!/usr/bin/env python3
"""
Osmos problem
for Google Code Jam 2013
Round 1B

Link to problem description:
https://code.google.com/codejam/contest/2434486/dashboard

author: 
Christos Nitsas
(chrisn654)

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
from math import ceil, floor, log2
# non-standard modules:
from helpful import read_int, read_list_of_int


def round_up_to_next_power_of_2(num):
    """Returns the smallest power of 2 that is bigger than the given number."""
    return 2 ** (floor(log2(num)) + 1)


def min_number_of_operations_needed(current_size, other_motes_sizes):
    if current_size == 1:
        # the mote can't eat any of the other motes nor any of 
        # the motes we could add; we have to delete all other motes
        return len(other_motes_sizes)
    other_motes_sizes.sort()
    for i in range(len(other_motes_sizes)):
        if other_motes_sizes[i] < current_size:
            current_size += other_motes_sizes[i]
        else:
            # either delete all the remaining motes or add enough smaller 
            # motes to eat this one and continue checking the rest of the motes
            X = round_up_to_next_power_of_2(floor( (other_motes_sizes[i] - 1) / (current_size - 1)))
            number_of_operations_needed_to_eat_this_mote = ceil(log2(X))
            new_size = X * (current_size - 1) + 1 + other_motes_sizes[i]
            return min( len(other_motes_sizes) - i, number_of_operations_needed_to_eat_this_mote + min_number_of_operations_needed(new_size, other_motes_sizes[i+1:]))
    # if no motes left
    return 0


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
            current_size, num_other_motes = read_list_of_int(f)
            other_motes_sizes = read_list_of_int(f)
            print("Case #{0}:".format(i), end=" ")
            print(min_number_of_operations_needed(current_size, other_motes_sizes))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

