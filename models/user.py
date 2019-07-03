#!/usr/bin/python3
"""
    User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __str__(self):
        '''print all objects attributes
        '''
        return("[User] ({:s}) {:s}".format(self.id, str(self.__dict__)))
    def to_dict(self):
        '''return dictionary of object's attributes'''
        mydict = self.__dict__.copy()
        mydict["__class__"] = "User"
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["created_at"] = self.created_at.isoformat()

        return mydict
