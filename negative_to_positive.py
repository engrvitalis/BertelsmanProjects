"""
This program accepts continuous input of integers from users 
until blank line is entered. Then it will sort them in ascending order
putting into consideration their position during entry.

@param: Integer. eg. -2, 5, 0, etc.
@return: Sorted list of all the integers while preserving their order of entry.
"""

def negative_to_positive():
    # Initialize state variable.
    lst = list()
    final_list = list()

    # Read input from user and save in a list.
    while True:
        num = input("Enter an Integer: ")
        if num == "":break
        else:
            lst.append(int(num))
    
    # Go through lst and copy negative values to final_list.
    for i in lst:
        if i < 0:
            final_list.append(i)
    # Go through lst and copy zeros to final_list.
    for i in lst:
        if i == 0:
            final_list.append(i)
    # Go through lst and copy positive values to final_list.
    for i in lst:
        if i > 0:
            final_list.append(i)

    return final_list


def main():
    # Display output as per specification.
    for i in negative_to_positive():
        print(i)


if __name__ == '__main__':
    main()