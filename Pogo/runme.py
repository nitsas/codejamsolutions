#!/usr/bin/env python3
"""
Pogo problem
for Google Code Jam 2013
Round 1C

Link to problem description:
https://code.google.com/codejam/contest/2437488/dashboard#s=p1

author: 
Chris Nitsas
(nitsas)

language:
Python 3.3.2

date:
May, 2012

usage:
$ python3 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
import math
import operator
# non-standard modules:
from helpful import read_int, read_list_of_int, is_odd, is_even


def hops_to_get_to_x_y(x, y):
    hop_directions_string = hops_to_get_to_non_negative_x_y(abs(x), abs(y))
    if x < 0:
        hop_directions_string = hop_directions_string.translate(str.maketrans('WE', 'EW'))
    if y < 0:
        hop_directions_string = hop_directions_string.translate(str.maketrans('NS', 'SN'))
    return hop_directions_string


def hops_to_get_to_non_negative_x_y(x, y):
    # 
    # first calculate the minimum number of hops needed
    # 
    min_number_of_hops = math.ceil((-1 + math.sqrt(1 + 8 * (x + y))) / 2)
    s = sum(range(1, min_number_of_hops + 1))
    assert(s >= (x + y))
    overshot = s - x - y
    # we want the overshot to be even
    if is_odd(overshot):
        if is_odd(min_number_of_hops + 1):
            s += min_number_of_hops + 1
            overshot += min_number_of_hops + 1
            min_number_of_hops += 1
        else:
            s += (min_number_of_hops + 1) + (min_number_of_hops + 2)
            overshot += (min_number_of_hops + 1) + (min_number_of_hops + 2)
            min_number_of_hops += 2
    assert(s == sum(range(1, min_number_of_hops + 1)))
    assert(s >= (x + y))
    assert(overshot == s - x - y)
    assert(is_even(overshot))
    # 
    # then manage each hop's simplified direction (i.e. positive or 
    # negative hop) so that we move exactly x + y squares
    # 
    hop_value = list(range(1, min_number_of_hops + 1))
    hop_simplified_direction = [1] * min_number_of_hops
    assert(s == sum(map(operator.mul, hop_simplified_direction, hop_value)))
    largest_positive_hop = hop_value[-1]
    while overshot > 0:
        assert(overshot % 2 == 0)
        if overshot > 2 * largest_positive_hop:
            hop_to_change_simplified_direction = largest_positive_hop
            largest_positive_hop -= 1
            assert(largest_positive_hop > 0)
        else:
            hop_to_change_simplified_direction = int(overshot / 2)
        hop_simplified_direction[hop_to_change_simplified_direction - 1] = -1
        s -= 2 * hop_to_change_simplified_direction
        overshot -= 2 * hop_to_change_simplified_direction
    assert(overshot == 0)
    assert(s == (x + y) == sum(map(operator.mul, hop_value,
                                   hop_simplified_direction)))
    # 
    # now assign a true direction (i.e. North, East, South or West) to each hop
    # (we'll make all negative hops in the same direction)
    # 
    hop_direction = [None] * min_number_of_hops
    cur_x, cur_y = 0, 0
    negative_hops = [-h for h in map(operator.mul, hop_simplified_direction, hop_value) if h < 0]
    if x > y:
        for nh in negative_hops:
            hop_direction[nh - 1] = 'W'
            cur_x -= nh
    else:
        for nh in negative_hops:
            hop_direction[nh - 1] = 'S'
            cur_y -= nh
    available_hops = [h for h in map(operator.mul, hop_simplified_direction, hop_value) if h >= 0]
    if (x - cur_x >= y - cur_y):
        while (x > cur_x) and (x - cur_x >= available_hops[-1]):
            if (x - cur_x - available_hops[-1] == 2) and (2 not in available_hops):
                assert(available_hops[-2] > 3)
                hop_direction[available_hops[-2] - 1] = 'E'
                cur_x += available_hops[-2]
                available_hops.remove(available_hops[-2])
            elif (x - cur_x - available_hops[-1] == 1) and (1 not in available_hops):
                assert(available_hops[-2] > 2)
                hop_direction[available_hops[-2] - 1] = 'E'
                cur_x += available_hops[-2]
                available_hops.remove(available_hops[-2])
            else:
                hop_direction[available_hops[-1] - 1] = 'E'
                cur_x += available_hops[-1]
                available_hops = available_hops[:-1]
        if x > cur_x:
            try:
                available_hops.remove(x - cur_x)
                hop_direction[x - cur_x - 1] = 'E'
            except ValueError:
                available_hops.remove(x - cur_x - 1)
                hop_direction[x - cur_x - 2] = 'E'
                available_hops.remove(1)
                hop_direction[0] = 'E'
            cur_x = x
        for ah in available_hops:
            hop_direction[ah - 1] = 'N'
            cur_y += ah
        assert(cur_y == y)
    else:
        while (y > cur_y) and (y - cur_y >= available_hops[-1]):
            if (y - cur_y - available_hops[-1] == 2) and (2 not in available_hops):
                assert(available_hops[-2] > 3)
                hop_direction[available_hops[-2] - 1] = 'N'
                cur_y += available_hops[-2]
                available_hops.remove(available_hops[-2])
            elif (y - cur_y - available_hops[-1] == 1) and (1 not in available_hops):
                assert(available_hops[-2] > 2)
                hop_direction[available_hops[-2] - 1] = 'N'
                cur_y += available_hops[-2]
                available_hops.remove(available_hops[-2])
            else:
                hop_direction[available_hops[-1] - 1] = 'N'
                cur_y += available_hops[-1]
                available_hops = available_hops[:-1]
        if y > cur_y:
            try:
                available_hops.remove(y - cur_y)
                hop_direction[y - cur_y - 1] = 'N'
            except ValueError:
                available_hops.remove(y - cur_y - 1)
                hop_direction[y - cur_y - 2] = 'N'
                available_hops.remove(1)
                hop_direction[0] = 'N'
            cur_y = y
        for ah in available_hops:
            hop_direction[ah - 1] = 'E'
            cur_x += ah
        assert(cur_x == x)
    assert(not (None in hop_direction))
    return ''.join(hop_direction)


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
            x, y = read_list_of_int(f)
            print("Case #{0}:".format(i), end=" ")
            print(hops_to_get_to_x_y(x, y))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

