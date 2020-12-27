'''
This project converts a number to in base 10 to base 2.

Input: Integer
Output: String
'''
# Request for user input and initialize state variables.
print()
print("This program converts base 10 integers to base 2")
print("Please enter an integer below:")
q = int(input("--> "))
q_copy = q
result = ''

# Do long division and accumulate the remainders.
while q > 0:
    r = q % 2
    q = q // 2
    result = str(r) + result

# Diplay the result
print(f'Base 2 of {q_copy} is {result}')


