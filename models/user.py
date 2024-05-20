#!/usr/bin/python3
"""module that defines the class user"""


from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
