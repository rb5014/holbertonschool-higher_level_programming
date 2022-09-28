#!/usr/bin/python3
"""_summary_ module that contains the class BaseGeometry
    """


class BaseGeometry:
    """  (based on 6-base_geometry.py).
    """
    def area(self):
        """ raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value:
            name is always a string
            if value is not an integer: raise a TypeError exception, with the
             message <name> must be an integer
            if value is less or equal to 0: raise a ValueError exception with
             the message <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("name must be greater than 0")
