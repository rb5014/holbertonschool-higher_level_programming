#!/usr/bin/python3
"""_summary_ module that contains a function
    """


def add_attribute(obj, attr, val):
    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__')\
            and not hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
