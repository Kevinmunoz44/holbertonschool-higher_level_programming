#!/usr/bin/python3

'''Create a new class empty'''


class Square:
    '''Define a square'''
    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
        
    '''Return area of a square'''    
    def area(self):
        area = self.__size * self.__size
        return area
