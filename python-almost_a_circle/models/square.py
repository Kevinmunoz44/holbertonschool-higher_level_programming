#!/usr/bin/python3
'''Import the class call Rectangle'''
from models.rectangle import Rectangle


'''Create class call Square'''


class Square(Rectangle):

    '''Constructor of the class'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    '''Method str for square'''
    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    '''Method get for size'''
    @property
    def size(self):
        '''return the width'''
        return self.width

    '''Method set for size'''
    @size.setter
    def size(self, value):
        '''Enter the attributes'''
        self.width = value
        self.height = value

    '''Function for run each atributte'''
    def update(self, *args, **kwargs):
        '''Conditional for args'''
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        '''Conditional for kwargs key and values'''
        if len(args) == 0 or len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    '''Function for a dictionary'''
    def to_dictionary(self):
        '''Return a dictionary'''
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
