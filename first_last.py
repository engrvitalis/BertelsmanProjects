def first_last(inp):
    """
    This function retrieves the first and last elements of 
    inp which is either a sequence of string, list or tuple,
    join them and return them as same type with inp.

    @param: inp - str, list or tuple
    @return: same type as inp
    """

    # Check inp type, concatenate its first and last elements
    # and return as same type as inp.
    # Display error message if type is not subscriptable.
    if type(inp) == str:
        return inp[0] + inp[-1]
    elif type(inp) == list:
        return [inp[0], inp[-1]]
    elif type(inp) == tuple:
        return (inp[0], inp[-1])
    else:
        return 'Object is not subscriptable!'

# Call and test the function.
print()
print(first_last('a'))              # Output: aa
print(first_last(['b']))            # Output: ['b', 'b']
print(first_last(['1', 3]))         # Output: ['1', 3]
print(first_last([2,4, 5, 6]))      # Output: [2, 6]
print(first_last((4,4, 5, 1)))      # Output: [4, 1]
print(first_last('string'))         # Output: sg
print(first_last({2,4,6}))          # Output: Object is not subscriptable!
print(first_last({'a':3, 'b':4}))   # Output: Object is not subscriptable!
print()