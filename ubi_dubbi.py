def ubi_dubbi(word):
    """
    This function takes a string (word) as argument and 
    returns Ubi Dubbi translation of the word.

    @param: str - word
    @return: str
    """

    return [char for char in word]


def main():
    word = 'Program'
    print(ubi_dubbi(word))


if __name__ == '__main__':
    main()