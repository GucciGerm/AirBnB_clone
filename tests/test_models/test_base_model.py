#!/usr/bin/python3
"""
Unittests for BaseModel


"""
import unittest
import os
import pep8
import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """
    Tests for BaseModel
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

    def test_init_arg(self):
        """
        Checks arg instance
        """
        new_base = BaseModel(8)
        self.assertEqual(type(new_base).__name__, "BaseModel")
        self.assertFalse(hasattr(new_base, "8"))

    def test_init_kwarg(self):
        """
        Checks kwarg instance
        """
        new_base = BaseModel(name="Betty")
        self.assertEqual(type(new_base).__name__, "BaseModel")
        self.assertTrue(hasattr(new_base, "name"))
        self.assertTrue(hasattr(new_base, "__class__"))
        self.assertFalse(hasattr(new_base, "id"))
        self.assertFalse(hasattr(new_base, "created_at"))
        self.assertFalse(hasattr(new_base, "updated_at"))


if __name__ == "__main__":
    unittest.main()
