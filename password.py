def password(file):
    """
    This function will generate and print two 2 worded password.
    Please note that a word file name must be assigned to variable called file
    in the main function before the program is run.

    @param: None
    @return: None
    """

    # Declare variable.
    ls = list()

    # Give user loading commencement feedback.
    print("Loading ...")

 
    # Open the_industrial_republic.txt file and move words that met
    # desired specification into ls.
    with open(file, 'r') as f:
        for line in f:
            for word in line.split():
                if len(word) >= 3 and word.isalpha():
                    ls.append(word)
    print("Program loaded successfully!")
    print(ls[:20])

    


def main():
    file = 'words.txt'
    password(file)

if __name__ == '__main__':
    main()