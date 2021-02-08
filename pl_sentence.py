def pl_sentence(sentence):
    """
    This function will take a sentence as input and return 
    pig latin sentence after translation.

    @param: String
    @return: String
    """

    # Break sentence into words, convert each word to Pig latin and 
    # join them back using spaces.
    return ' '.join([pig_latin(word) for word in sentence.split()])



def pig_latin(word):
    """
    This function takes an English word as input and returns a pig latin version of 
    of the it while keeping track of the capitalized words.

    @param: str
    @return: str
    """

    # Flag capitalized words.
    capitalized = word[0].isupper()

    word = word.lower()

    # Translate words starting with vowel while keeping 
    # track of capitalized words.
    if word[0] in 'aeiou':
        if capitalized:
            return word.capitalize() + 'way'
        else:
            return word + 'way'

    # Translate words starting with consonants while keeping 
    # track of capitalized words.
    if capitalized:
        return word[1:].capitalize() + word[0] + 'ay'
    else:
        return word[1:] + word[0] + 'ay'


def main():
    # Request input from user.
    print("\nThis program translates English sentence to Pig Latin sentence.")
    sentence = input("Enter an English sentence: ")
    # Translate only if input is valid, else display error message.
    try:
        print(f'\nOriginal sentence: {sentence}')
        print(f'Pig latin sentence: {pl_sentence(sentence)}\n')
    except ValueError:
        print("Invalid entry!")


main()