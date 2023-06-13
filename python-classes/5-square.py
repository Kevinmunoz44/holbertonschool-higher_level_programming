#!/usr/bin/python3

'''Create a new class empty'''


class Square:
    '''Define a square'''
    def __init__(self, size=0):
        self.__size = size

    '''Method get for the size'''
    @property
    def size(self):
        return self.__size

    '''Method set for the size'''
    @size.setter
    def size(self, value):
        self.__size = value
        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    '''Return area of a square'''
    def area(self):
        area = self.size * self.size
        return area

    '''prints in stdout the square with the character #:'''
    def my_print(self):
        if self.__size == 0:
            print()
        for _ in range(self.size):
            print("#" * self.size)
