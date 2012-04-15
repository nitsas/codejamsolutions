#!/usr/bin/env python3.2
"""
Unit Tests for the Magicka problem MagickaWizard class.
for Google Code Jam 2011
Qualification

Link to problem description:
http://code.google.com/codejam/contest/975485/dashboard#s=p1

author: 
Christos Nitsas
(chrisn654)

language:
Python 3.2.1

date:
April, 2012
"""


import unittest
# non-standard modules:
from MagickaWizard import MagickaWizard


class TestMagickaWizard(unittest.TestCase):
    """
    Unit Tests for the Magicka problem MagickaWizard class
    for Google Code Jam 2011
    Qualification
    """
    
    def setUp(self):
        combination_rules = ["ABC", "DEF"]
        opposition_rules = ["AB", "AD"]
        self.wizard = MagickaWizard(combination_rules, opposition_rules)
    
    def test_init(self):
        self.assertEqual(self.wizard.element_list, [])
        d1 = {"AB":"C", "BA":"C", "DE":"F", "ED":"F"}
        self.assertEqual(self.wizard._combination_result, d1)
        d2 = {"A":set(("B", "D")), "B":set("A"), "D":set("A")}
        self.assertEqual(self.wizard._opposites_of, d2)
    
    def test_can_be_combined(self):
        self.assertTrue(self.wizard._can_be_combined("A", "B"))
        self.assertTrue(self.wizard._can_be_combined("B", "A"))
        self.assertTrue(self.wizard._can_be_combined("D", "E"))
        self.assertFalse(self.wizard._can_be_combined("A", "D"))
        self.assertFalse(self.wizard._can_be_combined("X", "Y"))
    
    def test_an_opposite_exists(self):
        self.wizard.element_list = ["D"]
        self.assertTrue(self.wizard._an_opposite_exists("A"))
        self.wizard.element_list = ["A"]
        self.assertTrue(self.wizard._an_opposite_exists("B"))
        self.assertFalse(self.wizard._an_opposite_exists("X"))
    
    def test_invoke_element(self):
        self.wizard.invoke_element("A")
        self.assertEqual(self.wizard.element_list, ["A"])
        self.wizard.invoke_element("B")
        self.assertEqual(self.wizard.element_list, ["C"])
        self.wizard.invoke_element("A")
        self.wizard.invoke_element("X")
        self.wizard.invoke_element("B")
        self.assertEqual(self.wizard.element_list, [])
    
    def test_element_list_as_string(self):
        self.assertEqual(self.wizard.element_list_as_string(), "[]")
        self.wizard.invoke_element("G")
        self.assertEqual(self.wizard.element_list_as_string(), "[G]")
        self.wizard.invoke_elements("HI")
        self.assertEqual(self.wizard.element_list_as_string(), "[G, H, I]")


if __name__ == "__main__":
    unittest.main()

