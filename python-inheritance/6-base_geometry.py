#!/usr/bin/python3
'''Create a class empty'''


class BaseGeometry:

    '''define a function init'''
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
