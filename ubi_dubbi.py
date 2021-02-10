def ubi_dubbi(word):
    """
    This function takes a string (word) as argument and 
    returns Ubi Dubbi translation of the word.

    @param: str - word
    @return: str
    """

    return ''.join(['ub'+char if char in 'aeiou' else char for char in word.lower()])


def main():
    print("Translate a word to Ubi Dubbi!")
    word = input("Enter a word: ")
    print(ubi_dubbi(word))


if __name__ == '__main__':
    main()