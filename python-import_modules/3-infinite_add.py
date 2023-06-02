#!/usr/bin/python3
import sys
numbers = sys.argv[1:]
value = sum(int(argm) for argm in numbers)
print(value)
