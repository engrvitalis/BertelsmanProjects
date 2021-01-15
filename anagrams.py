def anagrams(s1, s2):
    """
    This function request two string input from the 
    user and reports whether they are anagrams.

    @params: Strings (s1, s2)
    @return: Boolean (True or False)
    """

    return sorted(s1.lower()) == sorted(s2.lower())


def main():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    if anagrams(s1, s2):
        print(f'\nString 1: {s1}\nString 2: {s2}\nare anagrams.')
    else:
        print(f'String 1: {s1}\nString 2: {s2}\nare not anagrams.')

if __name__ == "__main__":
    main()