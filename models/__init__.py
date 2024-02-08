#!/usr/bin/python3
"""
Initialization file for the models module.
"""

from .engine import storage
from .base_model import BaseModel
from models.user import User

storage.reload()

