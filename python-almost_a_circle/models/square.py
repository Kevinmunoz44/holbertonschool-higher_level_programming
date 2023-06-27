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
