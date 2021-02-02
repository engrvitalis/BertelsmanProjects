def flatten_list(data):
    """
    This function recursively moves through a nested list (data) and 
    append its content into a new list (ls). It will then return 
    ls as a flattened version of the data.

    @param: List - data
    @return: List
    """

    # Initialize variable.
    ls = list()

    # Stop the program if list is empty.
    if len(data) == 0:
        return list()
    # Recursively flatten list the first element is a list.
    elif type(data[0]) == list:
        return flatten_list(data[0]) + flatten_list(data[1:])
    else:
        # Add element that are not list into ls.
        ls.append(data[0])

        return ls + flatten_list(data[1:])


def main():
    data = [1, [2, 3], [4, [5, [5, 7]]], [[[8], 9], [10]]]

    print(f'\nOriginal list: {data}')
    print(f'Flattened list: {flatten_list(data)}')


if __name__ == '__main__':
    main()