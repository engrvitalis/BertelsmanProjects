def hex_output(hex_num):
    """
    This function will take a hexadecimal number input
    from the user and convert it to decimal.

    @param: str
    @return: int

    eg:
        hex_output(50) --> 80
            Conversion procedure:
                0 * 16**0 + 5 * 16**1 = 80

        hex_output('80E1') --> 32993
            Conversion procedure:
                1 * 16**0 + 14 * 16**1 + 0 * 16**2 + 8 * 16**3 = 32993
    """
    # Iterate over each character of the reversed hex_num string,
    # convert to decimal and sum all.
    return sum([int(j, base=16) * 16**i for i, j in enumerate(reversed(hex_num))])


def main():
    # Request hexadecimal number from user and return decimal equivalent.
    
    print("\nConvert hexadecimal number to decimal.")
    # Continuously request input from user, process it and exit if blank 
    # line is entered.
    while True:
        num = input("Enter a hexadecimal number or blank line to exit: ")
        if not num:
            break

        # Trap invalid entries.
        try:
            print(f"Decimal equivalent of '{num}' is {hex_output(num)}\n")
        except ValueError:
            print("Invalid number!\n")

if __name__ == '__main__':
    main()