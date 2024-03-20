#!/user/bin/python3
"""This module defines a class that is the base of all other classes"""


from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Class that defines all common attributes/methods for other classes"""
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = None
        self.add_class_name("__class__", self.__class__.__name__)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def add_class_name(self, key, value):
        self.__dict__[key] = value

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
