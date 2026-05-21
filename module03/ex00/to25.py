#!/usr/bin/env python3

number = int(input("Enter a number lesser than 25\n"))

if number > 25:
    print("Error, Number more than 25!")
else:
    while number <= 25:
        print(f"Inside the loop, my variable is {number}!")
        number = number + 1
        
