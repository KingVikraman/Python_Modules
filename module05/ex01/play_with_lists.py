#!/usr/bin/env python3

i = 0
list = [2, 8, 9, 48, 8, 22, -12, 2]

print(f"Original list : {list}.")
while i < len(list):
    list[i] += 2
    i += 1

print(f"New list : {list}.") 