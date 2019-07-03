#!/usr/bin/python3
"""
    Place class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class that inherits from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''print all objects attributes
        '''
        return("[Place] ({:s}) {:s}".format(self.id, str(self.__dict__)))

    def to_dict(self):
        '''return dictionary of object's attributes'''
        mydict = self.__dict__.copy()
        mydict["__class__"] = "Place"
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["created_at"] = self.created_at.isoformat()

        return mydict
