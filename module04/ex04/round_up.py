#!/usr/bin/env python3
import math


number = float(input("Give me a number! : "))

rounded_num = math.ceil(number)

print(f"Original = {number}.\nRounded Up = {rounded_num}.")





# ==============================================================================
# PYTHON CHEAT SHEET: THE 'math' MODULE REFERENCE NOTES
# ==============================================================================
# Remember to always include 'import math' at the top of your python script!
# ==============================================================================

# --- 1. ROUNDING & VALUES ---
# math.ceil(x)  -> Rounds UP to the next whole integer. (e.g., 42.1 -> 43)
# math.floor(x) -> Rounds DOWN to the next whole integer. (e.g., 42.9 -> 42)
# math.trunc(x) -> Cuts off the decimals completely. (e.g., 42.99 -> 42)
# math.fabs(x)  -> Returns the absolute (positive) value as a float. (e.g., -5.5 -> 5.5)

# --- 2. POWERS & ROOTS ---
# math.sqrt(x)  -> Returns the square root of x as a float. (e.g., 16 -> 4.0)
# math.pow(x,y) -> Raises x to the power of y as a float. (e.g., 2, 3 -> 8.0)

# --- 3. MATH CONSTANTS ---
# math.pi       -> The value of Pi (approx: 3.141592653589793)
# math.e        -> Euler's number (approx: 2.718281828459045)

# --- 4. DATA LISTS & ARITHMETIC ---
# math.fsum([list]) -> Accurately adds up a list of float numbers without memory errors.
# math.gcd(x, y)    -> Returns the Greatest Common Divisor of two whole integers.

# --- 5. SAFETY CHECKS ---
# math.isnan(x) -> Returns True if the value is "Not a Number" (NaN).
# math.isinf(x) -> Returns True if the value is positive or negative infinity.
# ==============================================================================
