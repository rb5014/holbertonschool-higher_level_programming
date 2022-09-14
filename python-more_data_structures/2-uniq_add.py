#!/usr/bin/python3
'''
Function that adds all unique integers in a list (only once for each integer).

Prototype: def uniq_add(my_list=[]):
You are not allowed to import any module
'''


def uniq_add(my_list=[]):
    uniqList = set(my_list)
    return sum(uniqList)
