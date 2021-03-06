def anagrams(s1, s2):
    """
    This function request two string input from the 
    user and reports whether they are anagrams.

    @params: Strings (s1, s2)
    @return: Boolean (True or False)
    """

    return sorted(s1) == sorted(s2)


def main():
    # Request user input.
    s1 = input("\nEnter first string: ")
    s1_lower = s1[:].lower()
    s2 = input("Enter second string: ")
    s2_lower = s2[:].lower()

    # Check if the supplied inputs are anagrams and 
    # display feedback.
    if anagrams(s1_lower, s2_lower):
        print(f'\n"{s1}" and "{s2}" are anagrams.')
    else:
        print(f'\n"{s1}" and "{s2}" are not anagrams.')

if __name__ == "__main__":
    main()