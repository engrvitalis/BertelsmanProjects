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


