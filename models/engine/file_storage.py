#!/usr/bi/python3
""" serializes instances to a JSON file and
    deserializes JSON file to instances
"""
from json import loads, dumps
from os.path import exists


class FileStorage():
    """ serializes instances to a JSON file and
        deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            - obj (BaseModel): The object to set in __objects.
        """
        key = ("{}.{}".format(obj.__class__.__name__, obj.id))
        self.__objects[key] = obj
        self.save()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict_of_dicts = {}
        for key, value in self.__objects.items():
            dict_of_dicts[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(dumps(dict_of_dicts))

    def reload(self):
        """deserializes the JSON file to __objects
            only if the JSON file (__file_path) exists
            otherwise, do nothing.
        If the file doesn't exist, no exception should be raised
        """
        if exists(self.__file_path) is False:
            return

        with open(self.__file_path, 'r') as f:
            dicts = loads(f.read())

        from models.engine.get_class import classes

        self.__objects = {}
        for key, obj_dict in dicts.items():
            cls_name = key.split('.')[0]
            cls = classes[cls_name]
            if cls:
                self.__objects[key] = cls(**obj_dict)
