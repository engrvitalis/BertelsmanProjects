def how_many_different_numbers(ls):
    """
    This function takes a single list of integers 
    and returns the number of different integers it contains.

    @param: list - ls
    @return: int
    """

    # Remove duplicates and return number of unique elements.
    return len(set(ls))


# Test function call
ls = [2, 3, 3, 6, 5, 2, 5, 7]

print('List of integers:', ls)
print(f'Number of unique elements: {how_many_different_numbers(ls)}')