#!/usr/bin/python3
"""
Test for file storage.
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """To test the all() instance method"""

        all_objs = self.storage.all()

        self.assertEqual(type(all_objs), dict)
        self.assertIs(all_objs, self.storage._FileStorage__objects)

    def test_new(self):
        """To test the new() instance method"""

        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        self.storage.new(obj)
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        """To test the save and reload method"""

        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(key, new_storage.all())


if __name__ == "__main__":
    unittest.man()
