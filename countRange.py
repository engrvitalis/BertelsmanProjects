def countRange(ls, min_value, max_value):
    """
    Description:
             This program will count the number within the range: 
             min_value <= number < max_value

    @params: List - The parameter to be processed. eg. [2,3,4]
             Integer or float - min_value(Minimum value of the range).
             Integer or float - max_value(Maximum value of the range).
    @return: Integer - Elements count from and including min_value
             and up to but excluding max_value.
             ie. min_value <= number < max_value.
    """

    # Initialize counter
    count = 0

    # Move through the list and increment counter if
    # number is within specified range.
    for num in ls:
        if min_value <= num < max_value:
            count += 1

    return count

def create_list(num_cases=10, min_size=3, max_size=10, start_range=-100, end_range=100):
    # Generating several test cases.
    import random

    # Initialize state variables.
    main_ls = list()

    # Generate random list with minimum and maximum values
    # and run test.
    for i in range(num_cases):
        # Initialize variables.
        ls = list()
        list_size = random.randrange(min_size, max_size)

        # Create list for test.
        for j in range(list_size):
            num = random.randrange(start_range, end_range)
            ls.append(num)
        main_ls.append(ls)

    return tuple(main_ls)


def main():
    # Generate some lists.
    import random


    t = create_list()
    for l in t:
        while True:
            min_val = random.randrange(min(l), max(l))
            max_val = random.randrange(min(l), max(l))
            if min_val < max_val:
                break
        
        print(f'The range ({min_val} <= number < {max_val}) in {l} contains {countRange(l, min_val, max_val)} element(s).')



        



if __name__ == "__main__":
    main()