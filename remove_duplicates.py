"""
This program reads words from user until the user enters
a blank line.

@param: words(String). To enter the next word, hit return after the first.
        To stop data entry, hit return twice after the last word.
@return: The list of words entered in the same sequence they were entered 
         without duplicates.
"""

def remove_duplicates():
    list_of_words = list()

    while True:
        word = input("Enter a word or hit return to terminate: ")
        if word == '':break
        elif word not in list_of_words:
            list_of_words.append(word)

    return list_of_words

def main():
    # Display the output
    words = remove_duplicates()
    print()
    for word in words:
        print(word)


if __name__ == '__main__':
    main()