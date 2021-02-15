def most_repeating_letter_count(word):
    """
    This program will take a single word and  return 
    the most frequent character therein.

    @param: str - word
    @return: 
    """
    from collections import Counter
    
    # Return the most common word count
    return Counter(word).most_common(1)[0][1]



def most_repeating_word(words):
    """
    This function takes words as argument and return the 
    word which contains the most frequent character other 
    available words.

    @param: str - words
    @return: str
    """

    # Return the word with the most common character
    return max(words,key=most_repeating_letter_count)


def main():
    while True:
        words = input("Enter words or blank line to quit: ")
        if not words:
            break
        # Display the word with the most common character
        print(f'The word with most common character is "{most_repeating_word(words.lower().split())}"')


main()