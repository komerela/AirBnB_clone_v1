#!/usr/bin/python3
"""
    test for user class
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class Test_Place_class(unittest.TestCase):
    """ test cases for the place class"""
    a = Place()
    b = Place()
    c = Place()

    def test_unique_id(self):
        """ test to confirm that the id's are unique"""
        self.assertFalse(self.a.id is self.b.id)
        self.assertFalse(self.a.id is self.c.id)
        self.assertFalse(self.b.id is self.c.id)

    def test_Place_creation(self):
        """ Test to confirm creation of instance"""
        self.assertTrue(isinstance(self.b, Place))
        self.assertTrue(type(self.b) is Place)

    def test_Place_inheritance(self):
        """ Test to confirm inheritance"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_Place_attributes(self):
        """ test Place attributes"""
        self.assertTrue(type(self.a.city_id) is str)
        self.assertTrue(type(self.a.user_id) is str)
        self.assertTrue(type(self.a.name) is str)
        self.assertTrue(type(self.a.description) is str)
        self.assertTrue(type(self.a.number_rooms) is int)
        self.assertTrue(type(self.a.number_bathrooms) is int)
        self.assertTrue(type(self.a.max_guest) is int)
        self.assertTrue(type(self.a.price_by_night) is int)
        self.assertTrue(type(self.a.latitude) is float)
        self.assertTrue(type(self.a.longitude) is float)
        self.assertTrue(type(self.a.amenity_ids) is list)
