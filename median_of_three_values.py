"""
This function takes three number inputs from the user 
and returns the median number.

Input: Integer
Output: String
"""

def median_value(x, y, z):
    # Return the median of three numbers.
    return sorted([x, y, z])[1]

if __name__ == "__main__":
    # Request user input.
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    num3 = int(input('Enter third number: '))

    # Call median function and display the result.
    print(f'The median value between {num1}, {num2} and {num3} is {median_value(num1, num2, num3)}')