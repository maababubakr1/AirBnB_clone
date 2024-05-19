#!/usr/bin/python3
"""define User class"""
from models.base_model import BaseModel


class State(BaseModel):
    """ state class

    Attribute:
    - name (str): name of state
    """
    name = ""
