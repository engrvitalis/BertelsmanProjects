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
        if char in operators or char.isdigit():
            tokens.append(char)

    return tokens


def is_operator(char):
    # Return True if char is a mathematical operator or False otherwise.

    # Initialize variable.
    operators = ('+', '-', '*', '/', '*', '/', '=')

    if char in operators:
        return True

    return False

def is_signed_number()

def main():
    # Initialize state variables.
    new_s = []
    # Request input from the user.
    # s = input("Enter mathematical expression: ")
    s = 'witi534()'
    print(tokeniz(s))


if __name__ == "__main__":
    main()