def pig_latin(word):
    """
    This function takes an English word as input and returns a pig latin version of 
    of the it.

    @param: str
    @return: str
    """

    # Translate words starting with vowel.
    if word[0] in 'aeiou':
        return word + 'way'

    # Translate words starting with non-vowel character.
    return word[1:] + word[0] + 'ay'


def main():
    print("\nThis program translates English words to pig latin.")
    word = input("Enter an English word: ")
    try:
        print(f"The pig latin version of '{word}' is '{pig_latin(word.lower())}'")
    except ValueError:
        print("Invalid entry!")


main()