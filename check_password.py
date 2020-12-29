"""
This program check if a password is good by using the following criteria:
- It must contain at least 8 characters.
- It must contain at least one uppercase letter.
- It must contain at least one lowercase letter.
- It must contain at least one number.

Input: String
Output: Boolean
"""

def check_password(password):
    # Initialize state variables.
    uppercase = False
    lowercase = False
    digit = False

    # Check for password compliance with specification.
    for char in password:
        if char.isupper():
            uppercase = True
        if char.islower():
            lowercase = True
        if char.isdigit:
            digit = True
    
    return (len(password) >= 8 and uppercase and lowercase and digit)


def main():
    if check_password:
        print("The password is good!")
    else:
        print("The password is bad!")

if __name__ == '__main__':
    main()