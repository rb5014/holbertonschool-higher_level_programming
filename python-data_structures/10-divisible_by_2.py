#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    true_or_false = my_list.copy()
    for i in range(0, len(my_list)):
        true_or_false[i] = True if my_list[i] % 2 == 0 else False
    return true_or_false
