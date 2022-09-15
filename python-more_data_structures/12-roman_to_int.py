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
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listD = list(d)
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string):
            if d[roman_string[i + 1]] > d[roman_string[i]]:
                number -= d[roman_string[i]]
                continue
        number += d[roman_string[i]]
    return number
