#!/usr/bin/python3
'''Create a new class call My list'''


class MyList(list):
    '''Function that prints a list of objects'''

    def print_sorted(self):
        listsort = sorted(self)
        print(listsort)
