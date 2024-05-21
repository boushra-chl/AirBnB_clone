#!/usr/bin/python3
"""module that creates a class City"""


from models.base_model import BaseModel


class City(BaseModel):
    """class city that inherites from BaseModel"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the City"""
        super().__init__(self, *args, **kwargs)
