#!/usr/bin/python3
"""
Unittests for city Module


"""
import unittest
import os
import pep8
import datetime
from models.city import City
from models.base_model import BaseModel


class Test_City(unittest.TestCase):
    """
    Tests for City
    """

    def test_docstring(self):
        """
        Checks for docstring
        """
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_pep8_basemodel(self):
        """
        tests pep8
        """
        style = pep8.StyleGuide(quiet=True)
        pycode = style.check_files(['models/base_model.py'])
        self.assertEqual(pycode.total_errors, 0, "fix pep8")

    @classmethod
    def setUp(self):
        """
        Setup Test
        """
        pass

    @classmethod
    def tearDown(self):
        """
        Removes JSON file
        """
        pass

    def test_has_class_attrs(self):
        c = City()
        self.assertTrue("name" in dir(c))

if __name__ == "__main__":
    unittest.main()
