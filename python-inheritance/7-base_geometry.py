#!/usr/bin/python3
'''Create a class empty'''


class BaseGeometry:

    '''define a function init'''
    def __init__(self):
        pass

    '''define function for area'''
    def area(self):
        raise Exception("area() is not implemented")

    '''define function for validation of value'''
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
