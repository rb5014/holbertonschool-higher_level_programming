#!/usr/bin/python3
"""class Square that defines a square by: (based on 5-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the
 message size must be an integer
if size is less than 0, raise a ValueError exception with the message size
 must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a TypeError
 exception with the message position must be a tuple of 2 positive integers
Instantiation with optional size and optional position:
def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square
with the character #:
if size is equal to 0, print an empty line
position should be use by using space - Don’t fill lines by spaces when
 position[1] > 0
"""


class Square:
    """defines a square by: (based on 5-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__private

    @position.setter
    def position(self, value):
        for n in value:
            if len(value) != 2 or type(n) != int or n < 0:
                raise TypeError("position must be a tuple of 2 " +
                                "positive integers")
        self.__private = value

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.size > 0:
            for p1 in range(self.position[1]):
                print()
            for i in range(self.size):
                for p0 in range(self.position[0]):
                    print(' ', end='')
                for j in range(self.size):
                    print('#', end='')
                print()
        else:
            print()
