#!/usr/bin/python3
"""Defines the City class"""
from models.base_model import BaseModel
class City(BaseModel):
    """class for city

    Attributes:
        state_id: The id for the state class
        name: the name of the city
    """
    state_id = ""
    name = ""
