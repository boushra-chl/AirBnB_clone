#!/user/bin/python3
"""A module of serialization-deserialization"""

import json
import os
class FileStorage():
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        obj_id = obj.id
        key = f"{class_name}.{obj_id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_data = {}
        for key, obj in self.__objects.items():
            json_data[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(json_data, json_file)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                json_data = json.load(json_file)
                for key, value in json_data.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    obj = class_(**value)
                    self.__objects[key] = obj
