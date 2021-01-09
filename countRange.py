def countRange(lst, min_value, max_value):
    """
    This program will return the total number of elements within a 
    particular range in a list.

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


def main():
    # Initialize state variables.
    ls = list()
    min_value = None
    max_value = None

    # Request user to provide list of numbers and save it in a list.
    while True:
        num = input('Enter a number or blank line to stop): ')
        if num == '':
            break
        elif num.isdigit():
            ls.append(int(num))
        else:
            print('You can only enter an int or a float!')
            continue

    # Request user to provide minimum and maximum values.
    # min_value = input