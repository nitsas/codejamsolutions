#!/usr/bin/env python3
"""
Bot Trust problem
for Google Code Jam 2011
Qualification

Link to problem description:
http://code.google.com/codejam/contest/975485/dashboard#s=p0

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


import re
import sys
# non-standard modules:
from helpful import read_int


def time_to_push(sequence_of_buttons):
    time = 0
    blue_position, blue_time = 1, time
    orange_position, orange_time = 1, time
    for button in sequence_of_buttons:
        robot, button_num = button[0], int(button[2:])
        if robot == "B":
            time = max(blue_time + time_to_move_and_push(blue_position, button_num), orange_time + 1)
            blue_position, blue_time = button_num, time
        else:
            time = max(orange_time + time_to_move_and_push(orange_position, button_num), blue_time + 1)
            orange_position, orange_time = button_num, time
    return time


def time_to_move_and_push(current_position, target_button):
    return abs(target_button - current_position) + 1


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        num_cases = read_int(f)
        split_line_re = re.compile(r"^\d+ |[BO] \d+")
        for i, line in enumerate(f, 1):
            sequence_of_buttons = split_line_re.findall(line)[1:]
            print("Case #{0}: {1}".format(i, time_to_push(sequence_of_buttons)))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

