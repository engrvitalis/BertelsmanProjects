def tokeniz(string):
    """
    This program takes string containing mathematical expressions
    and breaks it into a list of tokens.

    @param: String.
    @return: List of tokens.
    """

    # Initialize state variables.
    tokens = list()

    # Go through the string and extract the tokens.

    for char in string:
        if char in ['*', '/', '^', '(', ')']:
            tokens.append(char)
        else:
            n = string[string.index(char) - 1]
            if char in ['+', '-'] and string.index(char) > 0 and n.isdigit() or n == ')':
                tokens.append(char)

    return tokens


def is_operator(char):
    # Return True if char is a mathematical operator or False otherwise.

    # Initialize variable.
    operators = ('+', '-', '*', '^', '/', '=')

    if char in operators:
        return True

    return False


def strip_space(s):
    # This function splits a string argument into individual characters.

    # remove space(s) from the string and return result.
    return ''.join(s.split())


def main():
    # Initialize state variables.
    new_s = []
    # Request input from the user.
    # s = input("Enter mathematical expression: ")
    s = 'witi5+34()+-*'
    print(s)
    print(tokeniz(s))


if __name__ == "__main__":
    main()
    # print(strip_space('rtry535  77h'))