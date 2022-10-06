#!/usr/bin/python3
"""test module for the class Square
"""
import unittest
from models.square import Square


class TestRectangleClass(unittest.TestCase):
    """Class testing the Square class
    """
    def test_square_regular(self):

        # Test of size with Square(1)
        sq = Square(1)
        self.assertIsInstance(sq, Square)
        self.assertEqual(sq.size, 1)

        # Test of x with Square(1, 2)
        sq = Square(1, 2)
        self.assertIsInstance(sq, Square)
        self.assertEqual(sq.x, 2)

        # Test of y with Square(1, 2, 3)
        sq = Square(1, 2, 3)
        self.assertIsInstance(sq, Square)
        self.assertEqual(sq.y, 3)

        # Test of id with Square(1, 2, 3, 4)
        sq = Square(1, 2, 3, 4)
        self.assertIsInstance(sq, Square)
        self.assertEqual(sq.id, 4)

    def test_square_bad_type(self):
        # Test of bad size type with Square("1")
        with self.assertRaises(TypeError):
            self.assertIsNone(Square("1"))

        # Test of bad x type with Square(1, "2")
        with self.assertRaises(TypeError):
            self.assertIsNone(Square(1, "2"))

        # Test of bad y type with Square(1, 2, "3")
        with self.assertRaises(TypeError):
            self.assertIsNone(Square(1, 2, "3"))

    def test_square_bad_values(self):
        # Test of negative size value with Square(-1)
        with self.assertRaises(ValueError):
            self.assertIsNone(Square(-1))

        # Test of 0 size value with Square(0)
        with self.assertRaises(ValueError):
            self.assertIsNone(Square(0))

        # Test of bad x value with Square(1, -2)
        with self.assertRaises(ValueError):
            self.assertIsNone(Square(1, -2))

        # Test of bad y value with Square(1, 2, -3)
        with self.assertRaises(ValueError):
            self.assertIsNone(Square(1, 2, -3))

    def test_str(self):
        # Test of __str__
        self.assertEqual(str(Square(2, 5, 0, 80)),
                         "[Square] (80) 5/0 - 2")

    def test_to_dictionary(self):
        # Test of to_dictionary() in Square
        self.assertEqual(Square(2, 0, 2, 17).to_dictionary(),
                         {'id': 17, 'x': 0, 'size': 2, 'y': 2})

    def test_update(self):
        # Test of update() in Square
        sq = Square(1, 2)
        s = str(sq)
        sq.update()
        s2 = str(sq)
        self.assertEqual(s, s2)

        # Test of *args:
        # Test of id update(89) in Square
        sq.update(89)
        self.assertEqual(sq.id, 89)

        # Test of width update(89, 1) in Square
        sq.update(89, 1)
        self.assertEqual(sq.size, 1)

        # Test of x update(89, 1, 2, 3) in Square
        sq.update(89, 1, 2)
        self.assertEqual(sq.x, 2)

        # Test of y update(89, 1, 2, 3, 4) in Square
        sq.update(89, 1, 2, 3)
        self.assertEqual(sq.y, 3)

        # Test of **kwargs:
        # Test of update(**{'id': 89}) in Square
        sq.update(**{'id': 89})
        self.assertEqual(sq.id, 89)

        # Test of update(**{'id': 89, 'size': 1}) in Square
        sq.update(**{'id': 89, 'size': 1})
        self.assertEqual(sq.size, 1)

        # Test of update(**{'id': 89, 'size': 1, 'x': 2})
        # in Square
        sq.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(sq.x, 2)

        # Test of update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3}) in Square
        sq.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(sq.y, 3)

    def test_create(self):
        # Test of Square.create(**{'id': 89}) in Square
        r = Square.create(**{'id': 89})
        self.assertIsInstance(r, Square)
        self.assertEqual(r.id, 89)

        # Test of Square.create(**{'id': 89, 'size': 1}) in Square
        r = Square.create(**{'id': 89, 'size': 1})
        self.assertIsInstance(r, Square)
        self.assertEqual(r.size, 1)

        # Test of Square.create(**{'id': 89, 'size': 1, 'x': 2}) in Square
        r = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertIsInstance(r, Square)
        self.assertEqual(r.x, 2)

        # Test of Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        # in Square
        r = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertIsInstance(r, Square)
        self.assertEqual(r.y, 3)

    def test_save_to_file_None(self):
        from os.path import exists
        # Test of Square.save_to_file(None) in Square
        Square.save_to_file(None)
        self.assertTrue(exists("Square.json"))
        with open("Square.json", 'r', encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        # Test of Square.save_to_file([]) in Square
        Square.save_to_file([])
        with open("Square.json", 'r', encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_regular(self):
        # Test of Square.save_to_file([Square(1, 2)]) in Square
        Square.save_to_file([Square(1, 2, 0, 98)])
        with open("Square.json", 'r', encoding="utf-8") as f:
            self.assertEqual(f.read(), '[{"id": 98, "x": 2, '
                             '"size": 1, "y": 0}]')

    def test_load_from_file(self):
        from os.path import exists
        # Test of Square.load_from_file() when file doesn’t exist
        aList = []
        aList = Square.load_from_file()
        self.assertTrue(exists("Square.json"))

        # Test of Square.load_from_file() when file exists
        sq1 = Square(3, 8)
        Square.save_to_file([sq1])
        aList = Square.load_from_file()
        self.assertTrue(type(aList) == list)
