def missing_comment(file):
    """
    This function takes the name of file as input argument
    and print the file name, name of function and line number
    of any function definition that is not preceeded by a comment.

    @param: String - file
    @return: None
    """
    
    with open(file) as f:
        # Starting counter to keep track of line number
        counter = 1

        for line in f:
            # Checking if line starts with #
            if line.lstrip().startswith('#'):
                comment = True
            # Checking if line a function definition but not preceeded by comment line
            elif comment is False and line.startswith('def '):
                # Extract function name from line
                func_name = line[line.index(' ')+1:line.index('(')]

                # Print output
                print(f'\nFunction name: {func_name}')
                print(f'File name: {file}')
                print(f'Line number: {counter}')

            else:
                comment = False


            counter += 1


def main():
    # Initialize variables
    files = list()
    invalid_files = list()

    while True:
        # Request input from user until blank line is entered.
        file = input("Enter file name or blank space to end: ")
        if file == "":
            break

        # Append all file names in files
        files.append(file)
    
    # Check the content of all the files in files for functions
    # that are not immediately preceeded by a comment. 
    for file in files:
        try:
            missing_comment(file)
        except:
            # If a file name is invalid, add the name into invalid_files.
            invalid_files.append(file)

    # If there were invalid files name entry by the user, 
    # print them all out.
    if len(invalid_files) > 0:
        print("\nThese file(s) could not be accessed!:")

        for file in invalid_files:
            print(file)


if __name__ == '__main__':
    main()