#!/usr/bin/env python3.2
"""
Unit Tests for the Swinging Wild problem 
for Google Code Jam 2012
Round 2

Link to problem description:
http://code.google.com/codejam/contest/1842485/dashboard#s=p0

author: 
Christos Nitsas
(chrisn654)

language:
Python 3.2.1

date:
May, 2012

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
    Unit Tests for the Swinging Wild problem 
    for Google Code Jam 2012
    Round 2
    """
    
    # define if needed
    #def setUp(self):
    #    pass
    
    # define if needed
    #def tearDown(self):
    #    pass
    
    #def test_something(self):
    #    # use self.assertEqual(), self.assertTrue() or self.assertRaises()
    #    pass
    
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

