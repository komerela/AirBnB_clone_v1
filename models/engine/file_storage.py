#!/usr/bin/env python3
'''
'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''
    '''
    __objects = {}
    __file_path = 'file.json'
    @property
    def file_path(self):
        return FileStorage.__file_path
    def all(self):
        '''
        '''
        return FileStorage.__objects
    def new(self, obj):
        '''
        '''
        FileStorage.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj
    def reload(self):
        pass
        '''
        '''
        try:
            with open(self.file_path, "r") as f:
                list_of_dicts = json.load(f)
        except FileNotFoundError:
            list_of_dicts = []
        for each in list_of_dicts:
        # use eval to make this flexible
            BaseModel(each)
