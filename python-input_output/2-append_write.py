#!/usr/bin/python3
'''Function for append a string'''


def append_write(filename="", text=""):

    '''write a file'''
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
