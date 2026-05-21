#!/usr/bin/env python3


number = int(input("Enter a number\n"))

count = 0

while count <= 9:
    ans = count * number
    print(f"{count} x {number} = {ans}")

    count = count + 1
