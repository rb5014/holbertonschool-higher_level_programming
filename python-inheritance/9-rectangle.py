#!/usr/bin/python3
"""_summary_ module that contains the class BaseGeometry
    """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """  (based on 7-base_geometry.py).
    """

    def __init__(self, width, height):
        """
        width and height must be private. No getter or setter
        width and height must be positive integers, validated
         by integer_validator
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """ raises an Exception with the message area() is not implemented
        """
        return self.__height * self.__width

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
        return f"[Rectangle] {self.__width}/{self.__height}"
