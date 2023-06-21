#!/usr/bin/python3
'''Defined a inherence'''


def inherits_from(obj, a_class):

    '''Validation between obj and a_class'''
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
