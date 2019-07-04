#!/usr/bin/python3
"""
    test for user class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity_class(unittest.TestCase):
    """ test cases for the amenity class"""
    a = Amenity()
    b = Amenity()
    c = Amenity()

    def test_unique_id(self):
        """ test to confirm that the id's are unique"""
        self.assertFalse(self.a.id is self.b.id)
        self.assertFalse(self.a.id is self.c.id)
        self.assertFalse(self.b.id is self.c.id)

    def test_Amenity_creation(self):
        """ Test to confirm creation of instance"""
        self.assertTrue(isinstance(self.b, Amenity))
        self.assertTrue(type(self.b) is Amenity)

    def test_Amenity_inheritance(self):
        """ Test to confirm inheritance"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_Amenity_attributes(self):
        """ test for amenity attributes"""
        self.assertTrue(type(self.a.name) is str)
