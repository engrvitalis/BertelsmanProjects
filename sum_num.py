def sum_num():
    """
    This function constantly request input of number from 
    user and displays the total of all the numbers entered so far
    while ignoring invalid entry.

    @param: Int or Float
    @return: Int or Float
    """

    # Initialize variable
    total = 0

    while True:
        print()
        num = input("Enter a number: ") # Request input from user.
        # print()

        # Exit and print total so far if blank line is entered.
        if num == '':
            print(f'Total so far: {total}')
            break
        
        # Check for invalid number.
        try:
            total += float(num) # Accumulate sum of numbers.
        except ValueError:
            print()

            # Incase of invalid entry, print relevant message.
            print("Invalid entry. Enter int or float!")

        # Continuously print total irrespective of input condition.
        print(f'Total so far: {total}')


def main():
    # Continuously sum up series of numbers entered by the user
    # and display the total.
    sum_num()


if __name__ == "__main__":
    main()