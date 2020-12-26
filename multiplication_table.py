"""
Project: Multiplication table
Description: This program displays multiplication table from 1 to 10
with rows and column headers.

Input: none
Output: String
"""

start = 1
stop = 10

# Create the column headers.
print("    ", end="")
for k in range(start, stop+1) :
    print(f"{k:3}", end=" ")

print("   ", end="")
print()

for i in range(start, stop+1):
    # Create row headers.
    print(' ', end=" ")
    print(i, end=" ")

    # Populate the body with rows x columns.
    print(*(f"{i*j:3}" for j in range(start, stop+1)))