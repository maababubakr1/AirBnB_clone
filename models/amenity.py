#!/usr/bin/python3
"""define amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ amenity class

    Attributes:
        - name (str): name of amenity
    """
    name = ""
