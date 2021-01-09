def countRange(lst, min_value, max_value):
    """
    This program will return the total number of elements within a 
    particular range in a list.

    @params: List - The parameter to be processed.
            min_value - Minimum value of the range.
            max_value - Maximum value of the range.
    @return: Integer - Elements count from and including min_value
            and up to but excluding max_value.
            ie. min_value <= element < max_value.
    """

    # Initialize counter
    count = 0

    # Move through the list and increment counter if
    # number is within specified range.
    for num in lst:
        if min_value <= num < max_value:
            count += 1

    return count