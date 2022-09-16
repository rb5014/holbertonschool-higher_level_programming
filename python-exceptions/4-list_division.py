#!/usr/bin/python3
'''Function that divides element by element 2 lists.

Prototype: def list_division(my_list_1, my_list_2, list_length):
my_list_1 and my_list_2 can contain any type (integer, string, etc.)
list_length can be bigger than the length of both lists
Returns a new list (length = list_length) with all divisions
If 2 elements can’t be divided, the division result should be equal to 0
If an element is not an integer or float:
print: wrong type
If the division can’t be done (/0):
print: division by 0
If my_list_1 or my_list_2 is too short
print: out of range
You have to use try: / except: / finally:
You are not allowed to import any module'''


def list_division(my_list_1, my_list_2, list_length):
    resList = [0] * list_length
    i = 0
    while i < list_length:
        try:
            resList[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            resList[i] = 0
            print("division by zero")
        except TypeError:
            resList[i] = 0
            print("wrong type")
        except IndexError:
            resList[i] = 0
            print("out of range")
        finally:
            i += 1
    return resList
