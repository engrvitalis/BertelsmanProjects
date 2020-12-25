"""
Project: Ceasar Cipher.
Description: This program encode or decode messages using Ceasar Cipher.

Input: String
Output: String
"""

message = 'Nnamdi Vitalis Ewuzie'
shift = 3

for i in message:
    if i.isalpha():
        val = ord(i.lower())
        
        # Encoding
        if val+shift <= ord('z'):
            letter = chr(val + shift)
    else:
        letter = i

    print(letter, end="")