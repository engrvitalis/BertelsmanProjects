'''
Title: Parity bits
Description: This programm computes the parity bit for eight group of bits
entered by user using even parity. It is assumed that the user will provide valid input.

Input: Integer
Output: String 
'''
print("This Program will compute the parity bit for eight group of bits using even parity.")

# Declare state variable.
flag = False

# Collect and validate input.
while True:
    if flag:
        bits = input("Enter the next 8 bits: ")
    else:
        bits = input("Enter the first 8 bits or press enter to stop: ")
        flag = True
    if bits == "":break
    if len(bits) == 8:
        if bits.count('1') % 2 == 0:
            parity_bit = 0
        else:
            parity_bit = 1
        print(f'Parity bit for {bits} is {parity_bit}')
    else:
        print("Invalid number of bits!\n")