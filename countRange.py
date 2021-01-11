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


def create_int_list(num_cases=5, min_size=3, max_size=10, start_range=-100, end_range=100):
    """
    This function a tuple of lists containing integers.

    @param: num_cases (int) - Number of list to generate.
            min_size (int) - Minimum size of list to generate.
            max_size (int) - Maximum size of list to generate.
            start_range (int) - Start of range.
            end_range(int) - End of range.
    @return: Tuple of lists containing floats with length equal to num_cases.
    """
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


def create_float_list(num_cases=5, min_size=3, max_size=10, start_range=-100, end_range=100):
    """
    This function a tuple of lists containing floats.

    @param: num_cases (int) - Number of list to generate.
            min_size (int) - Minimum size of list to generate.
            max_size (int) - Maximum size of list to generate.
            start_range (int) - Start of range.
            end_range(int) - End of range.
    @return: Tuple of lists containing floats with length equal to num_cases.
    """
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
            num = random.uniform(start_range, end_range)
            ls.append(round(num, 2))
        main_ls.append(ls)

    return tuple(main_ls)


def main():
    # Generate some lists.
    import random


    # Test for int.
    # Create series of list.
    int_t = create_int_list()
    # Initialize counter.
    # Generate the ranges of interest and count the elements inside the it.
    for l in int_t:
        while True:
            min_val = random.randrange(min(l), max(l))
            max_val = random.randrange(min(l), max(l))
            if min_val < max_val:
                break

        # Display the output.
        print(f'The range ({min_val} <= number < {max_val}) in {l} contains {countRange(l, min_val, max_val)} element(s)')

# Test for floats.
    # Create series of list.
    float_t = create_float_list()
    # Initialize counter.
    i = 0
    # Generate the ranges of interest and count the elements inside the it.
    for l in float_t:
        while True:
            min_val = random.uniform(min(l), max(l))
            max_val = random.uniform(min(l), max(l))
            if min_val < max_val:
                break
        i += 1

        # Display the output.
        print(f'The range ({round(min_val, 2)} <= number < {round(max_val, 2)}) in {l} contains {countRange(l, min_val, max_val)} element(s)')



if __name__ == "__main__":
    main()