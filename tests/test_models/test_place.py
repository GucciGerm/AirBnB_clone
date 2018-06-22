#!/usr/bin/python3
"""
Unittests for place Module


"""
import unittest
import os
import pep8
import datetime
from models.place import Place
from models.base_model import BaseModel


class Test_Place(unittest.TestCase):
    """
    Tests for place
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

    def test_has_class_attrs(self):
        p = Place()
        self.assertTrue("city_id" in dir(p))
        self.assertTrue("user_id" in dir(p))
        self.assertTrue("name" in dir(p))
        self.assertTrue("description" in dir(p))
        self.assertTrue("number_rooms" in dir(p))
        self.assertTrue("number_bathrooms" in dir(p))
        self.assertTrue("max_guest" in dir(p))
        self.assertTrue("price_by_night" in dir(p))
        self.assertTrue("latitude" in dir(p))
        self.assertTrue("longitude" in dir(p))
        self.assertTrue("amenity_ids" in dir(p))

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


if __name__ == "__main__":
    unittest.main()
