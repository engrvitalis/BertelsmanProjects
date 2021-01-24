def password(file):
    """
    This function will generate and print two 2 worded password.
    The user will provide the word text file to be read by the function.

    @param: None
    @return: None
    """

    import random


    # Declare variable.
    word_list = list()
    used_passwords = list()

    

 
    # Open text file and move words that met desired specification into ls.
    with open(file, 'r') as f:
        # Give user loading commencement feedback.
        print("Loading ...")
        print('...\n...')

        for line in f:
            for word in line.split():
                if len(word) >= 3 and word.isalpha():
                    word_list.append(word)
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
                word1 = random.choice(word_list)   
                word2 = random.choice(word_list)
                # if the numbers are the same or their lengths combined
                # is not between 8 and 10, continue, else concatenate.
                if word1 == word2 or not 8 <= len(word1 + word2) <= 10:
                    continue
                else:
                    pas = word1.capitalize() + word2.capitalize()
                    # Making sure there is no password duplicates per session.
                    if pas.lower() in used_passwords:
                        continue
                    else:
                        used_passwords.append(pas.lower())
                        print(f'Password: {pas}')
                        print()
                        break

        option = input("Hit return to generate a new password or enter 'q' to end: ")


def main():
    # Request input from user.
    file = input("\nEnter word file name: ")
    try:
        # Generate password.
        password(file)
    except:
        print("Enter valid file name!")

if __name__ == '__main__':
    main()