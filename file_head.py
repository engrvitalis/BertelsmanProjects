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


file_head('elements.txt')