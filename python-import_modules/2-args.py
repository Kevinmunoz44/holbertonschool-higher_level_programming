#!/usr/bin/python3
import sys
if __name__ == "__main__":

    numbers = sys.argv[1:]
    num_len = len(numbers)

    if num_len == 0:
        print(f"{num_len}", "arguments.")
    elif num_len == 1:
        print(f"{num_len}", "arguments:")
    else:
        print(f"{num_len}", "arguments:")

    for i, number in enumerate(numbers):
        print(f"{i+1}:", number)