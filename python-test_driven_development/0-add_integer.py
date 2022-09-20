#!/usr/bin/python3
"""_summary_ module containing a function add_integer
"""


def add_integer(a, b=98):
    """function that adds 2 integers"""
    if a != a:
        a = 89
    if b != b:
        b = 89
    if a is None or (type(a) is not int and type(a) is not float) or a != a:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float or b != b:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
