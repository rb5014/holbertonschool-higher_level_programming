#!/usr/bin/python3
"""test module for the class Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Class testing the Rectangle class
    """
    def test_rectangle_regular(self):
        # Test of Rectangle(1, 2)
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 1)
        # Test of Rectangle(1, 2, 3)
        self.assertIsInstance(Rectangle(1, 2, 3), Rectangle)
        # Test of Rectangle(1, 2, 3, 4)
        self.assertIsInstance(Rectangle(1, 2, 3, 4), Rectangle)
        #  Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(Rectangle(1, 2, 3, 4, 5), Rectangle)

    def test_rectangle_bad_type(self):
        # Test of Rectangle("1", 2)
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle("1", 2))
        # Test of Rectangle(1, "2")
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle(1, "2"))
        # Test of Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle(1, 2, "3"))
        # Test of Rectangle(1, 2, 3, "4")
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle(1, 2, 3, "4"))

    def test_rectangle_bad_values(self):
        # Test of Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(-1, 2))
        # Test of Rectangle(1, -2)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, -2))
        # Test of Rectangle(0, 2)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(0, 2))
        # Test of Rectangle(1, 0)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, 0))
        # Test of Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, 2, -3))
        # Test of Rectangle(1, 2, 3, -4)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, 2, 3, -4))
