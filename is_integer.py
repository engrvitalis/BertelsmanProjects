"""
This program reads in a string of characters and determines whether
it contains valid integer.

Input: String
Output: String
"""

def is_integer(string):
    if len(string) != 0:
        string = string.strip()
        if string[0] in ['+', '-']:
            if string[1:].isdigit():
                display = f'{string.strip()} is an integer'
            else:
                display = f'{string.strip()} is not an integer'
        else:
            if string.isdigit():
                display = f'{string.strip()} is an integer'
            else:
                display = f'{string.strip()} is not an integer'
    else:
        display = f'Invalid input!'

    return display


if __name__ == '__main__':
    string = input("Enter a value: ")

print(is_integer(string))
