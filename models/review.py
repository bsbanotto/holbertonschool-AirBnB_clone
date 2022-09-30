#!/usr/bin/python3
"""Module for review, inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class, inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
