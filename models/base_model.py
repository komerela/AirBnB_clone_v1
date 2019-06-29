#!/usr/bin/env python3
'''
'''
from datetime import datetime
import dateutil.parser
from uuid import uuid4
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
        else:
            self.id = kwargs['id']
            self.created_at = dateutil.parser.parse(kwargs['created_at'])
            self.updated_at = dateutil.parser.parse(kwargs['updated_at'])
    def __str__(self):
        '''
        '''
        return("[BaseModel] ({:s}) {:s}".format(self.id, str(self.__dict__)))
    def save(self):
        '''
        '''
        self.updated_at = datetime.now()
    def to_dict(self):
        '''
        '''
        mydict = self.__dict__
        mydict["__class__"] = "BaseModel"
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["created_at"] = self.created_at.isoformat()
        return mydict




