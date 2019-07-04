#!/usr/bin/python3
"""
    test for user class
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class Test_Review_class(unittest.TestCase):
    """ test cases for the review class"""
    a = Review()
    b = Review()
    c = Review()

    def test_unique_id(self):
        """ test to confirm that the id's are unique"""
        self.assertFalse(self.a.id is self.b.id)
        self.assertFalse(self.a.id is self.c.id)
        self.assertFalse(self.b.id is self.c.id)

    def test_Review_creation(self):
        """ Test to confirm creation of instance"""
        self.assertTrue(isinstance(self.b, Review))
        self.assertTrue(type(self.b) is Review)

    def test_Review_inheritance(self):
        """ Test to confirm inheritance"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_attributes(self):
        """ test review attributes"""
        self.assertTrue(type(self.a.place_id) is str)
        self.assertTrue(type(self.b.user_id) is str)
        self.assertTrue(type(self.c.text) is str)
