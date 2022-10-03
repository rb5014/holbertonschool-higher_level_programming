#!/usr/bin/python3
""" module containing the class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor: calls the super class

        Args:
            size (_type_): both width and height will get the value of size
            x (int, optional): position on x axis. Defaults to 0.
            y (int, optional): position on y axis. Defaults to 0.
            id (_type_, optional): id of the object. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns [Square] (<id>) <x>/<y> - <size>
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}")

    # Size of the square
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for i in kwargs:
                exec("%s = %d" % ("self." + i, kwargs[i]))

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
