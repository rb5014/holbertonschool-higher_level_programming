#!/usr/bin/python3
"""_summary_ module that contains the function is_same_class
    """


def is_same_class(obj, a_class):
    """_summary_ returns True if the object is exactly an instance of
    the specified class ; otherwise False.

    Args:
        obj (_type_): object to check
        a_class (_type_): specified class to compare with object
    """

    return type(obj) is a_class
