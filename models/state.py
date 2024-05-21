#!/usr/bin/python3
"""module that creates a class state"""


from models.base_model import BaseModel


class State(BaseModel):
    """class state that inherites from BaseModel"""

    name = ""
    def __init__(self, *args, **kwargs):
        """initializes the user"""
        super().__init__(self, *args, **kwargs)
