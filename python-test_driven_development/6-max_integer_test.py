#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        # test when list is empty
        emptyList = []
        self.assertEqual(max_integer(emptyList), None, "ça marche ?")


if __name__ == '__main__':
    unittest.main()
