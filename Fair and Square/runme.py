#!/usr/bin/env python3
"""
Fair and Square problem
for Google Code Jam 2013
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/2270488/dashboard#s=p2

author: 
Chris Nitsas
(nitsas)

language:
Python 3.2.3

date:
May, 2012

usage:
$ python3 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
import itertools
from math import sqrt, ceil, floor, log10
# non-standard modules:
from helpful import read_int, read_list_of_int


def count_digits_of(num):
    return len(str(num))


def count_fair_and_square_numbers_in_interval(low, high):
    count = 0
    # make all palindromes whose squares will be in the range [low, high]
    for num in generate_palindromes_in_interval(ceil(sqrt(low)), 
                                                floor(sqrt(high))):
        if is_palindrome(num**2):
            count += 1
    return count


def generate_fair_and_square_numbers_in_interval(low, high):
    for num in generate_palindromes_in_interval(ceil(sqrt(low)), 
                                                floor(sqrt(high))):
        if is_palindrome(num**2):
            yield num**2


def generate_palindromes_in_interval(low, high):
    num_digits_low = count_digits_of(low)
    num_digits_high = count_digits_of(high)
    # first make all palindromes with num_digits_low digits
    for palindrome in generate_palindromes_with_n_digits(num_digits_low):
        # we have to check that it's higher than "low"
        if palindrome > high:
            raise(StopIteration)
        elif palindrome >= low:
            yield palindrome
    # then make all palindromes with more than num_digits_low and 
    # less num_digits_high digits
    for n in range(num_digits_low + 1, num_digits_high):
        yield from generate_palindromes_with_n_digits(n)
    # last, make all palindromes with num_digits_high digits
    if not num_digits_low == num_digits_high:
        for palindrome in generate_palindromes_with_n_digits(num_digits_high):
            # we have to stop as soon as we pass "high"
            if palindrome > high:
                raise(StopIteration)
            else:
                yield palindrome

def generate_palindromes_with_n_digits(n):
    if n == 0:
        raise(StopIteration)
    elif n == 1:
        yield from range(1, 10)
    elif n % 2 == 0:
        for first_half in range(10 ** (floor(n/2) - 1), 10 ** floor(n/2)):
            yield int(str(first_half) + str(first_half)[::-1])
    else:
        for first_part in range(10 ** (floor(n/2) - 1), 10 ** floor(n/2)):
            for middle in range(10):
                yield int(str(first_part) + str(middle) + str(first_part)[::-1])


def is_palindrome(num):
    s = str(num)
    for i in range(floor(len(s)/2)):
        if s[i] != s[-i-1]:
            return False
    return True


def is_palindrome_alt(num):
    # alternate way
    s = str(num)
    if s[:floor(len(s)/2)] == s[-floor(len(s)/2):][::-1]:
        return True
    else:
        return False


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
            low, high = read_list_of_int(f)
            print("Case #{0}:".format(i), end=" ")
            print(count_fair_and_square_numbers_in_interval(low, high))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

