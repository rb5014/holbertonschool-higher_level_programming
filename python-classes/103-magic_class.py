#!/usr/bin/python3
"""module that contains the class MagicClass
"""
import math


class MagicClass:
    """MagicClass

    Args:
        radius (_type_): radius of the circle
    """
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
