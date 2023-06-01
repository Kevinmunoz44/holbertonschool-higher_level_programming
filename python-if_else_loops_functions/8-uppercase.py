#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            i = chr(ord(i) - 32)
        new_str += i
    print(new_str)
