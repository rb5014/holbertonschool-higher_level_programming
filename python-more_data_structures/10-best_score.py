#!/usr/bin/python3
'''Function that returns a key with the biggest integer value.

Prototype: def best_score(a_dictionary):
You can assume that all values are only integers
If no score found, return None
You can assume all students have a different score
You are not allowed to import any module'''


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sortedValues = sorted(list(a_dictionary.values()))
    bestScore = sortedValues[-1]
    for key, value in a_dictionary.items():
        if bestScore == value:
            return key
