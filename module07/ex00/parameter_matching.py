#!/usr/bin/env python3

import sys


total_params = len(sys.argv) - 1

if total_params == 0:
    print("none")
else:
    index1 = sys.argv[1]
    new_param = input("What was the parameter? : ")

    if new_param == index1:
        print("Good Job!")
    else:
        print("Nope,sorry...")