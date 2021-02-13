def mySum(*items):
    """
    This function takes variable number of arguments.
    It returns empty tuple if called with no arguments,
    sum if called with int or float arguments or it will
    concatenate arguments elements if called with str, list or
    tuple.
    
    @param: *items: int, float, list or tuple.
    @return: int, float, list or tuple.
    """
    # Return empty tuple if no argument was provided.
    if not items:
        return items 

    # Initialize output with the first argument.
    output = items[0]
    # Add or concatenate the remaining arguments to output and return it.
    for item in items[1:]:
        output += item
    return output

# Test calls.
print(mySum([2,4,5], [3,5]))                # Expected Output: [2, 4, 5, 3, 5]
print(mySum(1, 2, 3))                       # Expected Output: 6
print(mySum('1', 's', 't'))                 # Expected Output: 1st
print(mySum())                              # Expected Output: ()