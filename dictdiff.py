def dictdiff(first, second):
    """
    This function takes two dicts as arguments and returns a new dict 
    that expresses the difference between the two dicts. 
    If there are no differences between the dicts, dictdiff returns an empty dict.

    @param: dict - first, second
    @return: dict
    """

    # Initialize variable.
    output = dict()
    # Remove key duplicates before interation.
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        # Check if key values in first and second are unequal.
        if first.get(key) != second.get(key):
            # Add key value pair in output with value as a list
            # containing key value in first and second dicts.
            output[key] = [first.get(key), second.get(key)]

    return output

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
d3 = {'a': 1, 'b': 2, 'd': 3}

print(dictdiff(d1, d1))
print(dictdiff(d1, d2))
print(dictdiff(d1, d3))
print(dictdiff(d2, d3))