def my_sum(*args):
    """
    This function takes a variable number of arguments from 
    the user and return the sum.

    @param: List, float, int, tuple.
    @return: Int, float.
    """

    # Initialize result variable.
    result = 0
    # Add the next available number to result.
    for x in args:
        result += x
    return result


def main():
    # Get the sum of variables a, b, c and display the an output.
    a, b, c, d = [2, 4], 5, (4, 5.1), 6.0
    print(f'\n{a} + {b} + {c} + {d} = {my_sum(*a, b, *c, d)}')


if __name__ == '__main__':
    main()