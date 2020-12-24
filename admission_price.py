"""
Project Name: Admission price
Description: This project determines the admission price into a zoo 
based on age of the customer.
Input: Age - Integer
Output: Price for each age bracket - String
"""

group_age_list = []
flag = False
total_amount = 0

while True:
    if flag:
        age = input("Enter the next guest age: ")
    else:
        age = input("Enter guest age: ")
        flag = True
        
    if age == "":break
    
    # Collect the supplied ages
    group_age_list.append(int(age))

group_age_tup = tuple(group_age_list)

for age in group_age_tup:
    if age <= 2:
        pass
    elif 3 <= age <= 12:
        total_amount += 14.0
    elif age >= 65:
        total_amount += 18.0
    else:
        total_amount += 23.0
        
print("\nTotal group amount: {:.2f}".format(total_amount))