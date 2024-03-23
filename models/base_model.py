#!/user/bin/python3
"""This module defines a class that is the base of all other classes"""


from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Class that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at":
                    kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = {**self.__dict__}
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict
