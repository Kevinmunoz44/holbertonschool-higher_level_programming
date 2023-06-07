#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_1 = set(set_1)
    set_2 = set(set_2)
    union_set = set_1.symmetric_difference(set_2)
    return union_set
