def strsort(string):
    """
    This function takes a string and return a 
    sorted version of it.

    @param: str
    @return: str
    """

    # Return sorted string.
    return ''.join(sorted(string.lower()))


def main():
    # Request string input from user and return the sorted version
    # of it.
    string = input("Enter a string of characters: ")
    print(f'\nThe string "{string}" after sorting is "{strsort(string)}".\n')


if __name__ == '__main__':
    main()