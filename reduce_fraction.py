"""
This project takes two positive integers as numerator and denominator of a fraction
as its only parameters and reduce the fraction to the lowest terms and return them.
"""

def reduce_fraction(numerator, denominator):
    numerator = int(numerator)
    denominator = int(denominator)
    divisor = min(numerator, denominator)

    for i in range(divisor):
        if numerator % divisor == 0 and denominator % divisor == 0:
            numerator = numerator // divisor
            denominator = denominator // divisor
            divisor -= 1
        else:
            divisor -= 1
    
    return numerator, denominator

def main():
    print("Enter the fraction to reduce")
    x = input("Enter the numerator: ")
    y = input("Enter the denominator: ")

    print("\nReduced fraction:")
    print(f'{reduce_fraction(x, y)[0]}/{reduce_fraction(x, y)[1]}')

if __name__ == '__main__':
    main()