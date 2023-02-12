#!/usr/bin/python3
"""Defines review"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represents the review of place
    Attributes:
        place_id: id of the place
        user_id: id of user
        text: The review message
    """
    place_id = ""
    user_id = ""
    text = ""
