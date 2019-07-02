#!/usr/bin/python3
"""
    Unittest for Base class
"""
import unittest
from models.base_model import BaseModel
class Test_base_model_class(unittest.TestCase):
    """ Unittest for Base class"""
    b = BaseModel()
    a = BaseModel()
    c = BaseModel()
    def test_unique_id(self):
        """ test to confirm that the id's are unique"""
        self.assertFalse(self.a.id is self.b.id)
        self.assertFalse(self.a.id is self.c.id)
        self.assertFalse(self.b.id is self.c.id)
    def test_Base_Model_Creation(self):
        """ Test to confirm instance of Base class"""
        self.assertTrue(isinstance(self.b, BaseModel))
        self.assertTrue(type(self.b) is BaseModel)
    def test_id_is_string(self):
        """ Test to make sure uuid.uuid4() was
            converted to string
        """
        self.assertTrue(type(self.b.id) is str)
    def test_to_dict(self):
        """ test that to_dict produces a string"""
        self.assertTrue(type(self.b.to_dict()) is dict)
    def test_save(self):
        """ test to make sure the time/date are
            being changed
        """
        self.b.save()
        self.assertNotEqual(self.b.created_at,
                            self.b.updated_at)
