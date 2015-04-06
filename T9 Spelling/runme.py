#!/usr/bin/env python3
"""
T9 Spelling problem
for Google Code Jam Africa 2010
Qualification

Link to problem description:
http://code.google.com/codejam/contest/351101/dashboard#s=p2

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
from helpful import read_int


class T9Translator:
    """
    Translates strings of lowercase characters a-z and space 
    characters to T9 strings.
    """

    def __init__(self, characters=None, t9_phrases=None):
        if characters is not None:
            self.characters = characters
        else:
            self.characters = "abcdefghijklmnopqrstuvwxyz "
        if t9_phrases is not None:
            self.t9_phrases = t9_phrases
        else:
            self.t9_phrases = ["2", "22", "222", "3", "33", "333", "4", "44", 
                               "444", "5", "55", "555", "6", "66", "666", "7", 
                               "77", "777", "7777", "8", "88", "888", "9", 
                               "99", "999", "9999", "0"]
        self.character_to_t9 = dict(zip(self.characters, self.t9_phrases))
    
    def toT9(self, string):
        result = self.character_to_t9[string[0]]
        for letter in string[1:]:
            # check if we're going to have to press the same key again
            if result[-1] != self.character_to_t9[letter][0]:
                # add the new letter's t9 translation to result
                result += self.character_to_t9[letter]
            else:
                # we must pause (insert a space) before the next keypress
                result += " " + self.character_to_t9[letter]
        return result


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        num_cases = read_int(f)
        translator = T9Translator()
        for i, line in enumerate(f, 1):
            print("Case #" + str(i) + ": " + translator.toT9(line.rstrip("\n")))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

