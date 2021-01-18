def file_head(filename):
    """
    This function prints the first ten lines 
    in a file.

    @param: String - filename
    @return: None
    """

    # Initialize variable.
    i = 1

    # Go through the file and print first 10 lines.
    with open(filename) as file:
        for line in file:
            if i <= 10:
                print(line, end='')
            i += 1


def main():
    # Request input from user
    filename = input("Enter file name: ")

    # Check if file name was provided by user and 
    # display error message otherwise.
    if filename == "":
        print("File name was not provided!")
    else:
        try:
            print()
            # Display first ten lines on the file.
            file_head(filename)
        except:
            # Display error message for wrong file name.
            print("Invalid file name!")


if __name__ == "__main__":
    main()