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

    # Open file and start checking for character occurrence.
    with open(file) as f:
        for line in f:
            # print(line)
            for word in line.split():
                # ls.append(word)
                for char in set(word):
                    if char.isalpha():
                        dic[char.lower()] = dic.get(char, 0) + 1

    # Get the total number of words.
    total_words = sum([val for val in dic.values()])

    # Sort dic with values in ascending order.
    ls = list(sorted(dic.items(), key=lambda kv:(kv[1], kv[0])))

    # Creating a list of tuples containing characters with smallest word count.
    min_val = [t for t in ls if t[1] == ls[0][1]]

    # Return a list containing ls, min_val and total_words.
    return [ls, min_val, total_words]


def main():
    file = "gatsby.txt"

    ls = word_proportion(file)

    # print(f'{char_occurence(file)}')
    
    print(f'\nCharacter\tWord Count\tRatio')
    for tup in ls[0]:
        print(f"{tup[0]}\t\t{tup[1]}\t\t{round(tup[1]/ls[2], 4)}")

    # Display the characters with the smallest occurrence.
    print('\nThe character(s) with the smallest word occurrence are: ')
    print(', '.join([tup[0] for tup in ls[1]]))
        


if __name__ == '__main__':
    main()
