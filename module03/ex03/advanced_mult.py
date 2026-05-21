#!/usr/bin/env python3

table = 0

while table <= 10:
    print(f"Table of {table}:", end="")

    multiplier = 0
    while multiplier <= 10:
        result = table * multiplier
        print(f" {result}" , end="")
        multiplier = multiplier + 1

    print()
    table = table + 1
