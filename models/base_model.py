#!/usr/bin/env python3
'''
'''
from datetime import datetime
import dateutil.parser
import json
import models
from uuid import uuid4


class BaseModel:
    '''
    '''
    def __init__(self, *args, **kwargs):
        '''
        '''
        if kwargs:
            print('UPDATING FROM DICT---------------------------------------------')
            for (key, value) in kwargs.items():
                if key in ('updated_at', 'created_at'):
                    self.key = dateutil.parser.parse(value)
                elif key == '__class__':
                    continue
                else:
                    self.key = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            models.storage.new(self)
    def save(self):
        models.storage.save()
    def __str__(self):
        '''
        '''
        return("[BaseModel] ({:s}) {:s}".format(self.id, str(self.__dict__)))
    def save(self):
        '''
        '''
        self.updated_at = datetime.utcnow()
        list_of_dicts = [obj.to_dict() for (key, obj) in models.storage.all().items()]
        print(type(list_of_dicts))
        with open(models.storage.file_path, "w+", encoding="utf-8") as f:
            f.write(json.dumps(list_of_dicts))
    def to_dict(self):
        '''
        '''
        mydict = self.__dict__.copy()
        mydict["__class__"] = "BaseModel"
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["created_at"] = self.created_at.isoformat()
        return mydict
