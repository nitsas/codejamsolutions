#!/usr/bin/env python3
"""
Hall of Mirrors problem
for Google Code Jam 2012
Qualification

Link to problem description:
http://code.google.com/codejam/contest/1460488/dashboard#s=p3

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
import HallOfMirrors


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
            height, width, max_distance = read_list_of_int(f)
            hall = HallOfMirrors.read_hall(f, height)
            hall.emit_light_from_source_and_propagate(max_distance)
            print("Case #{0}: {1}".format(i, hall.number_of_reflections))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

