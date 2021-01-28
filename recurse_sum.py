def recurse_sum():
    pass






def get_nums():
    """
    This function continuously request number input from
    user until a blank line is entered. Then, it will return a list containing 
    all the numbers entered by the user.

    @param: None
    @return: List
    """

    # Initialize variable.
    ls = list()

    # Continuously request input from user until blank line is entered.
    while True:
        num = input("Enter a number or blank line to stop: ")
        if num == "":
            break
        
        # Add the number into ls.
        ls.append(float(num))
        
    return ls


def main():
    print(get_nums())


if __name__ == '__main__':
    main()
    