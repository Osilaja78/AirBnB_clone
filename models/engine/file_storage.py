#!/usr/bin/python3
"""
Class FileStorage that serializes instances
to a JSON file and deserializes JSON file
to instances.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """A new file storage model"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict __objects"""

        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""

        self.__objects["{}.{}".format(
                obj.__class__.__name__, str(obj.id)
            )] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""

        serialized_objects = {}
        for k, v in self.__objects.items():
            serialized_objects[k] = v.to_dict()

        with open(self.__file_path, "w") as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        try:
            with open(self.__file_path) as json_file:
                data = json.load(json_file)
                for k, v in data.items():
                    class_name = v["__class__"]
                    del v["__class__"]
                    self.__objects[k] = globals()[class_name](**v)
        except FileNotFoundError:
            return
