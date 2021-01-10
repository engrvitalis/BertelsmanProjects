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
        if min_value <= num < max_value:
            count += 1

    return count


def validate_number(num):
    """
    Validate number input from user.
    """


def main():
    # Initialize state variables.
    ls = list()

    # Request and Validate Input of number(s) from user.
    while True:
        num = input('Enter a number or blank line to stop): ')
        if num == '':
            break
        try:
            ls.append(int(num))
        except ValueError:
            try:
                ls.append(float(num))
            except ValueError:
                print("You can only enter an int or a float!")
    
    print()
    # Continue only if user provided at least one valid numbers to process.
    if len(ls) != 0:
        # Request and Validate input of minimum and maximum values.
        while True:
            min_value = input("Provide a minimum value to define a range: ")
            max_value = input("Provide a maximum value to define a range: ")
            if min_value != "":
                try:
                    min_value = int(min_value)
                except ValueError:
                    try:
                        min_value = float(min_value)
                    except ValueError:
                        print("Enter either integer or float!")
                        continue

            if max_value != "":
                try:
                    max_value = float(max_value)
                except ValueError:
                    try:
                        max_value = float(max_value)
                    except ValueError:
                        print("Enter either integer or float!")
                        continue

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
                print(type(max_value), max_value)
                max_value += 1
            if max_value == "":
                max_value = max(ls) + 1

            print(f'Min: {min_value}, Max: {max_value}, List: {ls}')
            # Count values based on the minimum and maximum values.
            print(countRange(ls, min_value, max_value))

if __name__ == "__main__":
    main()