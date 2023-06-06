#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = [value % 2 == 0 for value in my_list]
    return result
