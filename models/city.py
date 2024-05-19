#!/usr/bin/python3
"""define city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ city class

    Attributes:
        - name (str): name of city
        - state_id (str): ID of state where the city is located
    """
    name = ""
    state_id = ""
