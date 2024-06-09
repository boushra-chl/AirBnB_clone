#!/usr/bin/python3
"""module that creates a class Amenity"""


from models.base_model import BaseModel                         


class Amenity(BaseModel):
    """class Amenity that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the Amenity"""
        super().__init__(*args, **kwargs)
