#!/usr/bin/python3
'''Define a function'''

def is_same_class(obj, a_class):
    
    '''Validation about if the obj is instance of the class'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
