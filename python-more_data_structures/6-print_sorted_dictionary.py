#!/usr/bin/python3
'''function that prints a dictionary by ordered keys.

Prototype: def print_sorted_dictionary(a_dictionary):
You can assume that all keys are strings
Keys should be sorted by alphabetic order
Only sort keys of the first level
(don’t sort keys of a dictionary inside the main dictionary)
Dictionary values can have any type
You are not allowed to import any module'''


def print_sorted_dictionary(a_dictionary):
    sortedList = sorted(a_dictionary.items())
    sortedDict = {}
    for key, value in sortedList:
        sortedDict[key] = value
    for key, value in sortedDict.items():
        print(f'{key}: {value}')
