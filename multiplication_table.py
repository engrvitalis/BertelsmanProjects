"""
Project: Multiplication table
Description: This program displays multiplication table from 1 to 10
with rows and column headers.

Input: none
Output: String
"""
# Create the column headers.
print("    ", end="")
for k in range(1, 11) :
    print(f"{k:3}", end=" ")

print("   ", end="")
print()

for i in range(1, 11):
    # Create row headers.
    print(' ', end=" ")
    print(i, end=" ")

    # Populate the body with rows X columns.
    print(*(f"{i*j:3}" for j in range(1, 11)))