#!/usr/bin/env python3.2
"""
Magicka problem
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

usage:
$ python3.2 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
# non-standard modules:
from helpful import read_int
from MagickaWizard import MagickaWizard


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        num_cases = read_int(f)
        for i, line in enumerate(f, 1):
            parts = line.split()
            C = int(parts[0])
            combination_rules = parts[1:C+1]
            opposition_rules = parts[C+2:-2]
            elements_to_invoke = parts[-1]
            wizard = MagickaWizard(combination_rules, opposition_rules)
            wizard.invoke_elements(elements_to_invoke)
            print("Case #{0}: {1}".format(i, wizard.element_list_as_string()))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

