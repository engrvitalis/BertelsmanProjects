"""
This function will generate random passwords of length between 
7 and 10. They will be generated from ASCII positions 33 through 126.

Input: None
Output: Boolean
"""

def password_generator():
    import random

    # Initialize state variables.
    password = ''
    length = random.randint(7, 10) # Decide the length of your password.

    # Generate password.
    for i in range(length):
        char_position = random.randint(33, 126) # Generate character position in ASCII table.
        password += chr(char_position)

    return password


print(password_generator())