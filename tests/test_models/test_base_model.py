#!/usr/bin/python3
"""
Test for base model.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel"""

    def test_model(self):
        m1 = BaseModel()
        m2 = BaseModel()
        self.assertIsInstance(m1, BaseModel)
        self.assertIsInstance(m2, BaseModel)

    def test_id(self):
        m1 = BaseModel()
        m2 = BaseModel()
        self.assertIsInstance(m1.id, str)
        self.assertIsInstance(m2.id, str)
        self.assertNotEqual(m1.id, m2.id)

    def test_save(self):
        m1 = BaseModel()

        m1.save()
        self.assertNotEqual(m1.created_at, m1.updated_at)

    def test_to_dict(self):
        m1 = BaseModel()

        my_dict = m1.to_dict()

        self.assertEqual(my_dict['__class__'], "BaseModel")
        self.assertTrue(isinstance(my_dict['created_at'], str))
        self.assertTrue(isinstance(my_dict['updated_at'], str))


if __name__ == "__man__":
    unittest.main()
