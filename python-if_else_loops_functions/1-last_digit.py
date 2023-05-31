#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    sign = "-"
else:
    sign = ''

if lastdigit > 5:
    print("Last digit of {0} is {1}{2} and is greater than 5".format(number, sign, lastdigit))
elif lastdigit == 0:
    print("Last digit of {0} is {1}{2} and is 0".format(number, sign, lastdigit))
else:
    print("Last digit of {0} is {1}{2} and is less than 6 and not 0".format(number, sign, lastdigit))