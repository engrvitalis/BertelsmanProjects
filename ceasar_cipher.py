"""
Project: Ceasar Cipher.
Description: This program encode or decode messages using Ceasar Cipher.

Input: String
Output: String
"""

message = input("Enter message: ")
shift = int(input("Enter cipher key: "))

for letter in message: 
    if not letter.isalpha():
        char = letter
    else:
        if letter.isupper():
            char = chr((ord(letter) + shift - ord('A')) % 26 + ord('A'))
        else:
            char = chr((ord(letter) + shift - ord('a')) % 26 + ord('a'))
          
    print(char, end="")
