#!/usr/bin/python3
"""
Unittests for file_storage
"""
import os
import sys
import pep8
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import datetime as dt
import json
from models.engine.file_storage import FileStorage


class Test_File_Storage(unittest.TestCase):
    """
    Test cases
    """

    def test_docstr(self):
        """
        Checks for comments
        """
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_pep8(self):
        """
        Checks for pep8 styling
        """
        style = pep8.StyleGuide(quiet=True)
        pycode = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(pycode.total_errors, 0, "fix pep8")

    def setUp(self):
        """
        Checks User class configurations
        """
        pass

    def tearDown(self):
        """
        Removes JSON file created in storage
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Tests the all method
        """
        fs = FileStorage()
        dict_1 = fs.all()
        self.assertIsNotNone(dict_1)
        self.assertEqual(type(dict_1), dict)
        self.assertIs(dict_1, fs._FileStorage__objects)

    def test_new(self):
        """
        Tests the new method
        """
        fs = FileStorage()
        bm = BaseModel()
        bmc = BaseModel.__class__.__name__
        bmid = bm.id
        dic = fs.all()
        fs.new(bm)

    def test_reload(self):
        """
        Tests the reload method
        """
        new_fs = FileStorage()

        try:
            os.remove("file.json")
        except BaseException:
            pass

        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as f:
            for item in f:
                self.assertEqual(item, "{}")
        self.assertIs(new_fs.reload(), None)
