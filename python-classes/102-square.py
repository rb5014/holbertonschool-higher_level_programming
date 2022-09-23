#!/usr/bin/python3
"""class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
        size must be an integer, otherwise raise a TypeError exception with
         the message size must be an integer
        if size is less than 0, raise a ValueError exception with the message
         size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Square instance can answer to comparators: ==, !=, >, >=, < and <= based
on the square area

You are not allowed to import any module
"""


from functools import total_ordering


@total_ordering
class Square:
    """defines a square by: (based on 3-square.py)"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size**2

    def _is_valid_operand(self, other):
        return hasattr(other, "area")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.area() == other.area()

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.area() < other.area()
