#!/usr/bin/python3
" "

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
    """
    """
    __file_path = 'data.json'
    __objects = dict()

    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City, \
            "Place": Place, "Review": Review, "State": State, "User": User}
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
            for k, v in odict.items():
                data = {k: v.to_dict()}
            json.dump(data, f)

    def reload(self):
        """ Deserialization of Json file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for k, v in data.items():
                    FileStorage.__object[k] = classes[v["__class__"]](**v)
        except FileNotFoundError:
            pass
