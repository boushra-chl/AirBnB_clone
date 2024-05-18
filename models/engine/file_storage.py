#usr/bin/python3
import os
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        json_data = {}
        for key, obj in self.__objects.items():
            json_data[key] = obj.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(json_data, json_file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as json_file:
                json_data = json.load(json_file)
                for key, value in json_data.items():
                    parts = key.split('.')
                    if len(parts) == 2:
                        class_name, obj_id = parts
                        obj_class = globals().get(class_name)
                        if obj_class:
                            obj = obj_class(**value)
                            self.__objects[key] = obj
                    else:
                        print(f"Class {class_name} not found.")
                else:
                    print(f"Invalid key format: {key}")
