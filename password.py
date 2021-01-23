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

 
    # Open the_industrial_republic.txt file and move words that met
    # desired specification into ls.
    with open(file, 'r') as f:
        print('...\n...')
        for line in f:
            for word in line.split():
                if len(word) >= 3 and word.isalpha():
                    ls.append(word)
    print('...')
    print("Program loaded successfully!\n")
    

    option = ""
    while True:
        if option.lower() == 'q':
            break
        elif option == "":
            while True:
                word1 = random.choice(ls)
                word2 = random.choice(ls)
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