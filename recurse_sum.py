def recurse_sum():
    """
    This function sums request number input from user and 
    sums them recursively.

    @param: None
    @return: Float - Total sum of the numbers.
    """

    # Request input from the user.
    num = input("Enter a number or blank line to stop: ")

    # Return total if the user enters blank line.
    if num == "":
        return 0.0
    else:
        # Recursively sum numbers.
        return float(num) + recurse_sum()


def main():
    try:
        # Recursively sum numbers and display the total.
        print(f'\nTotal: {recurse_sum()}')
    except:
        print("\nLast input was invalid! All values must be float or int! ")

if __name__ == '__main__':
    main()
    