def missing_comment(file):
    """
    This function takes the name of file as input argument
    and print the file name, name of function and line number
    of any function definition that is not preceeded by a comment.

    @param: String - file
    @return: None
    """

    with open(file) as f:
        counter = 1

        for line in f:
            if line.lstrip().startswith('#'):
                comment = True
            elif comment is False and line.startswith('def '):
                func_name = line[line.index(' ')+1:line.index('(')]
                print(f'\nFunction name: {func_name}')
                print(f'File name: {file}')
                print(f'Line number: {counter}')

            else:
                comment = False


            counter += 1


def main():
    files = list()
    invalid_files = list()

    while True:
        file = input("Enter file name or blank space to end: ")
        if file == "":break
        files.append(file)
    
    for file in files:
        try:
            missing_comment(file)
        except:
            invalid_files.append(file)

    if len(invalid_files) > 0:
        print("\nThese file(s) could not be accessed!:")

        for file in invalid_files:
            print(file)


if __name__ == '__main__':
    main()