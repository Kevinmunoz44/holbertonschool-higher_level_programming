#!/usr/bin/python3
def no_c(my_string):
    change_letter = ""
    for i in my_string:
        if i != "c" and i != "C":
            change_letter += i

    return change_letter
