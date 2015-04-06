#!/usr/bin/env python3
"""
Alien Language problem
for Google Code Jam 2009
Qualification Round

Link to problem description:
http://code.google.com/codejam/contest/dashboard?c=90101#s=p0

Author: 
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.2)

Date:
  April, 2012

Usage:
  python3 runme.py input_file
"""


import sys
import re
from itertools import islice
from itertools import product
# non-standard modules:
from helpful import read_list_of_int


# when "import *" from the module, anything not in __all__ will be hidden
__all__ = ['make_list_of_known_words', 'get_list_of_test_cases', 
           'num_words_that_match', 'process_pattern', 'main']


# match a single letter or a group of letters before a parenthesis
_LETTER_OR_POSSIBLE_LETTERS_RE = re.compile(r'(\w+(?=\))|\w)')


def make_list_of_known_words(lines_of_words):
    return [line.rstrip('\n') for line in lines_of_words]


def get_list_of_test_cases(lines_of_test_cases):
    return [line.rstrip('\n') for line in lines_of_test_cases]


def num_words_that_match(pattern, known_words):
    sets_of_possible_letters = process_pattern(pattern)
    num_matches = 0
    for word in known_words:
        for (letter, set_of_letters) in zip(word, sets_of_possible_letters):
            if not letter in set_of_letters:
                # 'word' doesn't match the pattern (don't execute 'else')
                break
        else:
            # every letter in 'word' matches some letter in its corresp. set
            # increase the number of matching words
            num_matches += 1
    return num_matches


def process_pattern(pattern):
    return [set(match.group()) for match in \
            _LETTER_OR_POSSIBLE_LETTERS_RE.finditer(pattern)]


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print('Usage: runme.py input_file')
            return 1
    with open(filename, 'r') as f:
        (word_length, num_known_words, num_test_cases) = read_list_of_int(f)
        known_words = make_list_of_known_words(islice(f, num_known_words))
        test_cases = get_list_of_test_cases(islice(f, num_test_cases))
        for (index, pattern) in enumerate(test_cases):
            print('Case #' + str(index+1) + ': ' + \
                  str(num_words_that_match(pattern, known_words)))
    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
