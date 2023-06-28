#!/usr/bin/python3
"""Define the Base Class"""


class Base:
    """constructor"""
    __nb_objects = 0

    """Function Initialized"""

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
