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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    '''Method get for height'''
    @property
    def height(self):
        return self.__height

    '''Method set for height'''
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    '''Method get for x'''
    @property
    def x(self):
        return self.__x

    '''Method set for x'''
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    '''Method get for y'''
    @property
    def y(self):
        return self.__y

    '''Method set for y'''
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
