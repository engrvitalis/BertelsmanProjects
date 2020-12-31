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
    num = int(num)
    new_base = int(new_base)

    # Do long division and accumulate the remainders.
    while num > 0:
        rem = num % new_base
        if rem >= 10:
            rem = chr(55 + rem) # Map to appropriate letter if remainder is less greater than 9.
        num = num // new_base
        result = str(rem) + result

    return result


def others_to_decimal(num, num_base):
    result = 0
    power = len(num) - 1

    for i in num:
        if ord('A') <= ord(i) <= ord('Z'):
            result += (ord(i) - 55) * int(num_base)**(power)
        else:
            result += int(i) * int(num_base)**(power)
        power -= 1

    return result

def main():
    print('Please enter the type of conversion to perform: ')
    print('- Enter 1 for "Decimal to other bases conversion"\n- Enter 2 for "Other bases to Decimal conversion"')
    conv_type = int(input('--> '))

    num = input("Enter number: ")
    base = input("Enter base: ")
    if 2 <= int(base) <= 16:
        if conv_type == 1:
            print(f'{num} to base 10 = {decimal_to_others(num, base)} to base {base}.')

        if conv_type == 2:
            print(f'{num} to base {base} = {others_to_decimal(num, base)} to base 10')
    else:
        print('Invalid input!\nBase must be between 2 and 16!')

if __name__ == '__main__':
    main()
    