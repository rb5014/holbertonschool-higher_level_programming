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
        self.assertIsInstance(Rectangle(1, 2), Rectangle)
        self.assertIsInstance(Rectangle(1, 2, 3), Rectangle)
        self.assertIsInstance(Rectangle(1, 2, 3, 4), Rectangle)
        self.assertIsInstance(Rectangle(1, 2, 3, 4, 5), Rectangle)
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle("1", 2))
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle(1, "2"))
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle(1, 2, "3"))
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle(1, 2, 3, "4"))
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(-1, 2))
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, -2))
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(0, 2))
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, 0))
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, 2, -3))
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, 2, 3, -4))
