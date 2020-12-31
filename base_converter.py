'''
This project allows the user to convert from one base to another.
It supports bases 2 through 16.

Input: Integer
Output: String
'''

def decimal_to_others(num, new_base):
    """
    This function converts numbers from decimal to bases 2 through 16.

    Input: Integer
    Output: String
    """

    # Request for user input and initialize state variable.
    result = ''

    # Do long division and accumulate the remainders.
    if 2 <= new_base <= 16:
        while num > 0:
            rem = num % new_base
            if rem >= 10:
                rem = chr(55 + rem) # Map to appropriate letter if remainder is less greater than 9.
            num = num // new_base
            result = str(rem) + result

        return result
    else:
        print("Base must be between 2 and 16!")
        return -1

def others_to_decimal(num, num_base):
    pass

def main():
    num = int(input("Enter number: "))
    base = int(input("Enter number base: "))

    print(decimal_to_others(num, base))

if __name__ == '__main__':
    main()
    