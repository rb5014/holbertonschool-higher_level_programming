#!/usr/bin/python3
"""test module for the class base
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Class testing the Base class
    """
    def test_id(self):
        # Test with the different possible values of id
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)