#!/usr/bin/python3
'''
'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''
    '''
    __objects = {}
    __file_path = 'file.json'

    def file_path(self):
        return FileStorage.__file_path

    def all(self):
        '''
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        '''
        FileStorage.__objects['{}.{}'.format(obj.__class__.__name__,
                              obj.id)] = obj

    def reload(self):
        pass
        '''
        '''
        try:
            with open(FileStorage._FileStorage__file_path, "r") as f:
                list_of_dicts = FileStorage.from_json_string(f.read())
        except FileNotFoundError:
            list_of_dicts = []
        for each in list_of_dicts:
            # use eval to make this flexible
            print('TYPE OF EACH DICT', type(each))
            BaseModel(**each)

    def from_json_string(json_string):
        '''convert json string of obj dicts into list of same'''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
