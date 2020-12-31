'''
This project allows the user to convert from one base to another.
It supports bases 2 through 16.

Input: Integer
Output: String
'''

def decimal_to_others(num, new_base):
    # Request for user input and initialize state variable.
    result = ''
    above_nine_rem = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14:'E', 15:'F'}

    # Do long division and accumulate the remainders.
    while num > 0:
        rem = num % new_base
        if rem >= 10:
            rem = above_nine_rem[rem] # Map to appropriate letter if remainder is less greater than 9.
        num = num // new_base
        result = str(rem) + result

    return result

def others_to_decimal(num, num_base):
    pass

def main():
    num = int(input("Enter number: "))
    base = int(input("Enter number base: "))

    print(decimal_to_others(num, base))

if __name__ == '__main__':
    main()
    