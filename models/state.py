#!/usr/bin/python3
""" holds class State"""


import models
from models.base_model import BaseModel


class State(BaseModel):
    """class state that inherits from basemodel"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
