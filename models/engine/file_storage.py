#!/usr/bin/python3
"Module for FileStorage class"


import os
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Representation of FileStorage
    Attributes:
        __file_path: The name of the file to save objects to.
        __objects: A dictionary of instantiated objects.
    """
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialization of __object to Json file """
        odict = FileStorage.__objects
        data = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """ Deserialization of Json file to __objects """
        try:
            with open(FileStorage.__file_path) as f:
                data = json.load(f)
                for o in data.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
