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
    # Request input from user and print out total character count
    # and unique character count.
    s = input("\nEnter a string of characters: ")

    print(f'Total characters: {len(s)}')
    print(f'Unique characters count: {unique_char(s)}')


if __name__ == "__main__":
    main()