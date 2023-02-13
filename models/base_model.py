#!/usr/bin/python3
"""BaseModel class object of the AirBnB clone"""

import models
from uuid import uuid4
from datetime import datetime
import json
from imp import reload

class BaseModel:
    """Classs method which all files inherits from."""
    def __init__(self, *args, **kwargs):
        """Initialisation of Base model public instance attributes.
        Args:
            *args - Unused
            **kwargs - Takes a dictionary
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        "Print out: [<class name>] (<self.id>) <self.__dict__>"
        cls_name = type(self).__name__
        return("[{}] ({}) {}".format(cls_name, self.id, self.__dict__))

    def save(self):
        " returns a dictionary containing all keys/values of __dict__"
        self.update_at = datetime.today().isoformat()
        models.storage.save()

    def to_dict(self):
        "returns a dictionary containing all keys/values of __dict__"
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
