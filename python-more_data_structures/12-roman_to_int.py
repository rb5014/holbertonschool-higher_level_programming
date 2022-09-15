#!/usr/bin/python3
'''Create a function def roman_to_int(roman_string): that converts a Roman
numeral to an integer.

You can assume the number will be between 1 to 3999.
def roman_to_int(roman_string) must return an integer
If the roman_string is not a string or None, return 0'''


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    number = 0
    convDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                'M': 1000}
    for i in range(roman_string):
        if roman_string[i] == convDict[roman_string[i + 1]]:
            number -= convDict[roman_string[i]]
        else:
            number += convDict[roman_string[i]]
    return number
