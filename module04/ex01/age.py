#!/usr/bin/env python3


age = int(input("Please tell me your age?: "))

print(f"You currently are {age} years old!")

iterator = 10
while iterator <= 30:
    sum_age = age + iterator
    print(f"In {iterator} years, you will be {sum_age} years old!")
    iterator = iterator + 10