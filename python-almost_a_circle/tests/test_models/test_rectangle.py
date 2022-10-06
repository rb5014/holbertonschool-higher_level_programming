#!/usr/bin/python3
"""test module for the class Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Class testing the Rectangle class
    """
    def test_rectangle_regular(self):
        # Test of width and height with Rectangle(1, 2)
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

        # Test of x with Rectangle(1, 2, 3)
        r = Rectangle(1, 2, 3)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.x, 3)

        # Test of y with Rectangle(1, 2, 3, 4)
        r = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.y, 4)

        #  Test of id with Rectangle(1, 2, 3, 4, 5)
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 5)

    def test_rectangle_bad_type(self):
        # Test of bad width type with Rectangle("1", 2)
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle("1", 2))

        # Test of bad height type with Rectangle(1, "2")
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle(1, "2"))

        # Test of bad x type with Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle(1, 2, "3"))

        # Test of bad y type with Rectangle(1, 2, 3, "4")
        with self.assertRaises(TypeError):
            self.assertIsNone(Rectangle(1, 2, 3, "4"))

    def test_rectangle_bad_values(self):
        # Test of negative width value with Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(-1, 2))

        # Test of negative height value withRectangle(1, -2)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, -2))

        # Test of 0 width value with Rectangle(0, 2)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(0, 2))

        # Test of 0 height value withRectangle(1, 0)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, 0))

        # Test of bad x value with Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, 2, -3))

        # Test of bad y value with Rectangle(1, 2, 3, -4)
        with self.assertRaises(ValueError):
            self.assertIsNone(Rectangle(1, 2, 3, -4))

    def test_area(self):
        # Test of area()
        self.assertEqual(Rectangle(2, 2).area(), 4)

    def test_str(self):
        # Test of __str__
        self.assertEqual(str(Rectangle(2, 3, 5, 0, 80)),
                         "[Rectangle] (80) 5/0 - 2/3")

    def test_display(self):
        # Import libraries to access stdout and store the string
        # input-output stream
        from io import StringIO
        import sys
        # Keep stdout in temporary variable to reset sys.stdout at the end
        tmp = sys.stdout
        # Capture the stdout stream into s
        stream = StringIO()
        # 'Connect' stdout to the new stream
        sys.stdout = stream
        # Test of display() without x and y
        Rectangle(3, 2).display()
        self.assertEqual(stream.getvalue(), "###\n###\n")
        # Reset stream value
        stream = StringIO()
        sys.stdout = stream

        # Test of display() without y exists
        Rectangle(3, 2, 2).display()
        self.assertEqual(stream.getvalue(), "  ###\n  ###\n")
        # Reset stdout back to normal(tmp)
        sys.stdout = tmp

    def test_to_dictionary(self):
        # Test of to_dictionary() in Rectangle
        self.assertEqual(Rectangle(17, 2, 0, 0, 19).to_dictionary(),
                         {'x': 0, 'y': 0, 'id': 19, 'height': 2, 'width': 17})

    def test_update(self):
        # Test of update() in Rectangle
        r = Rectangle(1, 2)
        s = str(r)
        r.update()
        s2 = str(r)
        self.assertEqual(s, s2)

        # Test of *args:
        # Test of id update(89) in Rectangle
        r.update(89)
        self.assertEqual(r.id, 89)

        # Test of width update(89, 1) in Rectangle
        r.update(89, 1)
        self.assertEqual(r.width, 1)

        # Test of height update(89, 1, 2) in Rectangle
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

        # Test of x update(89, 1, 2, 3) in Rectangle
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

        # Test of y update(89, 1, 2, 3, 4) in Rectangle
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

        # Test of **kwargs:
        # Test of update(**{'id': 89}) in Rectangle
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

        # Test of update(**{'id': 89, 'width': 1}) in Rectangle
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

        # Test of update(**{'id': 89, 'width': 1, 'height': 2}) in Rectangle
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

        # Test of update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        # in Rectangle
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

        # Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3,
        # 'y': 4 }) in Rectangle
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create(self):
        # Test of Rectangle.create(**{'id': 89}) in Rectangle
        r = Rectangle.create(**{'id': 89})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 89)

        # Test of Rectangle.create(**{'id': 89, 'width': 1}) in Rectangle
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 1)

        # Test of Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        # in Rectangle
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.height, 2)

        # Test of Rectangle.create(**{'id': 89, 'width': 1, 'height': 2,
        # 'x': 3}) in Rectangle
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.x, 3)

        # Test of Rectangle.create(**{'id': 89, 'width': 1, 'height': 2,
        # 'x': 3, 'y': 4}) in Rectangle
        r = Rectangle.create(**{'id': 89, 'width': 1,
                                'height': 2, 'x': 3, 'y': 4})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.y, 4)

    def test_save_to_file(self):
        from os.path import exists
        # Test of Rectangle.save_to_file(None) in Rectangle
        Rectangle.save_to_file(None)
        self.assertTrue(exists("Rectangle.json"))
        with open("Rectangle.json", 'r', encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

        # Test of Rectangle.save_to_file([]) in Rectangle
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r', encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

        # Test of Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 98)])
        with open("Rectangle.json", 'r', encoding="utf-8") as f:
            self.assertEqual(f.read(),
                             "[{\"x\": 0, \"y\": 0, "
                             "\"id\": 98, \"height\": 2, "
                             "\"width\": 1}]")

    def test_load_from_file(self):
        from os.path import exists
        # Test of Rectangle.load_from_file() when file doesn’t exist
        aList = []
        aList = Rectangle.load_from_file()
        self.assertTrue(exists("Rectangle.json"))

        # Test of Rectangle.load_from_file() when file exists
        r1 = Rectangle(3, 8)
        Rectangle.save_to_file([r1])
        aList = Rectangle.load_from_file()
        self.assertTrue(type(aList) == list)
