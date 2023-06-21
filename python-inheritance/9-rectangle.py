#!/usr/bin/python3
"""Import class BaseGeomety"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


'''Create a class Rectangle'''


class Rectangle(BaseGeometry):

    '''function for privated with and height'''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    '''Function for area of a rectangle'''
    def area(self):
        return self.width * self.height

    '''Function for print mensagge'''
    def __str__(self):
        return f"[Rectangle] {self.width}/{self.height}"

    '''Function for print self'''
    def print(self):
        print(self)
