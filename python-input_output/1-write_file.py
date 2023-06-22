#!/usr/bin/python3
'''Function that write in a file'''


def write_file(filename="", text=""):

    '''write a file'''
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
