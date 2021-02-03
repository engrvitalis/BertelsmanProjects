def compress(data):
    '''
    This function takes a list or string argument, 
    recursively compress it using run-length algorithm and 
    return compressed list.

    @param: List or String
    @return: List
    '''

    ls = []
    if len(data) == 0:
        return ls
    else:
        for i in range(len(data)):
            if data[i] != data[0]:
                ls.extend([data[0], i])
                return ls + compress(data[i:])
        ls.extend([data[0], len(data)])
        return ls


def main():
    data = list()
    while True:
        inp = input("Please, enter an input or blank line to stop: ")
        if inp == "":
            break

        data.append(inp)
    
    print(f'\nOriginal Data:\n{data}\n')
    print(f'\nCompressed Data:\n{compress(data)}')


if __name__ == '__main__':
    main()