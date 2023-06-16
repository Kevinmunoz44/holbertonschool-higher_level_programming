#!/usr/bin/python3
"""
Define print # in multiple lines
"""


def print_square(size):
    """Define loop and validations"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")
    square = '#' * size
    for _ in range(size):
        print(square)
