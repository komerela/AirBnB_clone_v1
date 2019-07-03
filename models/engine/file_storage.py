#!/usr/bin/python3
'''This module contains one class, FileStorage
'''
import datetime
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    '''FileStorage reloads and initializes objects from json
    '''
    __objects = {}
    __file_path = 'file.json'
    __allowed_classes = ('BaseModel', 'User', 'Amenity',
                         'State', 'Place', 'City', 'Review')

    @staticmethod
    def allowed_classes():
        '''The classes we allow eval() to evaluate upon reload'''
        return FileStorage.__allowed_classes

    def file_path(self):
        '''The path of the json file being loaded'''
        return FileStorage.__file_path

    def all(self):
        '''Return dict of all objects
        '''
        return FileStorage.__objects

    def save(self):
        '''dummy method'''
        self.updated_at = datetime.datetime.utcnow()
        list_of_dicts = [obj.to_dict() for (key, obj) in
                         FileStorage.__objects.items()]
        with open(FileStorage.__file_path, "w+", encoding="utf-8") as f:
            f.write(json.dumps(list_of_dicts))

    def new(self, obj):
        '''insert new objects into dict of all objects
        '''
        FileStorage.__objects['{}.{}'.format(obj.__class__.__name__,
                              obj.id)] = obj

    def reload(self):
        '''reload objects from a json file
        '''
        try:
            with open(FileStorage.__file_path, "r") as f:
                list_of_dicts = FileStorage.from_json_string(f.read())
        except FileNotFoundError:
            list_of_dicts = []
        for each in list_of_dicts:

            # use eval to make this flexible
            BaseModel(each)
        for each_dict in list_of_dicts:
            # use eval to make this flexible
            if each_dict['__class__'] in FileStorage.allowed_classes():
                class_name = each_dict['__class__']
                executable = '{}(**{})'.format(class_name, each_dict)
                eval(executable)

    def from_json_string(json_string):
        '''convert json string of obj dicts into list of same'''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
