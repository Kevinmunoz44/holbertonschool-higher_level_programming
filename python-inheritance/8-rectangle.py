#!/usr/bin/python3
"""Import class BaseGeomety"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


'''Create a class call Rectangle'''


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
