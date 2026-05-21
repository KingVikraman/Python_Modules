#!/usr/bin/env python3

import sys


total_param = len(sys.argv) - 1
# print(f"Ignored argument : {sys.argv[0]}.")
# print(f"Actual argument : {sys.argv[1]}.")

if total_param == 0:
    print(f"Number of parameters: {total_param}.")
else:
    print(f"Number of parameters: {total_param}.")


# ==============================================================================
# PYTHON NOTES: COMMAND LINE ARGUMENTS WITH sys.argv
# ==============================================================================
# ALWAYS REQUIREMENT: 'import sys' at the top of your file.

# WHAT IS IT?
# sys.argv is a LIST of strings containing all arguments passed to the script.

# HOW THE INDEXING WORKS:
# If you run: ./script.py "hello world" 42
# - sys.argv[0] -> './script.py'      (Always the script's own filename!)
# - sys.argv[1] -> 'hello world'      (The terminal strips the quotes automatically)
# - sys.argv[2] -> '42'               (Note: All arguments come in as STRINGS)

# COUNTING PARAMETERS ACCURATELY:
# Use 'len(sys.argv) - 1' because you must exclude the script name at index 0.

# EDGE CASES HANDLED BY THE TERMINAL:
# 1. Spaces inside quotes ("arg one"): Counted as ONE parameter.
# 2. Spaces outside quotes (arg one): Counted as TWO parameters.
# 3. No parameters: len(sys.argv) will equal 1.
# ==============================================================================
