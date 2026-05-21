#!/usr/bin/env python3

import sys


total_param = len(sys.argv) - 1


if total_param == 0:
    print(f"none")
else:
    param = (sys.argv[1]).upper()
    print(f"First Argument: {param}")