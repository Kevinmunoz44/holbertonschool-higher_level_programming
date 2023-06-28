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

    '''Function that get area'''
    def area(self):
        '''Value of the area'''
        result = self.__height * self.__width
        return result

    '''Function display'''
    def display(self):
        '''Run a String'''
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    '''Method str for print'''
    def __str__(self):
        '''Print values'''
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    '''Function for update'''
    def update(self, *args, **kwargs):
        '''Conditionals for the args'''
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

        '''Conditional for kwargs key and values'''
        if len(args) == 0 or len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    '''Function for a dictionary'''
    def to_dictionary(self):
        '''Return a dictionary'''
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
