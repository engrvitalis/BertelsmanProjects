'''
This project converts a number to in base 10 to base 2.

Input: Integer
Output: String
'''
print()
print("This program converts base 10 integers to base 2")
print("Please enter an integer below:")
q = int(input("--> "))
q_copy = q
result = ''

while q > 0:
    r = q % 2
    q = q // 2
    result = str(r) + result

print(f'Base 2 of {q_copy} is {result}')


