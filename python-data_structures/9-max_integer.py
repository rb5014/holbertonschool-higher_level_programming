#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_int = my_list[0]
    for val in my_list:
        if val > max_int:
            max_int = val
    return max_int
