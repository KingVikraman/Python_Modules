#!/usr/bin/env python3

fst_num = int(input("Enter your first number: "))
sec_num = int(input("Enter your second number: "))

sum_num = (fst_num * sec_num);

print(f"{fst_num} x {sec_num} = {sum_num}");

if sum_num < 0:
    print("The result is negative!")
elif sum_num > 0:
    print("The result is positive!")
elif sum_num == 0:
    print("The result is positive and negative!")
else:
    print("Error")