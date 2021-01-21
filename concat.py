import sys

def concat(filename):
    """
    This function concatenates and displays one or more files
    whose names are provided as command line parameters.
    
    @param: Strings
    @return: None
    """
    ls = list()
    
    for file in sys.argv: 
        with open(file) as f:
            ls.extend(f.readlines())
        ls.append('\n')

    with open('new_file.txt', 'w') as new_file:
        for line in ls:
            new_file.write(line)

    with open('new_file.txt') as f:
        for line in f:
            print(line.rstrip())


def main():
    try: 
        filename = sys.argv[1]
        concat(filename) 

    except FileNotFoundError:
        print("File not found!")

    except IndexError:
        print("Please, provide a file name!")



if __name__ == "__main__":
    main()