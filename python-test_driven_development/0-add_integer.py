#!/usr/bin/python3
"""_summary_ module containing a function add_integer
"""


def add_integer(a, b=98):
    """ function that adds 2 integers"""
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
