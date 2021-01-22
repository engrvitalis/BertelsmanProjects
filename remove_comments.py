def remove_comments(old_file, new_file):
    """
    This function accepts a source file and creates a copy of the
    file with the comments removed.

    @param: String - old_file: name of file to modify
            String - new_file: name of new file to create.
    @return: None
    """

    with open(old_file, 'r') as old_fh:
        for line in old_fh:
            print(line, end='')


def main():
    print(remove_comments('elements2.txt', 'elements2_copy.txt'))


if __name__ == "__main__":
    main()