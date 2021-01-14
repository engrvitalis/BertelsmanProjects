def unique_char(string):
    """
    This function counts the number of unique characters in 
    in a string.
    @param: String
    @return: Integer
    """

    # Return the length of unique values.
    return len(set(string.lower()))


def main():
    # Request input from user and print the unique value count.
    print(f'{unique_char(input("Enter a string of characters: "))} unique characters')


if __name__ == "__main__":
    main()