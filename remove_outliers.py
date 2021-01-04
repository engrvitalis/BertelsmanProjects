"""
This program accepts input(List) from user and display a new
list with the two smallest and the two largest values removed.

Input: List or sequence of numbers - len(List) >= 4
       eg.: [4,3,4,5,6] or 43456
Output: List
"""


def remove_outliers(ls):
    # Create a new list and sort in ascending order.
    new_ls = ls[:]
    new_ls.sort()

    # Remove outliers as per specification.
    for i in range(2):
        new_ls.pop(0)
        new_ls.pop(-1)

    return new_ls


def main():
    # Get input from the users.
    ls = input("Enter a list of values: ")

    # Package the input as a list.
    ls = [int(i) for i in ls if i not in [',', ']', '[']]

    # Make sure the length of list is up to 4 elements else terminate program.
    if len(ls) >= 4:
        # Process the input data and display the result.
        print(f'\nProcessed list: {remove_outliers(ls)}')
        print(f'Original list: {ls}')

    else:
        print('\nInvalid Input!\nLength of list must >= 4!')


if __name__ == "__main__":
    main()