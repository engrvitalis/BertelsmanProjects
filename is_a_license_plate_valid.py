"""
This project receives an input from the user and classifies it as 
either old style plate number, new style plate number or invalid number

Input: String
Output: String
"""

plate_num = input("Enter license plate number: ")

if len(plate_num) == 6 and plate_num[-3:].isnumeric() and plate_num[:4].isupper():
    print('Number is valid old style license plate')
elif len(plate_num) == 8 and plate_num[:4].isnumeric() and plate_num[5:].isupper():
    print('Number is valid new style license plate')
else:
    print('Invalid number')