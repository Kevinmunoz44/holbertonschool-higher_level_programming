#!/usr/bin/python3
'''Import module json'''
import json


'''Function that creates an Object from a “JSON file'''


def load_from_json_file(filename):

    '''Create a object'''
    with open(filename, 'r') as fileobj:
        data = json.load(fileobj)
        return data
