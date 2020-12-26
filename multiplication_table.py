"""
Project: Multiplication table
Description: This program displays multiplication table from 1 to 10

Input: none
Output: String
"""

for i in range(1, 11):
    print(*(f"{i*j:3}" for j in range(1, 11)))