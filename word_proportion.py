def word_proportion(file):
    """
    This program will take a file input and count the 
    number of words that a character appeared in, then assign the word count
    to the character in a dictionary, sort by values and return list of tuples.

    @param: String - file name
    @return: List - [ls, min_val, total_words]

            ls - List of tuples(Key value pair of characters and word count)
                - [(char1, count1), (char2, count2), ...]

            min_vale(Characters with least word count) 
                - List of tuples - [(char1, count1), (char2, count2), ...]

            total_words(Total number of words) - Int
    """

    # Define variable.
    dic = dict()

    # Open file and start checking for character in words.
    with open(file) as f:
        # Parse each line in the file.
        for line in f:
            # Parse each word in line.
            for word in line.split():
                # Parse each character in word while avoiding duplicate.
                # Count word once even if character occurred twice in word. 
                for char in set(word):
                    # Check if character is an alphabet.
                    if char.isalpha():
                        # Increment word count for character.
                        dic[char.lower()] = dic.get(char, 0) + 1

    # Get the total number of words.
    total_words = sum([val for val in dic.values()])

    # Sort dic with values in ascending order.
    ls = list(sorted(dic.items(), key=lambda kv:(kv[1], kv[0])))

    # Creating a list of tuples containing character(s) with smallest word count.
    min_val = [t for t in ls if t[1] == ls[0][1]]

    # Return a list containing ls, min_val and total_words.
    return [ls, min_val, total_words]


def main():
    try:
        # Request user input.
        file = input("Enter file name: ")

        # Count words that contain each character.
        ls = word_proportion(file)
        
        # Display the table containing characters, word count and ratios.
        print("The table below contains characters, the number of words they appeared in and the ratio: ")
        print(f'\nCharacter\tWord Count\tRatio')
        for tup in ls[0]:
            print(f"{tup[0]}\t\t{tup[1]}\t\t{round(tup[1]/ls[2], 4)}")

        # Display the characters with the smallest occurrence.
        print('\nThe character(s) with the smallest word occurrence are: ')
        print(', '.join([tup[0] for tup in ls[1]]))
    except:
        print('Please, enter a valid input!')
        
if __name__ == '__main__':
    main()