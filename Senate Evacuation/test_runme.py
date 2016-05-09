#!/usr/bin/env python3
"""
Unit Tests for the Senate Evacuation problem
for Google Code Jam 2016
Round 1C

Link to problem description:
https://code.google.com/codejam/contest/4314486/dashboard#s=p0

Author:
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.4)

Date:
  May, 2016

Usage:
  python3 test_runme.py
"""


import io
import os
import sys
import unittest
# modules I've written:
import runme


def are_extra_samples_present():
    return os.path.isfile('extra_sample.in') and os.path.isfile('extra_sample.out')


def contents_of(output_file):
    with open(output_file, 'r', encoding='utf-8') as f:
        return f.read()


def output_of_runme_on(input_file):
    # call runme.main and get its output into from_main
    with io.StringIO() as target_output_stream:
        # redirect stdout to an io.StringIO object to run main
        sys.stdout, old_stdout = target_output_stream, sys.stdout
        runme.main(input_file)
        from_main = target_output_stream.getvalue()
        # get original stdout back
        sys.stdout = old_stdout
    return from_main


class TestRunme(unittest.TestCase):
    """
    Simple tests for the Senate Evacuation problem
    for Google Code Jam 2016
    Round 1C
    """
    # define if needed
    # def setUp(self):
    #     pass
    #
    # define if needed
    # def tearDown(self):
    #     pass
    #
    # def test_something(self):
    #     # use self.assertEqual(), self.assertTrue() or self.assertRaises()
    #     pass
    #
    def test_main_on_sample_in(self):
        input_file, output_file = 'sample.in', 'sample.out'
        # compare runme.main's results with sample.out's contents
        self.assertEqual(output_of_runme_on(input_file),
                         contents_of(output_file))
    
    @unittest.skipIf(not are_extra_samples_present(), 'no extra samples')
    def test_main_on_extra_sample_in(self):
        input_file, output_file = 'extra_sample.in', 'extra_sample.out'
        # compare runme.main's results with extra_sample.out's contents
        self.assertEqual(output_of_runme_on(input_file),
                         contents_of(output_file))


if __name__ == '__main__':
    unittest.main()
