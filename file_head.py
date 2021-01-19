import sys

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
    try: 
        filename = sys.argv[1]
        file_head(filename) 

    except FileNotFoundError:
        print("File not found!")

    except IndexError:
        print("Please, provide a file name!")


if __name__ == "__main__":
    main()