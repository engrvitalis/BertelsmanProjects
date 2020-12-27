"""
This project finds the greatest common divisor for two integers.

Input: Integers
Output: String
"""

m = int(input("Enter the first integer: "))
n = int(input("Enter the second integer: "))

d = abs(min(m, n))
while True:
    if m % d == 0 and n % d == 0:
        print(f"The greatest common divisor of {m} and {n} is {d}")
        break
    else:
        d -= 1