#!/usr/bin/python3
"""_summary_ module that contains the class Rectangle
    """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """   inherits from Rectangle (9-rectangle.py)
    """

    def __init__(self, size):
        """
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
        """
        self.__size = size
        self.integer_validator("width", self.__size)

    def area(self):
        """ raises an Exception with the message area() is not implemented
        """
        return self.__size ** 2

    def integer_validator(self, name, value):
        """ validates value:
            name is always a string
            if value is not an integer: raise a TypeError exception, with the
             message <name> must be an integer
            if value is less or equal to 0: raise a ValueError exception with
             the message <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
