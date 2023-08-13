#!/usr/bin/python3
"""
Contains the class Amenity
"""
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of Amenity

    Attributes:
        name (str): The name of the amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity attributes"""
        super().__init__(*args, **kwargs)
