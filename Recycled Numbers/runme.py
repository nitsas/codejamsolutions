#!/usr/bin/env python3
"""
Recycled Numbers problem
for Google Code Jam 2012
Qualification

Link to problem description:
http://code.google.com/codejam/contest/1460488/dashboard#s=p2

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
from helpful import read_int, read_list_of_int


def count_recycled_pairs(A, B):
    result = 0
    for n in range(A, B):
        sn = str(n)
        set_of_m = set()
        for m in (int(sn[i:] + sn[0:i]) for i in range(-1, -len(sn), -1)):
            if m > n and m <= B:
                set_of_m.add(m)
        result += len(set_of_m)
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
            A, B = read_list_of_int(f)
            print("Case #{0}: {1}".format(i, count_recycled_pairs(A, B)))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

