#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    sign = "-"
else:
    sign = ""

if digit > 5:
    print("Last digit of" ,number , "is",sign,digit , "and is greater than 5")
if digit == 0:
    print("Last digit of" ,number , "is",sign,digit , "and is 0")
if digit < 6 and digit != 0:
    print("Last digit of" ,number , "is",sign,digit , "and is less than 6 and not 0")
