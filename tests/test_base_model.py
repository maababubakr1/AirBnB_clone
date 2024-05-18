#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel
    """

    def setUp(self):
        """Set up for all tests"""
        self.model = BaseModel()

    def test_id(self):
        """Test that id is unique and is a valid uuid"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)
        self.assertIsInstance(uuid.UUID(self.model.id), uuid.UUID)

    def test_created_at(self):
        """Test that created_at is a datetime object
                and is the current datetime"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test that updated_at is a datetime object
                and is the same as created_at upon creation"""
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_str(self):
        """Test the string representation of the BaseModel instance"""
        string = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), string)

    def test_save(self):
        """Test that save updates updated_at with the current datetime"""
        old_updated_at = self.model.updated_at
        time.sleep(1)
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(self.model.__class__.__name__,
                         model_dict['__class__'])
        self.assertEqual(self.model.id, model_dict['id'])
        self.assertEqual(self.model.created_at.isoformat(),
                         model_dict['created_at'])
        self.assertEqual(self.model.updated_at.isoformat(),
                         model_dict['updated_at'])
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_kwargs_initialization(self):
        """Test initialization with kwargs"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertEqual(self.model.__str__(), new_model.__str__())


if __name__ == '__main__':
    unittest.main()
