#!/usr/bin/env python3.3
"""
--Problem Name-- problem
for Google Code Jam --Year--
--Round--

Link to problem description:
--Link--

author: 
Christos Nitsas
(chrisn654)

language:
Python 3.2.3

date:
May, 2012

usage:
$ python3.2 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
# non-standard modules:
from helpful import *


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        raise(NotImplementedError)
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

