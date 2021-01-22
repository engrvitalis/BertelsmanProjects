def remove_comments(old_file, new_file):
    """
    This function accepts a source file and creates a copy of the
    file with the comments removed.

    @param: String - old_file: name of file to modify
            String - new_file: name of new file to create.
    @return: None
    """

    # Declare variable.
    

    with open(old_file, 'r') as old_fh:
        for line in old_fh:
            # Checking for # on a line.
            if '#' in line:
                # print(line, end='')
                # Checking if # is inside a string.
                for char in ["'", '"']:
                    if char not in line[:line.index('#')] and char not in line[line.index('#')+1:]:
                        # Ignoring # that are inside a string.
                        # print(line, end='')
                        continue
                    else:
                        # Getting # inside a string.
                        print(line, end='')
            else:
                # Getting all lines without # in them.
                print(line, end='')


def main():
    print(remove_comments('elements2.txt', 'elements2_copy.txt'))


if __name__ == "__main__":
    main()