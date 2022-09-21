#!/usr/bin/python3
""" Module containing a function print_square
"""


def print_square(size):
    """ print_square - prints a square with the character #
        Parameters:
        @size: lenght of the square
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(int(size)):
        print("#" * int(size))
