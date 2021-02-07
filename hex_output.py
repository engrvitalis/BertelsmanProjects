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
    return sum([int(str(j), base=16) * 16**i for i, j in enumerate(reversed(hex_num))])


def main():
    print(hex_output('80e1'))


if __name__ == '__main__':
    main()