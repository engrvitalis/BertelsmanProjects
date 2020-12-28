"""
This function reads in a string of characters and determines whether
it contains valid integer.

Input: String
Output: String
"""

def is_integer(string):
    # Make sure value is provided.
    if len(string) != 0:
        # Remove white spaces before processing.
        string = string.strip()
        # Accomodate signed integers.
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
    # Request for user input.
    string = input("Enter a value: ")

# Display relevant information.
print(is_integer(string))
