#!/usr/bin/python3
'''Import class Rectangle'''


Rectangle = __import__('9-Rectangle').Rectangle


'''Create class call Square'''


class Square:

    '''Function for validation of size'''
    def __init__(self, size):
        self._size = size
        self.integer_validator("size", size)
