"""
This program accepts input(List) from user and display a new
list with the two smallest and the two largest values removed.
It is assumed that user will provide valid input which is list 
of numbers.

Input: List - len(List) >= 4
Output: Modified list
"""


def remove_outliers(ls):

    # Create a new copy of the list.
    new_ls = [int(i) for i in ls if i not in [',', ']', '[']]

    # Sort the list in ascending order.
    new_ls.sort()

    # Remove outliers as per specification.
    for i in range(2):
        new_ls.pop(0)
        new_ls.pop(-1)

    return new_ls


def main():
    # Get input from the users.
    ls = input("Enter a list of values: ")

    # Make sure the length of list is up to 4 elements.
    if len(ls) >= 4:
        # Process the input data and display the result.
        print(f'\nProcessed list: {remove_outliers(ls)}')
        print(f'Original list: {ls}')

    else:
        print('\nInvalid Input!\nLength of list must >= 4!')


if __name__ == "__main__":
    main()