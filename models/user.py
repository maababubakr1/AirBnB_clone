#!/usr/bin/python3
"""define User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    create user objects

    Attributes:
    - email (str): user email
    - password (str): user password
    - first_name (str): first name of the user
    - last_name (str): last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
