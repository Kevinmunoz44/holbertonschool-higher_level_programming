#!/usr/bin/python3
'''Import json'''
import json


'''Define a function that read a file'''
def read_file(filename=""):
    
    '''read a file'''
    with open("my_file_0.txt", 'r', encoding='UTF8') as filename:
        content = filename.read()
        print(content, end="\n")
