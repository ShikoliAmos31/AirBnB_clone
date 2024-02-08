#!/usr/bin/python3
"""This module contains the FileStorage class."""
import json


class FileStorage:
    """FileStorage class for serializing and deserializing instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the file exists)."""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    module_name = class_name.lower()
                    module = __import__('models.' + module_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    instance = class_(**value)
                    self.new(instance)
        except FileNotFoundError:
            pass

