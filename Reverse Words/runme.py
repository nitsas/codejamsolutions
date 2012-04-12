#!/usr/bin/env python3.2
"""
Reverse Words problem
for Google Code Jam Africa 2010
Qualification

Link to problem description:
http://code.google.com/codejam/contest/351101/dashboard#s=p1

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
from helpful import read_int, read_list_of_str


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        num_cases = read_int(f)
        for i, line in enumerate(f, 1):
            words = read_list_of_str(f)
            words.reverse()
            print("Case #" + str(i) + ": " + " ".join(words))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

