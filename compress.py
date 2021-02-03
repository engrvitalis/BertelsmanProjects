def compress(data):
    '''
    This function takes a list or string argument, 
    recursively compress it using run-length algorithm and 
    return compressed list.

    @param: List or String
    @return: List
    '''

 
    if len(data) == 0:
        return []
    
    for i in range(len(data)):
        if data[i] != data[0]:
            # print(data[i:], i)
            # break
 
            return [data[0], i] + compress(data[i:])


def main():
    data = ['a', 'a', 'a', 'b', 'b', 'r', 'u']
    print(compress(data))


if __name__ == '__main__':
    main()