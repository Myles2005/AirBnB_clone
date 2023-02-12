#!/usr/bin/python3
"""Defines the User"""
from models.base_model import BaseModel

class User(BaseModel):
    """Represents a User
    Attributes:
        email: email of the user
        password: Password of the user
        first_name: First name of the user
        last_name: Last name of the user
    """
    email = ""
    password= ""
    first_name = ""
    last_name = ""
