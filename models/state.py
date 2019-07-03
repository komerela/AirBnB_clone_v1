#!/usr/bin/python3
"""
    State class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """ State class that inherits from BaseModel"""
    name = ""

    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''print all objects attributes
        '''
        return("[State] ({:s}) {:s}".format(self.id, str(self.__dict__)))

    def to_dict(self):
        '''return dictionary of object's attributes'''
        mydict = self.__dict__.copy()
        mydict["__class__"] = "State"
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["created_at"] = self.created_at.isoformat()

        return mydict
