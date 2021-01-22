def remove_comments(old_file, new_file):
    """
    This function accepts a source file and creates a copy of the
    file with the comments removed.

    @param: String - old_file: name of file to modify
            String - new_file: name of new file to create.
    @return: None
    """

    print()
    # Open old_file in read mode.
    with open(old_file, 'r') as old_fh:

        # Open new_file in write mode.
        with open(new_file, 'w') as new_fh:
            
            print(f"Creating a new file, '{new_file}' ...")
            print(f"Copying uncommented lines from '{old_file}' to '{new_file}' ...")
            print('...')
            # Go through the content of old_file line by line.
            for line in old_fh:
                # Checking for '#' on a line.
                if '#' in line:

                    # Checking lines for '#' is inside a string.
                    for char in ["'", '"']:

                        if char not in line[:line.index('#')] and char not in line[line.index('#')+1:]:
                            # Ignoring '#' that are not inside a string.
                            continue
                        else:
                            # Writing lines with # inside a string to new_file.
                            new_fh.write(line)

                else:
                    # Writing all lines without # in them to new_file.
                    new_fh.write(line)
    
    print("Done!")


def main():
    # Request input from users.
    old_file = input("Enter the name of file to be processed: ")
    new_file = input("Enter the name of new file to be created: ")

    try:
        remove_comments(old_file, new_file)
    except:
        print('Please, provide valid file names!')

if __name__ == "__main__":
    main()