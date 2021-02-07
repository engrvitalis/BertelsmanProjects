def pig_latin(word):
    """
    This function takes an English word as input and returns a pig latin version of 
    of the it.

    @param: str
    @return: str
    """

    if word[0] in 'aeiou':
        return word + 'way'

    return word[1:] + word[0] + 'ay'


def main():
    print("\nThis program translates English words to pig latin.")
    word = input("Enter an English word: ")
    try:
        print(f"The pig latin version of '{word}' is {pig_latin(word)}")
    except ValueError:
        print("Invalid entry!")