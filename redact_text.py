def redact_text(file, new_file, sensitive_file):
    """
    This program takes as parameters, name of file to redact, 
    the name of new file to return and the name of the file containing 
    sensitive information to remove.
    It will read the file provided, shield the sensitive words in the file, create
    a new file with the name provided, and write the processed content of the 
    the original file in it.

    @param: file - original file name
            new_file - name of file to return
            sensitive_file - name of file containing sensitive words.
    @return: None
    """

    # Initialize variable.
    sensitive_list = list()

    # Open sensitive_file.
    with open(sensitive_file) as f:
        # Parse the line
        for line in f:
            # Split line by words and add into sensitive_list.
            for word in line.split():
                # Strip word of any special character to the right of it.
                word = get_word(word)

                if word != "":
                    sensitive_list.append(word.lower().strip())

    # Open original file.
    with open(file) as in_file:
        # Create new file.
        with open(new_file, 'w') as out_file:

            # Parse the line, shielding sensitive words and write to new file.
            for line in in_file:
                for word in sensitive_list:
                    line = line.replace(word.lower(), '*' * len(word))
                out_file.write(line)


def get_word(word):
    """
    This function strips all special characters to the right of the
    argument and returns the clean word.

    @param: String - word
    @return String
    """

    # Recursively remove special character to the right of word
    # and return any remaining alpha numeric character.
    if word == "" or word[-1].isalpha() or word[-1].isdigit():
        return word
    return get_word(word[:-1])


def main():
    # Display instructions to the user.
    print()
    print("You are about to Redact a document!")
    print("To proceed, enter the name of the document to redact, the new file name to return and")
    print("the file containing sensitive words.")
    print()

    # Request input from user.
    file = input("Enter name of file to redact: ")
    new_file = input("Enter name of new file: ")
    sensitive_words = input("Enter sensitive words file name: ")

    try:
        # Redact a document and create a new file.
        redact_text(file, new_file, sensitive_words)
    except:
        print("Please, enter valid input!")
        quit()

if __name__ == '__main__':
    main()
    