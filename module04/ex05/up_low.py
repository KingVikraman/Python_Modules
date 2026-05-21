#!/usr/bin/env python3

text = input("Say something : ")

converted_text = text.swapcase()
print(f"Initial Text : {text}.\nConverted Text : {converted_text}.")


# ==============================================================================
# PYTHON NOTES: THE .swapcase() STRING METHOD
# ==============================================================================

# WHAT IT DOES:
# Converts all uppercase letters to lowercase and all lowercase letters to 
# uppercase within a string. Numbers, spaces, and punctuation are left alone.

# USE CASES:
# 1. Inverting User Input: Helpful if a user accidentally types with Caps Lock on.
# 2. Text Animations/Styling: Creating "tOgGlEd" text effects for UI elements.
# 3. Data Processing: Quickly flipping letter cases without writing a loop.