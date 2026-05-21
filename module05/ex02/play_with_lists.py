#!/usr/bin/env python3

i = 0
ori_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = []

print(f"Original list : {ori_list}.")

while i < len(ori_list):
	if ori_list[i] > 5:
		modified_list = ori_list[i] + 2
		new_list.append(modified_list)

	i += 1
print(f"New list : {new_list}.")

# ==============================================================================
# PYTHON NOTES: THE .append() METHOD (FILTERING LOGIC USE CASE)
# ==============================================================================

# WHAT IT DOES IN MY CODE:
# It acts as a "collector" to build a brand-new list from scratch, keeping 
# only the specific numbers that pass my condition.

# WHY I AM USING IT TO FILTER NUMBERS LESS THAN 5:
# 1. Gatekeeper Logic: By putting .append() inside the 'if list[i] > 5:' block, 
#    it only runs for big numbers. Smaller numbers are skipped completely.
# 2. Safety (No Crashes): Modifying or deleting numbers from an original list 
#    while looping through it can confuse the index counter and crash your code.
# 3. Clean Output: It allows us to leave behind the unwanted numbers (like 2, -12) 
#    so the final printout only shows the filtered results.

# VISUAL FLOW IN THE LOOP:
# [2, 8, -12] ---> Is it > 5? ---> NO  ---> (Ignored, left behind)
#                             ---> YES ---> New value + 2 ---> .append() to new_list
# ==============================================================================
