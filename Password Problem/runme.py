#!/usr/bin/env python3
"""
Password Problem problem
for Google Code Jam 2012
Round 1A

Link to problem description:
http://code.google.com/codejam/contest/1645485/dashboard#s=p0

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
from helpful import read_int, read_list_of_int, read_list_of_float


def expected_num_keystrokes(a, b, p):
    prob_first_k_ok = make_prob_first_k_ok(a, p)
    expected = 3 * b
    expected = min(expected, expected_keep_typing(a, b, prob_first_k_ok))
    expected = min(expected, expected_press_enter(a, b, prob_first_k_ok))
    for n in range(1, int((a + 1) / 2) + 1):
        expected = min(expected, expected_delete_n(a, b, prob_first_k_ok, n))
    return expected


def make_prob_first_k_ok(a, probability_typed_correctly):
    """
    The list:
    [P_{1}, P_{2}, ..., P_{k}, ..., P_{a + 1}]
    where P_{k} is the probability that the first k characters are ok (they 
    were typed correctly).
    """
    result = [1.0]
    for i in range(a):
        result.append(result[-1] * probability_typed_correctly[i])
    return result


def expected_keep_typing(a, b, prob_first_k_correct):
    expected_keystrokes = prob_first_k_correct[a] * (b - a + 1)
    expected_keystrokes += (1 - prob_first_k_correct[a]) * (2 * b - a + 2)
    return expected_keystrokes


def expected_press_enter(a, b, p):
    return b + 2


def expected_delete_n(a, b, prob_first_k_correct, n):
    expected_keystrokes = prob_first_k_correct[a - n] * (2 * n + b - a + 1)
    expected_keystrokes += (1 - prob_first_k_correct[a - n]) * (2 * n + 2 * b - a + 2)
    return expected_keystrokes


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
            A, B = read_list_of_int(f)
            P = read_list_of_float(f)
            print("Case #{0}: {1}".format(i, expected_num_keystrokes(A, B, P)))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

