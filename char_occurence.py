def char_occurence(file):
    """
    This program will take a file input and count the 
    number of words that contains each character.

    @param: String - file name
    @return: Dictionary - with keys as character and value as 
    the number of words they are contained in.
    """

    # Define variables.
    dic = dict()
    ls = list()

    # Open file and start checking for character occurrence.
    with open(file) as f:
        for line in f:
            # print(line)
            for word in line.split():
                # ls.append(word)
                for char in set(word):
                    if char.isalpha():
                        dic[char.lower()] = dic.get(char, 0) + 1
    print(dic)


def main():
    try:
        file = input("Enter file name: ")
        print(f'File processing is complete!')
        print(f'{len(char_occurence(file)} characters found in {file}')
        print('The word count for each character is as follows:')
        print(f'Character\t')
        char_occurence(file)
    except:
        print("Invalid file name!")


if __name__ == '__main__':
    main()
