def sum_num():
    """
    This function constantly request input of number from 
    user and displays the total of all the numbers entered so far
    while ignoring invalid entry.

    @param: Int or Float
    @return: Int or Float
    """

    total = 0

    while True:
        num = input("Enter a number: ")

        if num == '':
            print(total)
            break
        
        
        print(total += float(num))


def main():
    sum_num()


if __name__ == "__main__":
    main()