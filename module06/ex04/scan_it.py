#!/usr/bin/env python3

import sys


total_index = len(sys.argv)

if total_index == 3:
    keyword = sys.argv[1]
    string = sys.argv[2]

    match = string.count(keyword)
    print(f"{match}.")
else:
    print("none")


