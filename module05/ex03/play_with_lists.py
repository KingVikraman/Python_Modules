#!/usr/bin/env python3

i = 0
ori_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = set()

print(f"Original list : {ori_list}.")

while i < len(ori_list):
	if ori_list[i] > 5:
		modified_list = ori_list[i] + 2

		new_list.add(modified_list)
	i += 1

print(f"New list : {new_list}.")


# ==============================================================================
# PYTHON CHEAT SHEET: WORKING WITH SETS & DUPLICATE FILTERING
# ==============================================================================

# WHAT IS A SET?
# A built-in data type used to store collections of data. Unlike a list, 
# a set is UNORDERED (no indexes) and items must be UNIQUE (no duplicates).

# KEY DIFFERENCES: LIST vs SET
# Feature        List                     Set
# ----------------------------------------------------
# Brackets       Square [ ]               Curly { }
# Order          Maintained (0, 1, 2...)  Random / Unordered
# Duplicates     Allowed                  Strictly Forbidden (Deleted)
# Method         .append(item)            .add(item)


# HOW THE .add() METHOD CHECKS FOR DUPLICATES (BEHIND THE SCENES):
# When you call 'my_set.add(10)', Python looks inside the collection:
# - If 10 is NOT there -> It gets added inside the curly braces.
# - If 10 IS already there -> Python drops it instantly. No error is thrown.


# MANDATORY EXERCISE CODE BLUEPRINT:
# ----------------------------------
# 1. Create empty set:   unique_set = set()  # Do NOT use {} (that makes a dictionary!)
# 2. Add an item:        unique_set.add(value)
# 3. Print the set:      print(unique_set)   # Outputs automatically as {x, y, z}


# THE ULTIMATE SHORTCUT (Casting):
# If you ever want to instantly remove duplicates from a list without a loop:
# original = [1, 2, 2, 3, 3, 3]
# unique   = list(set(original))  # Result: [1, 2, 3]
# ==============================================================================
