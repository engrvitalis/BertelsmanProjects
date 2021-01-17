def scrabble_score(word):
    """
    This function takes a word and return the full score
    based on scrabble rules. It is assumed that the user
    will enter valid English word.

    @param: String - word
    @return: Integer
    """

    # Generate the points for all the characters in word 
    # and return the sum.
    return sum([char_score(s) for s in word])


def char_score(s):
    """
    This function takes a character and returns the score
    attached to the character based on scrabble rules.

    @param: String - s
    @return: Integer
    """

    # Mapping points to each English alphabet as  
    # per scrabble rules.
    score = {
        "a": 1, "e": 1, "i": 1, "l": 1, "o": 1, 
        "n": 1, "s": 1, "r": 1, "u": 1, "t": 1, 
        "d": 2, "g": 2, "c": 3, "b": 3, "m": 3, 
        "p": 3, "f": 4,  "h": 4, "w": 4, "v": 4, 
        "y": 4, "k": 5, "j": 8,  "x": 8, "q": 10, 
        "z": 10
        }

    # Lookup score for character and return.
    return score[s]
             
          
def main():
    # Request input from user.
    word = input("\nEnter a word: ")
    # Convert word to lowercase for uniformity.
    word_lower = word.lower()

    # Calculate and display word score.
    print(f'The word "{word}" scores {scrabble_score(word_lower)} points')

if __name__ == "__main__":
    main()