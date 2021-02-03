def compress(data):
    '''
    This function takes sequence of characters as argument, 
    recursively compress them using run-length algorithm and 
    return a compressed list.

    @param: All types
    @return: List
    '''

    # Initialize variable.
    ls = []

    # Go through the characters.
    for i in range(len(data)):
        # Check if character is different from the first one
        # on the list.
        if data[i] != data[0]:
            # Add the first character on the list with its 
            # number of occurrence to ls.
            ls.extend([data[0], i])
            # Remove counted character from data and recursively call 
            # function with the new data.
            return ls + compress(data[i:])

    # Count and add the last similar character in data into ls.
    ls.extend([data[0], len(data)])

    return ls


def main():
    # Initialize variable.
    data = list()
    # Request input from user.
    while True:
        inp = input("Please, enter an input or blank line to stop: ")
        if inp == "":
            break
        
        # Add all user input into data.
        data.append(inp)
    
    # Guard against blank line entry and display output.
    if len(data) != 0:
        print(f'\nOriginal Data:\n{data}\n')
        print(f'\nCompressed Data:\n{compress(data)}')


if __name__ == '__main__':
    main()