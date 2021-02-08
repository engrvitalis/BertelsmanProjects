def pl_sentence(sentence):
    """
    This function will take a sentence as input and return 
    pig latin sentence after translation.

    @param: String
    @return: String
    """

    return ' '.join([pig_latin(word) for word in sentence.split()])



def pig_latin(word):
    """
    This function takes an English word as input and returns a pig latin version of 
    of the it.

    @param: str
    @return: str
    """

    # Flag capitalized words.
    capitalized = word[0].isupper()

    word = word.lower()

    # Translate words starting with vowel.
    if word[0] in 'aeiou':

        # Translate words starting with consonants.
        if capitalized:
            return word.capitalize() + 'way'
        else:
            return word + 'way'

    # Translate words starting with consonants.
    if capitalized:
        return word[1:].capitalize() + word[0] + 'ay'
    else:
        return word[1:] + word[0] + 'ay'


def main():
    # Request input from user.
    print("\nThis program translates English sentence to Pig Latin sentence.")
    sentence = 'This is the town of Eggs' #input("Enter an English sentence: ")
    # Translate only if input is valid, else display error message.
    try:
        print(f'Original sentence: {sentence}')
        print(f'Pig latin sentence: {pl_sentence(sentence)}\n')
    except ValueError:
        print("Invalid entry!")


main()