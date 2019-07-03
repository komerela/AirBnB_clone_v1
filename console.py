#!/usr/bin/python3
'''This module contains one class, HBNBCommand'''

import cmd
import sys
import models
import json
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNBCommand is a command line
    interpreter for the HBNB project
    """
    prompt = '(hbnb) '
    file = None
    __allowed_classes = ('BaseModel', 'User', 'Amenity',
                         'State', 'Place', 'City', 'Review')

    @staticmethod
    def allowed_classes():
        '''The classes we allow eval() to evaluate upon reload'''
        return HBNBCommand.__allowed_classes

    def from_json_string(json_string):
        '''convert json string of obj dicts into list of same'''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    def do_quit(self, arg):
        """quit the command line
        """
        self.close()
        return True

    def do_EOF(self, arg):
        """exits with a newline
        """
        print()
        self.close()
        return True

    def close(self):
        """closes a file before it's finished execut
        """
        if self.file:
            self.file.close()
            self.file = None

    def emptyline(self):
        '''Do nothing if empty newline'''
        pass

    def do_create(self, arg):
        """create new instance of object and serialize
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.allowed_classes():
            print("** class doesn't exist **")
        else:
            args = arg.split()
            obj = eval(str(args[0]) + '()')
            if not isinstance(obj, BaseModel):
                return
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """print the json string of an object
        """
        args = arg.split()
        if not args or len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.allowed_classes():
            print("** class doesn't exist **")
        elif len(args) < 1:
            print("** instance id missing **")
        id_exists = 0
        for key in models.storage.all().keys():
            classname_then_id = str(key).split('.')
            if len(args) > 1 and args[1] in classname_then_id:
                id_exists = 1
                print(models.storage.objects[(args[0] + "." + args[1])])
        if id_exists == 0:
            print("** no instance found **")

    def do_all(self, line):
        """ method that prints all instances"""
        args = line.split()
        if len(args) < 1:
            list_objects = []
            with open("file.json", mode="r") as f:
                list_of_dicts = HBNBCommand.from_json_string(f.read())
                for each_dict in li0t_of_dicts:
                    list_objects.append(str(each_dict))
                print(list_objects)
        elif line not in HBNBCommand.allowed_classes():
            print("** class doesn't exist **")
        else:
            list_objects = []
            with open("file.json", mode="r") as f:
                list_of_dicts = HBNBCommand.from_json_string(f.read())
                for each_dict in list_of_dicts:
                    list_objects.append(str(each_dict))
                print(list_objects)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
