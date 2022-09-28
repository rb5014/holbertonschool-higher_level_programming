#!/usr/bin/python3
"""_summary_ module that contains the function is_kind_of_class
    """


def is_kind_of_class(obj, a_class):
    """_summary_ returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class ;
    otherwise False

    Args:
        obj (_type_): object to check
        a_class (_type_): specified class to compare with object
    """

    return isinstance(obj, a_class)
