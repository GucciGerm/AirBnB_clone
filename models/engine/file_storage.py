#!/usr/bin/python3
"""
FileStorage Model


"""
import json


class FileStorage():
    """
    Stores Python dictionaries as JSON files
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        All will print the string representation of all instances
        """
        return (self.__objects)

    def new(self, obj):
        """
        New will insert an object into the __objects dictiionary
        """
        self.__objects.update({"{}.{}".format(obj.__class__.__name__,
                                              obj.id): obj})

    def save(self):
        """
        Save will serialize an object in __objects to the JSON file format
        """
        d1 = {}
        with open(self.__file_path, mode="w") as f:
            for k, v in self.__objects.items():
                d1[k] = v.to_dict()
            json.dump(d1, f)

    def reload(self):
        """
        Reload will deserialize a JSON formatted file to an __object
        *** Only if it exists!
        """
        try:
            with open(self.__file_path, mode="r", encoding='UTF-8') as f:
                readit = json.load(f)
                for v in readit.values():
                    from ..base_model import BaseModel
                    from ..user import User
                    from ..state import State
                    from ..city import City
                    from ..amenity import Amenity
                    from ..place import Place
                    from ..review import Review

                    a = eval("{}(**v)".format(v["__class__"]))
                    self.new(a)

        except FileNotFoundError:
            """
            No file has been found so pass
            """
            pass
