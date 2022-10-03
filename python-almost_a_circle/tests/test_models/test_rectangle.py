#!/usr/bin/python3
"""test module for the class Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Class testing the Rectangle class
    """
    def test_rectangle_exists(self):
        # Test with the different possible values of the args in
        # rectangle object
        r1 = Rectangle(1, 2)
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(1, 2, 3)
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle("1", 2)
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(1, "2")
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(1, 2, "3")
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(1, 2, 3, "4")
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(-1, 2)
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(1, -2)
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(0, 2)
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(1, 0)
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(1, 2, -3)
        self.assertIsInstance(r1, Rectangle)

        r1 = Rectangle(1, 2, 3, -4)
        self.assertIsInstance(r1, Rectangle)
