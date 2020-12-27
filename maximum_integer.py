"""
This program will generate 100 random integers between 1 and 100
and display while also keeping track is the maximum number generated and
the number of times it was updated.

Input: None
Output: String of values
"""

import random

# Initialize state variables.
update_count = 0
largest = None

# Generate series of integers update the maximum value while keeping 
# count on the number of updates.
for i in range(100):
    num = random.randint(1, 100)
    if largest is None:
        largest = num
        display = f'{num}'
    elif largest < num:
        largest = num
        display = f"{num} <== Update"
        update_count += 1
    else:
        display = f'{num}'
    
    # Display all relevant information
    print(display)

print(f'\nMaximum value found was {largest}')
print(f'Maximum value was updated {update_count} times')