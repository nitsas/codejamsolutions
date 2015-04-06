#!/usr/bin/env python3
"""
Minimum Scalar Product problem
for Google Code Jam 2008
Round 1A

Link to problem description:
http://code.google.com/codejam/contest/32016/dashboard#s=p0

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
import operator
# non-standard modules:
from helpful import read_int, read_list_of_int


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
            vector_length = read_int(f)
            v1 = read_list_of_int(f)
            v2 = read_list_of_int(f)
            v1.sort()
            v2.sort(reverse=True)
            print("Case #{0}: {1}".format(i, sum(map(operator.mul, v1, v2))))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

