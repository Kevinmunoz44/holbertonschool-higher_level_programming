#!/usr/bin/python3
'''Import json'''
import json


'''Define a function that read a file'''


def read_file(filename=""):

    '''read a file'''
    with open(filename, 'r', encoding='UTF8') as file:
        for line in file:
            print(line, end="")
