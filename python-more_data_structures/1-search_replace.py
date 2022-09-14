#!/usr/bin/python3
'''
Write a function that replaces all occurrences of an element by another
in a new list.

Prototype: def search_replace(my_list, search, replace):
my_list is the initial list
search is the element to replace in the list
replace is the new element
You are not allowed to import any module
'''


def search_replace(my_list, search, replace):
    newList = list(map(lambda x: str(x).replace(str(search), str(replace)),
                       my_list))
    return newList
