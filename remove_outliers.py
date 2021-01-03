"""
This program accepts input(List) from user and display a new
list with the two smallest and the two largest values removed.
It is assumed that user will provide valid input which is list 
of numbers.

Input: List - len(List) >= 4
Output: Modified list
"""


def remove_outliers(ls):
    new_ls = ls[:]

    new_ls.sort()
    print(new_ls)
    for i in range(2):
        new_ls.pop(0)
        new_ls.pop(-1)

    return new_ls


def main():
    # Get input from the users.
    # ls = list(input("Enter a list of values: "))
    ls = [3,4,5,5,6]

    if len(ls) >= 4:
        # Process the input data and display the result.
        print(f'\nProcessed list: {remove_outliers(ls)}')
        print(f'Original list: {ls}')

    else:
        print('\nInvalid Input!\nLength of list must >= 4!')


if __name__ == "__main__":
    main()