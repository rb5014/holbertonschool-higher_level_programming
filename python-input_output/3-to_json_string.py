#!/usr/bin/python3
import json
"""module containing a function to_json_string
"""


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string):
    """
    return json.dumps(my_obj)
