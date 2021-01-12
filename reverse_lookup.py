def reverseLookup(dic, value):
    """
    This program takes two arguments, a dictionary and a value
    and tries to lookup the corresponding keys for the value.

    @param: Dictionary
            value - int, float, str etc.
    @return: list of keys.
    """

    # Initialize variable
    ls = list()

    for k, v in dic.items():
        if v == value:
            ls.append(k)

    return ls


def main():
    pass
    # print(reverseLookup({'me': 4, 'you': 6, 'i': 7, 'jjs': 7}, 8))

if __name__ == "__main__":
    main()