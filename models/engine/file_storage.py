#usr/bin/python3
"""
defines the class FileStorage
"""


import json
from models.base_model import BaseModel


class FileStorage:
    """storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes to json file"""
        objects_dict = {}
        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(objects_dict, json_file)

    def reload(self):
        """deserializes the json file"""
        try:
            with open(self.__file_path, "r") as json_file:
                objects_dict = json.load(json_file)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
