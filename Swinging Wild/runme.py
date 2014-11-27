#!/usr/bin/env python3
"""
Swinging Wild problem
for Google Code Jam 2012
Round 2

Link to problem description:
http://code.google.com/codejam/contest/1842485/dashboard#s=p0

Author: 
  Christos Nitsas
  (nitsas)
  (chrisnitsas)

Language:
  Python 3(.2)

Date:
  May, 2012

Usage:
  python3 runme.py sample.in
"""


import sys
# modules I've written:
from helpful import read_int, read_list_of_int


def make_list_of_vines(f, N):
    return [read_list_of_int(f) for i in range(N)]


def is_target_reachable(pos, reach, next_vines, D, results=dict()):
    if pos + reach >= D:
        return 'YES'
    reachable_vines = []
    for i, vine in enumerate(next_vines):
        if vine[0] > pos + reach:
            break
        else:
            reachable_vines.append(i)
    for i in reversed(reachable_vines):
        vine = next_vines[i]
        new_pos = vine[0]
        new_reach = min(new_pos - pos, vine[1])
        if (new_pos, new_reach) in results:
            is_reachable = results[(new_pos, new_reach)]
        else:
            is_reachable = is_target_reachable(new_pos, new_reach, \
                                               next_vines[i+1:], D, results)
        if is_reachable is 'YES':
            return 'YES'
    return 'NO'


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print('Usage: runme.py input_file')
            return 1
    with open(filename, 'r') as f:
        T = read_int(f)
        for i in range(1, T + 1):
            N = read_int(f)
            vines = make_list_of_vines(f, N)
            D = read_int(f)
            pos = vines[0][0]
            reach = min(vines[0][0], vines[0][1])
            print('Case #{0}: {1}'.format(i, is_target_reachable(pos, reach, \
                                                               vines[1:], D)))
    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
