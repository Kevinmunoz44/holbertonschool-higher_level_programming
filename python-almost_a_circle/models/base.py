#!/usr/bin/python3
'''Class base'''


class Base:
    '''This is contructor'''
    __nb_objects = 0

    '''Define the function __init__'''
    def __init__(self, id=None):

        '''Conditionals for id'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
