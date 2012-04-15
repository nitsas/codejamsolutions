"""
MagickaWizard class for the Magicka problem
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


import collections


class MagickaWizard:
    """
    A Magicka wizard. 
    """
    
    def __init__(self, combination_rules, opposition_rules):
        self.element_list = []
        self._make_combination_result_dict(combination_rules)
        self._make_opposites_of_dict(opposition_rules)
    
    def element_list_as_string(self):
        if not self.element_list:
            return "[]"
        else:
            result = "[" + self.element_list[0]
            for element in self.element_list[1:]:
                result += ", " + element
            result += "]"
            return result
    
    def invoke_elements(self, elements):
        for element in elements:
            self.invoke_element(element)
    
    def invoke_element(self, element):
        if self.element_list and self._can_be_combined(self.element_list[-1], element):
            combination = self.element_list[-1] + element
            self.element_list[-1] = self._combination_result[combination]
        elif self._an_opposite_exists(element):
            self.element_list = []
        else:
            self.element_list.append(element)
    
    def _make_combination_result_dict(self, combination_rules):
        self._combination_result = {}
        for elem1, elem2, result in combination_rules:
            self._combination_result[elem1 + elem2] = result
            self._combination_result[elem2 + elem1] = result
    
    def _make_opposites_of_dict(self, opposition_rules):
        self._opposites_of = collections.defaultdict(set)
        for elem1, elem2 in opposition_rules:
            self._opposites_of[elem1].add(elem2)
            self._opposites_of[elem2].add(elem1)
    
    def _can_be_combined(self, elem1, elem2):
        if elem1 + elem2 in self._combination_result.keys():
            return True
        else:
            return False
    
    def _an_opposite_exists(self, element):
        for opposite in self._opposites_of[element]:
            if opposite in self.element_list:
                return True
        else:
            return False

