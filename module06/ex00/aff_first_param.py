#!/usr/bin/env python3

import sys


total_param = len(sys.argv) - 1

if total_param == 0:
    print(f"none")
else:
    print(f"First Argument: {sys.argv[1]}")
    # print(f"First Argument: {sys.argv[2]}")
    # print(f"First Argument: {sys.argv[3]}")

