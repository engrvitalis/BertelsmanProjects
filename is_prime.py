"""
This function checks if a number is a prime number or not.

Input: Integer
Output: String
"""

def is_prime(num):
    if num == 1:
        return f'{num} is not prime.'
    
    for i in range(2, num):
        if num % i == 0:
            return f'{num} is not prime'
        
    return f'{num} is a prime'


if __name__ == "__main__":
    num = int(input("Enter an integer: "))

print(is_prime(num))