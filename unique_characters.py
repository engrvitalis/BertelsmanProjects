def unique_char(string):
    """
    This function counts the number of unique characters in 
    in a string.
    @param: String
    @return: Integer
    """

    return set(string)


def main():
    print(unique_char('skskgjrtjjj'))


if __name__ == "__main__":
    main()