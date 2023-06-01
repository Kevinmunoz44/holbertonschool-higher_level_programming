#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        new_str += i
    print(new_str)