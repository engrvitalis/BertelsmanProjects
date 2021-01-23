def password(file):
    """
    This function will generate and print two 2 worded password.
    Please note that a word file name must be assigned to variable called file
    in the main function before the program is run.

    @param: None
    @return: None
    """

    import random


    # Declare variable.
    ls = list()

    # Give user loading commencement feedback.
    print("Loading ...")

 
    # Open text file and move words that met desired specification into ls.
    with open(file, 'r') as f:
        print('...\n...')
        for line in f:
            for word in line.split():
                if len(word) >= 3 and word.isalpha():
                    ls.append(word)
    print('...')
    print("Program loaded successfully!\n")
    
    # Initialize options variable
    option = ""

    while True:
        # Quit if the user enters 'q'.
        if option.lower() == 'q':
            break
        # If return is hit instead, generate the password.
        elif option == "":
            while True:
                # Generate 2 random words from word list.
                word1 = random.choice(ls)   
                word2 = random.choice(ls)
                # if the numbers are the same or their lengths combined
                # is not between 8 and 10, continue, else concatenate.
                if word1 == word2 or not 8 <= len(word1 + word2) <= 10:
                    continue
                else:
                    print(f'Password: {word1.capitalize() + word2.capitalize()}')
                    print()
                    break

        option = input("Hit return to generate a new password or enter 'q' to end.: ")


def main():
    # Replace word2.txt with the any text file name.
    file = 'words2.txt'
    # Generate password.
    password(file)

if __name__ == '__main__':
    main()