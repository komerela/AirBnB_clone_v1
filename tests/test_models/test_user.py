#!/usr/bin/python3
"""
    test for user class
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class Test_User_class(unittest.TestCase):
    """ test cases for the user class"""
    a = User()
    b = User()
    c = User()

    def test_unique_id(self):
        """ test to confirm that the id's are unique"""
        self.assertFalse(self.a.id is self.b.id)
        self.assertFalse(self.a.id is self.c.id)
        self.assertFalse(self.b.id is self.c.id)

    def test_User_creation(self):
        """ Test to confirm creation of instance"""
        self.assertTrue(isinstance(self.b, User))
        self.assertTrue(type(self.b) is User)

    def test_User_inheritance(self):
        """ Test to confirm inheritance"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_User_attributes(self):
        """ test user attributes"""
        self.assertTrue(type(self.a.email) is str)
        self.assertTrue(type(self.b.password) is str)
        self.assertTrue(type(self.c.first_name) is str)
        self.assertTrue(type(self.a.last_name) is str)
