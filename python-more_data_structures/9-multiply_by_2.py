#!/usr/bin/python3
'''Function that returns a new dictionary with all values multiplied by 2

Prototype: def multiply_by_2(a_dictionary):
You can assume that all values are only integers
Returns a new dictionary
You are not allowed to import any module'''


def multiply_by_2(a_dictionary):
    newDict = {key: a_dictionary[key]*2 for key in a_dictionary}
    return newDict
