#!/usr/bin/python3
""" Defines a basemodel for other classes"""
from models import storage
import uuid
from datetime import datetime


class BaseModel():
    """ A class that defines all common attributes/methods for other classes

    Attributes:
        - id (str): unique id for each instance.
        - created_at (datetime): the datetime when an instance is created.
        - updated_at (datetime): the datetime when an instance is updated
    """

    def __init__(self, *args, **kwargs):
        """ Initialize a new instances of basemodel

        Args:
        - *args (tuple): unused
        - **kwargs (dict): key/value piars of attributes
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Return string implementation of basemodel"""
        cls_name = type(self).__name__
        str_rep = "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
        return (str_rep)

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing
            all keys/values of __dict__ of the instance

        a key __class__ must be added to this dictionary
            with the class name of the object
        created_at and updated_at must be
            converted to string object in ISO format

        Return:
            - dictionary containing all keys/values of __dict__ of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
