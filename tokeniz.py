def tokeniz(string):
    """
    This program takes string containing mathematical expressions
    and breaks it into a list of tokens.

    @param: String.
    @return: List of tokens.
    """

    # Initialize variables.
    tokens = list()
    i = 0

    # Remove spaces.
    string = strip_space(string)

    while i < len(string):
        # Check if character is an operator.
        if is_operator(string[i]):
            # Check if character is either '+' or '-' and not at the
            # beginning or end of string.
            if i != 0 and i != len(string)-1 and string[i] in ['+', '-']:
                # Check if '+' or '-' is following a number or ')'.
                if string[i-1] == ')' or string[i-1].isdigit():
                    # Add '+' or '-' as an operator.
                    tokens.append(string[i])
                else:
                    if string[i+1].isdigit():
                        # Add as a signed number.
                        tokens.append(''.join(string[i:i+2]))
                        i += 1
                    else:
                        tokens.append(string[i])
            else:
                # Take care of signed numbers at string extremes.
                if string[i] in ['+', '-'] and i != len(string) - 1 and string[i + 1].isdigit():
                    tokens.append(''.join(string[i:i+2]))
                    i += 1
                else:
                    tokens.append(string[i])
        # Add parenthesis and numbers.
        elif string[i] in ['(', ')'] or string[i].isdigit():
            tokens.append(string[i])
        i += 1

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
    return list(''.join(s.split()))


def main():
    # Request input from the user.
    s = input("Enter mathematical expression: ")

    # Print tokens.
    print("\nIdentified tokens are:")
    for token in tokeniz(s):
        print(token, end='  ')


if __name__ == "__main__":
    main()
    # print(strip_space('rtry535  77h'))