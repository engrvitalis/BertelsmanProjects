"""
This program reads in a string of characters and determines whether
it contains valid integer.

Input: String
Output: String
"""

def is_integer(string):
    return len(string) != 0 and string.strip().isdigit()



if __name__ == '__main__':
    string = '345'

print(is_integer(string))
