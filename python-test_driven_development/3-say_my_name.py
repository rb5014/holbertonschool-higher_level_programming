#!/usr/bin/python3
""" Module containing a function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """ say_my_name - prints "My name is <first name> <last name>"
        Parameters:
        @first_name: the first name to print
        @last_name: the last name to print
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
