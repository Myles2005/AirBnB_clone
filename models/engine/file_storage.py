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
    __file_path = 'data.json'
    __objects = dict()

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialization of __object to Json file """
        odict = FileStorage.__objects.copy()
        with open(FileStorage.__file_path, 'w') as f:
            data = {k: v.to_dict() for k, v in odict.items()}
            json.dump(data, f)

    def reload(self):
        """ Deserialization of Json file to __objects """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                d = json.load(f)
