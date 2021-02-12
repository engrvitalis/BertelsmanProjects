def first_last(inp):
    """
    This function retrieves the first and last elements in 
    inp, join and return them of type inp.

    @param: inp - any type
    @return: same type as inp
    """
    if type(inp) == str:
        return inp[0] + inp[-1]
    elif type(inp) == list:
        return [inp[0], inp[-1]]
    elif type(inp) == tuple:
        return (inp[0], inp[-1])
    else:
        return 'Object is not subscriptable!'


print(first_last([2,4, 5, 6]))
print(first_last((2,4, 5, 6)))
print(first_last('string'))
print(first_last({2,4,6}))
print(first_last({'a':3, 'b':4}))