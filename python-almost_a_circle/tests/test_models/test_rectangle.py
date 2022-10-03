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

        r2 = Rectangle(1, 2, 3)
        self.assertIsInstance(r2, Rectangle)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r3, Rectangle)

        r4 = Rectangle("1", 2)
        self.assertIsInstance(r4, Rectangle)

        r5 = Rectangle(1, "2")
        self.assertIsInstance(r5, Rectangle)

        r6 = Rectangle(1, 2, "3")
        self.assertIsInstance(r6, Rectangle)

        r7 = Rectangle(1, 2, 3, "4")
        self.assertIsInstance(r7, Rectangle)

        r8 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r8, Rectangle)

        r9 = Rectangle(-1, 2)
        self.assertIsInstance(r9, Rectangle)

        r10 = Rectangle(1, -2)
        self.assertIsInstance(r10, Rectangle)

        r11 = Rectangle(0, 2)
        self.assertIsInstance(r11, Rectangle)

        r12 = Rectangle(1, 0)
        self.assertIsInstance(r12, Rectangle)

        r13 = Rectangle(1, 2, -3)
        self.assertIsInstance(r13, Rectangle)

        r14 = Rectangle(1, 2, 3, -4)
        self.assertIsInstance(r14, Rectangle)
