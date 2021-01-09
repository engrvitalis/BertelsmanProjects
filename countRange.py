def countRange(lst, min_value, max_value):
    """
    Description:
             This program will count the number within the range: 
             min_value <= number < max_value

             If min_value and max_value were not provided, it will return the 
             length of the list. 
             If only max_value was provided, it will count all numbers within 
             the range: number < max_value.
             if only min_value was provided, it will count all numbers within 
             the range: min_value <= number.

    @params: List - The parameter to be processed. eg. [2,3,4]
             Integer or float - min_value(Minimum value of the range).
             Integer or float - max_value(Maximum value of the range).
    @return: Integer - Elements count from and including min_value
             and up to but excluding max_value.
             ie. min_value <= element < max_value.
    """

    # Initialize counter
    count = 0

    # Move through the list and increment counter if
    # number is within specified range.
    for num in lst:
        if int(min_value) <= num < int(max_value):
            count += 1

    return count


def main():
    # Initialize state variables.
    ls = list()

    # Request user to provide list of numbers, reject invalid inputs
    # and collect the good inputs in ls.
    while True:
        num = input('Enter a number or blank line to stop): ')
        if num == '':
            break
        elif num.isdigit():
            ls.append(int(num))
        else:
            print('You can only enter an int or a float!')
            continue
    
    print()
    # Request user to provide minimum and maximum values.
    if len(ls) != 0:
        while True:
            min_value = input("Provide a minimum value to define a range: ")
            max_value = input("Provide a maximum value to define a range: ")
            if min_value == '' or max_value == '':
                break
            else:
                if not min_value.isdigit():
                    print("Minimum value must be a number!")
                    continue
                if not max_value.isdigit():
                    print("Maximum value must be a number!")
            break
        
        # Make sure you have data to process.
        if len(ls) != 0:
            # Set default values incase of blank line entry by user
            # for minimum or maximum values or both.
            if min_value == "" and max_value == "":
                min_value = min(ls)
                max_value = max(ls) + 1
            if min_value == "":
                min_value = min(ls)
            if max_value == "":
                max_value = max(ls)

            # Count values based on the minimum and maximum values.
            print(countRange(ls, min_value, max_value))

if __name__ == "__main__":
    main()