import sys


def concat(filename):
    """
    This function concatenates and displays one or more files
    whose names are provided as command line parameters.
    
    @param: Strings
    @return: None
    """

    # Initialize variables.
    ls = list()
    bad_files = list()

    # Go through the file names in the list of arguments.
    for file in filename: 
        # Check for error while processing.
        try:
            # Convert the contents of file to list and append to ls.
            with open(file) as f:
                ls.extend(f.readlines())
        except FileNotFoundError:
            # Add invalid names to bad_files.
            bad_files.append(file)

        ls.append('\n')

    # Open a new file and write the contents of ls into it.
    with open('new_file.txt', 'w') as new_file:
        for line in ls:
            new_file.write(line)

    # Display the contents of new file.
    with open('new_file.txt') as f:
        for line in f:
            print(line.rstrip())
    
    # Return invalid names as list, bad_files.
    return bad_files


def main():
    # Make sure user provided at least one name to be processed.
    if len(sys.argv) < 2:
        print("Please, provide a file name!")
    else:
        # Concatenate and print the contents of the provide file names 
        # and return the invalid ones. 
        filename = sys.argv[1:]
        bad_files_names = concat(filename) 
    
    # Print the invalid names.
    print("List of invalid names provided by user:")
    for name in bad_files_names:
        print(name)

if __name__ == "__main__":
    main()