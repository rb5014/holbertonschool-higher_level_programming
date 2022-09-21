#!/usr/bin/python3
"""_summary_ module containing a function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>"""
    if not first_name:
        first_name = ""
    elif type(first_name) != str:
        raise TypeError("first_name must be a string")
    if not last_name:
        last_name = ""
    elif last_name and type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
