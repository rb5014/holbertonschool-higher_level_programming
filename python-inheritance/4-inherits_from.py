#!/usr/bin/python3
"""_summary_ module that contains the function inherits_from
    """


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ;
    otherwise False

    Args:
        obj (_type_): obj to check
        a_class (_type_): class to compare with object
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
