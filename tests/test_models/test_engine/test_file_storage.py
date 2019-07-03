#!/usr/bin/python3
"""
    unittest for file storage
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import os


class Test_file_storage_class(unittest.TestCase):
    """ Unittest for File Storage"""
    a = BaseModel()
    b = BaseModel()
    c = BaseModel()

    def test_methods_exist(self):
        """ test that methods exist in file storage class"""
        self.assertTrue(models.storage.all)
        self.assertTrue(models.storage.save)
        self.assertTrue(models.storage.new)
        self.assertTrue(models.storage.reload)
