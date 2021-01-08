"""
This program will generate six random number between 1 and 49
in ascending order without repetition.

@param: None
@return: Six integers arranged in ascending order.
"""

def num_generator():
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

    return ls


def main():
    # Display the output as per specification.
    for num in num_generator():
        print(num, end=' ')


if __name__ == '__main__':
    main()

