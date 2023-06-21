#!/usr/bin/python3
'''Import class Rectangle'''


Rectangle = __import__('9-rectangle').Rectangle


'''Create class call Square'''


class Square(Rectangle):

    '''Function for validation of size'''
    def __init__(self, size):
        self._size = size
        self.integer_validator("size", size)
        '''Super trae todos los metodos de la clase anterior'''
        super().__init__(size, size)
