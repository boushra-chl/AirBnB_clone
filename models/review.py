#!/usr/bin/python3
"""Module that creates a class Review"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Class Review that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Review"""
        super().__init__(*args, **kwargs)
