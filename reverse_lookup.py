def reverseLookup(dic, value):
    """
    This program takes two arguments, a dictionary and a value
    and tries to lookup the corresponding keys for the value.

    @param: Dictionary
            value - int, float, str etc.
    @return: list of keys.
    """

    # Initialize variable
    ls = list()

    # Search for value in dictionary and the key in a list if found.
    for k, v in dic.items():
        if v == value:
            ls.append(k)

    return ls


def create_dicts():
    """
    This program returns a list containing automatically generated
    dictionaries, ie. a list of dictionaries with the length of the 
    list being equal to num_cases.

    @param: None
    @return: List of dictionaries.
    """

    import random


    # Initialize state variables.
    num_cases = 10
    ind = 0

    # Create ls with size num_cases and pre-allocate zeros to as placeholders 
    # for the actual elements, dic.
    ls = [0 for i in range(num_cases)]

    for i in range(num_cases):

        # Initialize variables.
        dic_len = random.randrange(4, 7)
        dic = dict()

        for j in range(dic_len):
            # Generate length of proposed key.
            key_len = random.randrange(3, 5)
            # Generate list of characters with length key_len.
            key_list = [chr(random.randrange(ord('a'), ord('z'))) for i in range(key_len)]
            # Convert key_list to string to get a random key.
            key = ''.join(key_list)
            # Generate a random value.
            value = random.randrange(0, 5)
            # Populate dic with key value pair.
            if key not in dic:
                dic[key] = value
        
        # Replace the next zero placeholder with dic.
        ls[ind] = dic
        # Increment index.
        ind += 1

    # Return a list of dictionaries.
    return ls


def main():
    import random


    # Generate dictionaries for testing.
    for dic in create_dicts():
        # Generate a value and lookup the keys.
        value = random.randrange(0, 5)
        print(f'\nDict: {dic}\nValue: {value} is mapped to {reverseLookup(dic, value)} keys')

if __name__ == "__main__":
    main()