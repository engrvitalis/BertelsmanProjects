import sys

def concat(filename):
    """
    This function concatenates and displays one or more files
    whose names are provided as command line parameters.
    @param: Strings
    @return: None
    """

    
    for file in sys.argv: 
        with open(file) as f_handle:
            for f in f_handle:
                print(f_handle.readline(), end='')


def main():
    filename = sys.argv[1:]
    concat(filename)


if __name__ == "__main__":
    main()
