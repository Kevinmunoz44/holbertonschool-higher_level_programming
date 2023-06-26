#!/usr/bin/python3
'''Import the class call base'''
from models.base import Base


'''Create class call Rectangle'''


class Rectangle(Base):

    '''Define function with constructor'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    '''Method get for widht'''
    @property
    def width(self):
        return self.__width

    '''Method set for width'''
    @width.setter
    def width(self, value):
        self.__width = value

    '''Method get for height'''
    @property
    def height(self):
        return self.__height

    '''Method set for height'''
    def height(self, value):
        self.__height = value

    '''Method get for x'''
    @property
    def x(self):
        return self.__x

    '''Method set for x'''
    def x(self, value):
        self.__x = value

    '''Method get for y'''
    @property
    def y(self):
        return self.__y

    '''Method set for y'''
    def y(self, value):
        self.__y = value
