#!/usr/bin/python3
""" Defines the place class """
from models.base_model import BaseModel

class Place(BaseModel):
    """Represents place
    Attributes:
        city_id: id number of city
        user_id: id number of user
        name: Name of Place
        description: description of the place
        number_rooms: The Number of rooms of the place
        numebr_bathrooms: The Number of bathrooms of the place
        max_guest: Maximum number of guests to occupy the place
        price_by_night: Price of accomodation per night
        latitude: Latitude of the place
        longitude: Longitude of the place
        amenity_ids: List of ids of amenities
    """
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
