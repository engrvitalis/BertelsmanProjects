"""
This project takes two positive integers as numerator and denominator of a fraction
as its only parameters and reduce the fraction to the lowest terms and return them.
"""

def reduce_fraction(numerator, denominator):
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
    x = int(input("Enter the numerator: "))
    y = int(input("Enter the denominator: "))

    print(reduce_fraction(x, y))

if __name__ == '__main__':
    main()