#!/usr/bin/python3
"""test module for the class base
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Class testing the Base class
    """
    def test_id(self):
        # Test of Base() for assigning automatically an ID
        b1 = Base()
        self.assertEqual(b1.id, 1)
        # Test of Base() for assigning automatically an ID + 1 of
        # the previous
        b2 = Base()
        self.assertEqual(b2.id, 2)
        # Test of Base(12) saving the ID passed
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_to_json_string(self):
        # Test of Base.to_json_string(None)
        self.assertEqual(Base.to_json_string(None), "[]")
        # Test of Base.to_json_string([])
        self.assertEqual(Base.to_json_string([]), "[]")
        # Test of Base.to_json_string([{'id': 12}])
        self.assertEqual(Base.to_json_string([{"id": 12}]), "[{\"id\": 12}]")
        # Test of Base.to_json_string([{'id': 12}]) returning a string
        s = Base.to_json_string([{'id': 12}])
        self.assertEqual(s, "[{\"id\": 12}]")

    def test_from_json_string(self):
        # Test of Base.from_json_string(None)
        self.assertEqual(Base.from_json_string(None), [])
        # Test of Base.from_json_string(None)
        self.assertEqual(Base.from_json_string("[]"), [])
        # Test of Base.from_json_string(None)
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])
        # Test of Base.from_json_string(None)
        Listofdict = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(Listofdict, [{'id': 89}])
