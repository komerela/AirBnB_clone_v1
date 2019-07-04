#!/usr/bin/python3
"""
    test for user class
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class Test_City_class(unittest.TestCase):
    """ test cases for the city class"""
    a = City()
    b = City()
    c = City()

    def test_unique_id(self):
        """ test to confirm that the id's are unique"""
        self.assertFalse(self.a.id is self.b.id)
        self.assertFalse(self.a.id is self.c.id)
        self.assertFalse(self.b.id is self.c.id)

    def test_City_creation(self):
        """ Test to confirm creation of instance"""
        self.assertTrue(isinstance(self.b, City))
        self.assertTrue(type(self.b) is City)

    def test_City_inheritance(self):
        """ Test to confirm inheritance"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_City_attributes(self):
        """ test city attributes"""
        self.assertTrue(type(self.a.state_id) is str)
        self.assertTrue(type(self.b.name) is str)
