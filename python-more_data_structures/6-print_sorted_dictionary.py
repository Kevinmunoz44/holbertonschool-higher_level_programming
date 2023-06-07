#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = sorted(a_dictionary.keys())

    for i in key:
        print(i + ': ' + str(a_dictionary[i]))
