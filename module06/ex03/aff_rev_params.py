#!/usr/bin/env python


import sys

total_param = len(sys.argv) - 1

if total_param <= 2:
    print(f"none")
else:
    i = total_param
    while i != 0:
        print(f"{sys.argv[i]}")
        i -= 1
