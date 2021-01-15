def anagrams(s1, s2):
    """
    This function request two string input from the 
    user and reports whether they are anagrams.

    @params: Strings (s1, s2)
    @return: Boolean (True or False)
    """

    return sorted(s1.lower()) == sorted(s2.lower())


def main():
    pass