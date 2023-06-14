#!/usr/bin/python3

'''Create a new Square'''


class Square:

    '''Define a square'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    '''Method get for the size'''
    @property
    def size(self):
        return self.__size

    '''Method set for the size'''
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    '''Method get for the position'''
    @property
    def position(self):
        return self.__position

    '''Method set for the position'''
    @position.setter
    def position(self, value):
        if isinstance((value, tuple) and len(value) == 2 and
                      all(isinstance(v, int) and v >= 0 for v in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    '''Return area of a square'''
    def area(self):
        return self.__size ** 2

    '''prints in stdout the square with the character #:'''
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
