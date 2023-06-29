#!/usr/bin/python3
'''Imports necesary'''
import json
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

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)
        with open(cls.__name__ + ".json", "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                instance_list = [cls.create(**obj_dict) for obj_dict in dict_list]
                return instance_list
        except FileNotFoundError:
            return []
