#!/usr/bin/python3
'''Import module json'''
import json


'''function that writes an Object to a text file'''


def save_to_json_file(my_obj, filename):

    '''write in json'''
    with open(filename, "w") as fileobj:
        fileobj.write(json.dumps(my_obj))
        return fileobj
