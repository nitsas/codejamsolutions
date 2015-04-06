#!/usr/bin/env python3
"""
Freecell Statistics problem
for Google Code Jam 2011
Round 1A

Link to problem description:
http://code.google.com/codejam/contest/1145485/dashboard#s=p0

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
# non-standard modules:
from helpful import read_int, read_list_of_int


def is_it_possible(N, PD, PG):
    if PG == 0:
        if PD == 0:
            return "Possible"
        else:
            return "Broken"
    elif PG == 100:
        if PD == 100:
            return "Possible"
        else:
            return "Broken"
    else:
        for d in range(1, N + 1):
            if (PD * d) % 100.0 == 0.0:
                return "Possible"
    return "Broken"


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
            N, PD, PG = read_list_of_int(f)
            print("Case #{0}: {1}".format(i, is_it_possible(N, PD, PG)))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

