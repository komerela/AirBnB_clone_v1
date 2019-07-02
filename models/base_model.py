#!/usr/bin/python3
'''This module contains one class, BaseModel
'''
from datetime import datetime
import json
import models
from uuid import uuid4


class BaseModel:
    '''BaseModel handles serialization/deserialization
    '''
    def __init__(self, *args, **kwargs):
        '''Initialize object with kwargs if present
        '''
        if kwargs:
            for (key, value) in kwargs.items():
                if key == '__class__':
                    continue
                elif key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'id':
                    self.id = value
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        '''print all objects attributes
        '''
        return("[BaseModel] ({:s}) {:s}".format(self.id, str(self.__dict__)))

    def save(self):
        '''save all objects into json file
        '''
        self.updated_at = datetime.utcnow()
        list_of_dicts = [obj.to_dict() for (key, obj) in
                         models.storage.all().items()]
        with open(models.storage.file_path(), "w+", encoding="utf-8") as f:
            f.write(json.dumps(list_of_dicts))

    def to_dict(self):
        '''return dictionary of object's attributes
        '''
        mydict = self.__dict__.copy()
        mydict["__class__"] = "BaseModel"
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["created_at"] = self.created_at.isoformat()
        return mydict
