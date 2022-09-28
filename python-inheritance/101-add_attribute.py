#!/usr/bin/python3
"""_summary_ module that contains a function
    """


def add_attribute(obj, attr, val):
    """_summary_

    Args:
        obj (_type_): an object to check
        attr (_type_): the attribute to add
        val (_type_): value to dd in attribute
"""
    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    elif not hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
