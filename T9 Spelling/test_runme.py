#!/usr/bin/env python3.2
"""
Unit Tests for the T9 Spelling problem 
for Google Code Jam Africa 2010
Qualification

Link to problem description:
http://code.google.com/codejam/contest/351101/dashboard#s=p2

author: 
Christos Nitsas
(chrisn654)

language:
Python 3.2.1

date:
April, 2012

usage:
$ python3.2 test_runme.py
or
$ test_runme.py
"""


import io
import sys
import unittest
# non-standard modules:
import runme


class TestRunme(unittest.TestCase):
    """
    Unit Tests for the T9 Spelling problem 
    for Google Code Jam Africa 2010
    Qualification
    """
    
    def setUp(self):
        # use two characters on the same key, a capital, a foreign 
        # letter and a number as characters
        characters = "abDμ6 "
        t9_phrases = ["2", "22", "3", "555", "6", "0"]
        self.translator = runme.T9Translator(characters, t9_phrases)
    
    def test_T9Translator_initialization(self):
        characters = "abDμ6 "
        t9_phrases = ["2", "22", "3", "555", "6", "0"]
        character_to_t9 = dict(zip(characters, t9_phrases))
        self.assertEqual(self.translator.characters, characters)
        self.assertEqual(self.translator.t9_phrases, t9_phrases)
        self.assertEqual(self.translator.character_to_t9, character_to_t9)
    
    def test_T9Translator_toT9(self):
        self.assertEqual(self.translator.toT9("abD6 "), "2 22360")
        self.assertEqual(self.translator.toT9("μa "), "55520")

    def test_main_on_sample_in(self):
        # call runme.main and get it's output into from_main
        with io.StringIO() as target_output_stream:
            # redirect stdout to an io.StringIO object to run main
            sys.stdout, old_stdout = target_output_stream, sys.stdout
            runme.main("sample.in")
            from_main = target_output_stream.getvalue()
            # get original stdout back
            sys.stdout = old_stdout
        # get the "sample.out" file's contents
        with open("sample.out", "r") as sample_out:
            from_sample_out = sample_out.read()
        # compare runme.main's results with sample.out's contents
        self.assertEqual(from_main, from_sample_out)


if __name__ == "__main__":
    unittest.main()

