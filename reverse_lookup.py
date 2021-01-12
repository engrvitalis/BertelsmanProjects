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

    for k, v in dic.items():
        if v == value:
            ls.append(k)

    return ls


def create_dict():
    import random


    ls = list()
    num_cases = 10

    for i in range(num_cases):
        dic_len = random.randrange(2, 10)
        dic = dict()
        for j in range(dic_len):
            key_len = random.randrange(3, 5)
            key_list = [chr(random.randrange(ord('a'), ord('z'))) for i in range(key_len)]
            key = ''.join(key_list)
            value = random.randrange(0, 20)
            if key not in dic:
                dic[key] = value

        ls.append(dic)

    return ls





def main():
    print(create_dict())
    # print(reverseLookup({'me': 4, 'you': 6, 'i': 7, 'jjs': 7}, 8))

if __name__ == "__main__":
    main()