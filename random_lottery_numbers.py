def lottery_numbers():
    """
    This function will generate six random numbers between 1 and 49
    in ascending order without repetition.

    @param: None
    @return: A list of six integers.
    """

    # import relevant modules.
    import random


    # Initialize state variables.
    ls = list()

    # Generate random numbers between 1 and 49  
    # without duplicates and collect all in ls.
    while len(ls) < 6:
        num = random.randrange(1, 50)
        if num in ls:
            continue
        else:
            ls.append(num)
    ls.sort()

    return ls


def main():
    # Generate six random integers with repetition and 
    # display the output on a single line separated by spaces.
    print()
    for num in lottery_numbers():
        print(num, end=' ')


if __name__ == '__main__':
    main()

