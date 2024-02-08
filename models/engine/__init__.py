#!/usr/bin/python3
"""
Initialization file for the engine module.
"""
from .file_storage import FileStorage

storage = FileStorage()
storage.reload()

