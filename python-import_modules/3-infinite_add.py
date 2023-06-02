#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numbers = sys.argv[1:]
    value = sum(int(argm) for argm in numbers)
    print(value)
