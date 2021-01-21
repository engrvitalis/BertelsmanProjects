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
        print()
        num = input("Enter a number: ")
        # print()

        if num == '':
            print(f'Total so far: {total}')
            break
        
        try:
            total += float(num)
        except ValueError:
            print()
            print("Invalid entry! Enter int or float")

        print(f'Total so far: {total}')


def main():
    sum_num()


if __name__ == "__main__":
    main()