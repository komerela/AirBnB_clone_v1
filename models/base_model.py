#!/usr/bin/env python3
'''
'''
from datetime import datetime
import dateutil.parser
from uuid import uuid4
import models
import json


class BaseModel:
    '''
    '''
    def __init__(self, *args, **kwargs):
        '''
        '''
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            self.id = kwargs['id']
            self.created_at = dateutil.parser.parse(kwargs['created_at'])
            self.updated_at = dateutil.parser.parse(kwargs['updated_at'])
    def save(self):
        models.storage.save()
    def __str__(self):
        '''
        '''
        return("[BaseModel] ({:s}) {:s}".format(self.id, str(self.__dict__)))
    def save(self):
        '''
        '''
        objects_dict = {}
        for (key, obj) in models.storage.all().items():
            objects_dict[key] = obj.to_dict()
        with open(models.storage.file_path, "w", encoding="utf-8") as f:
            json.dump(objects_dict, f)
        self.updated_at = datetime.now()
    def to_dict(self):
        '''
        '''
        mydict = self.__dict__.copy()
        mydict["__class__"] = "BaseModel"
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["created_at"] = self.created_at.isoformat()
        return mydict
