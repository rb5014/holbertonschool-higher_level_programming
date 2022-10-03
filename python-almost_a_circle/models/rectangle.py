#!/usr/bin/python3
""" module containing the class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """class that inherits from Base, contains 4 private instance attributes:
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instanciation of the Rectangle object

        Args:
            width (_type_): width of the rectangle
            height (_type_): height of the rectangle
            x (int, optional): starting row of the rectangle. Defaults to 0.
            y (int, optional): starting column of the rectangle. Defaults to 0.
            id (_type_, optional): id of the object. Defaults to None.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width getter and setter
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validateAttributes("width", value)
        self.__width = value

    # height getter and setter
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validateAttributes("height", value)
        self.__height = value

    # x getter and setter
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validateAttributes("x", value)
        self.__x = value

    # y getter and setter
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validateAttributes("y", value)
        self.__y = value

    def validateAttributes(self, varname, value):
        """ Validate attributes with different tests
        """
        if type(value) != int:
            raise TypeError(f"{varname} must be an integer")
        if varname in "width height" and value <= 0:
            raise ValueError(f"{varname} must be > 0")
        if varname in "x y" and value < 0:
            raise ValueError(f"{varname} must be >= 0")

    def area(self):
        """returns the area value of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #
        """
        print(('\n' * self.y) +
              (' ' * self.x + '#' * self.width + '\n') *
              self.height, end="")

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for i in kwargs:
                exec("%s = %d" % ("self." + i, kwargs[i]))
