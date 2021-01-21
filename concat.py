import sys

def concat(filename):
    """
    This function concatenates and displays one or more files
    whose names are provided as command line parameters.
    
    @param: Strings
    @return: None
    """
    ls = list()
    bad_files = list()

    
    for file in filename: 
        try:
            with open(file) as f:
                ls.extend(f.readlines())
        except FileNotFoundError:
            bad_files.append(file)
        ls.append('\n')

    with open('new_file.txt', 'w') as new_file:
        for line in ls:
            new_file.write(line)

    with open('new_file.txt') as f:
        for line in f:
            print(line.rstrip())
    
    return bad_files


def main():
    if len(sys.argv) < 2:
        print("Please, provide a file name!")
    else:
        filename = sys.argv[1:]
        bad_files_names = concat(filename) 
    
    print("List of invalid names provided by user:")
    for name in bad_files_names:
        print(name)

if __name__ == "__main__":
    main()