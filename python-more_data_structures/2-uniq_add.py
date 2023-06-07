#!/usr/bin/python3
def uniq_add(my_list=[]):
    numbers_int = []
    for element in my_list:
        if element not in numbers_int:
            numbers_int.append(element)
    return numbers_int
