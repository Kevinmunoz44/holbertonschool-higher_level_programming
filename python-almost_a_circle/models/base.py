#!/usr/bin/python3
'''Imports necesary'''
import turtle
from turtle import *

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
                instance_list = [cls.create(**obj_dict)
                                 for obj_dict in dict_list]
                return instance_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.reset()
        drawTurtle = turtle.Turtle()
        drawTurtle.screen.bgcolor("#4A5A5D")
        drawTurtle.pensize(4)

        drawTurtle.color("#0FC3E6")
        for turtleRectangle in list_rectangles:
            drawTurtle.showturtle()
            drawTurtle.up()
            drawTurtle.goto(turtleRectangle.x, turtleRectangle.y)
            drawTurtle.down()
            for k in range(2):
                drawTurtle.forward(turtleRectangle.width)
                drawTurtle.left(100)
                drawTurtle.forward(turtleRectangle.height)
                drawTurtle.left(100)
            drawTurtle.hideturtle()

        drawTurtle.color("#0FE634")
        for turtleSquare in list_squares:
            drawTurtle.showturtle()
            drawTurtle.up()
            drawTurtle.goto(turtleSquare.x, turtleSquare.y)
            drawTurtle.down()
            for k in range(2):
                drawTurtle.forward(turtleSquare.width)
                drawTurtle.right(-100)
                drawTurtle.forward(turtleSquare.height)
                drawTurtle.right(-100)
            drawTurtle.hideturtle()

        turtle.exitonclick()
