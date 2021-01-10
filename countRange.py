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

    # print(f'List: {ls} | Min: {min_value} | Max: {max_value}')

    return count


def validate_number(num):
    """
    Validate number input from user.

    @param: String eg. '3', '2.3' etc.
    @return Boolean eg. (True, 'integer', int(num)), (True, 'float', float(num)) or False.
    """

    try:
        return (True, 'integer', int(num))
    except ValueError:
        try:
            return (True, 'float', float(num))
        except ValueError:
            return False



def main():
    # Initialize state variables.
    ls = list()

    # Request and Validate Input of number(s) from user.
    while True:
        num = input('Enter a number or blank line to stop): ')
        if num == '':
            break
        else:
            if validate_number(num)[1] == 'integer':
                ls.append(int(num))
            elif validate_number(num)[1] == 'float':
                ls.append(float(num))
            else:
                print("Invalid number. Please enter a float or int!")
                continue
    
    print()
    # Continue only if user provided at least one valid numbers to process.
    if len(ls) != 0:
        # Request and Validate input values.
        while True:
            min_value = input("Provide a minimum value to define a range: ")
            max_value = input("Provide a maximum value to define a range: ")
            # Check for min_value == max_value senario.
            if min_value != '' and max_value != '' and min_value == max_value:
                print(f'Minimum value cannot be equal to Maximum value: Min = {min_value}; Max = {max_value}')
                continue
            # Validate minimum value.
            if min_value != "":
                if validate_number(min_value)[1] == 'integer':
                    min_value = int(min_value)
                elif validate_number(min_value)[1] == 'float':
                    min_value = float(min_value)
                else:
                    print("Your minimum value is not a number! Please, re-enter values!")
                    continue
            # Validate maximum value.
            if max_value != "":
                if validate_number(max_value)[1] == 'integer':
                    max_value = int(max_value)
                    print(f'max1: {max_value}')
                elif validate_number(max_value)[1] == 'float':
                    max_value = float(max_value)
                    print(f'float: {max_value}')
                else:
                    print("Your maximum value is not a number! Please, re-enter values!")
                    continue

            break
        
        # Continue if there is valid data to process.
        if len(ls) != 0:
            # Set default values incase of blank line entry by user
            # for minimum or maximum values or both.
            if min_value == "" and max_value == "":
                min_value = min(ls)
                # max_value = max(ls) + 1
            elif min_value == "":
                min_value = min(ls)
            else:
                max_value = max(ls)
            print(f'Min: {min_value}, Max: {max_value}, List: {ls}')
            # Count values based on the minimum and maximum values.
            print(countRange(ls, min_value, max_value))

if __name__ == "__main__":
    # main()
    # print(countRange([2.2, 3.5, 2, 5, 7.1, 8], 2, 7.1))
    # print(validate_number('l'))