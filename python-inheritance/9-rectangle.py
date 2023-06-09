#!/usr/bin/python3
"""Import class BaseGeomety"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


'''Create a class Rectangle'''


class Rectangle(BaseGeometry):

    '''function for privated with and height'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    '''Function for area of a rectangle'''
    def area(self):
        return self.__width * self.__height

    '''Function str'''
    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
