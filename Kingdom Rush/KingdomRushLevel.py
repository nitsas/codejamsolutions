"""
KingdomRushLevel class for the Kingdom Rush problem
for Google Code Jam 2012
Round 1A

Link to problem description:
http://code.google.com/codejam/contest/1645485/dashboard#s=p1

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


class KingdomRushLevel:
    """
    A simple class representing a Kingdom Rush level.
    """
    
    def __init__(self, one_star_req, two_stars_req):
        """
        Set the required number of stars to complete the level with a one 
        star rating (one_star_req) and with a two star rating (two_star_req) 
        and initialize the current rating.
        """
        # required stars to complete level with a one star rating
        self.one_star_req = one_star_req
        # required stars to complete level with a two stars rating
        self.two_stars_req = two_stars_req
        # current rating (0 if the level has not been completed)
        self.rating = 0
    
    def completed(self, on_rating=2):
        """
        Completed the level with a "on_rating" rating.
        """
        self.rating = on_rating

