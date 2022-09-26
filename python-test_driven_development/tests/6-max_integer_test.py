#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_Empty_List(self):
        # test for an empty list
        testList = []
        self.assertEqual(max_integer(testList), None, "Empty_List test failed")

    def test_1_Elem(self):
        # test for a list of 1 element
        testList = [1]
        self.assertEqual(max_integer(testList), 1, "\'1_Elem\' test failed")

    def test_All_Neg(self):
        # test for a list of 1 element
        testList = [-1, -2, -10, -6]
        self.assertEqual(max_integer(testList), -1, "\'All_Neg\' test failed")

    def test_1_Neg(self):
        # test for a list of 1 element
        testList = [-5, 10]
        self.assertEqual(max_integer(testList), 10, "\'1_Neg\' test failed")

    def test_Max_Middle(self):
        # test for a list of 1 element
        testList = [1, 6, 2]
        self.assertEqual(max_integer(testList), 6, "\'Max_Middle\' failed")

    def test_Max_Beginning(self):
        # test for a list of 1 element
        testList = [7, 4, 2]
        self.assertEqual(max_integer(testList), 7, "\'Max_Beginning\' failed")

    def test_Max_End(self):
        # test for a list of 1 element
        testList = [1, 5, 53]
        self.assertEqual(max_integer(testList), 53, "\'Max_End\' failed")

