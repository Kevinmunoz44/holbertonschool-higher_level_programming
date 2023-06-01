#!/usr/bin/python3
def islower(c):
    if ord (c) > 96 and ord (c) < 123:
        return True
    elif ord (c) > 47 and ord (c) < 58 or ord (c) > 64 and ord (c) < 91:
        return False
