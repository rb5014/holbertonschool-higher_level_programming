#!/usr/bin/python3
"""module containing the function class_to_json
"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of an object

    Args:
        obj (_type_): instance of the class
    All attributes of the obj Class are serializable:
    list, dictionary, string, integer and boolean
    """
    return obj.__dict__
