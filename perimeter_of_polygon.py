'''
This Program will accept x-y coordinate input of a polygon 
from a user and then calculate the perimeter.

Input: Integer
Output: String
'''

coord = []
perimeter = 0
first_pass = False

while True:
    if first_pass:
        x = input('Enter the x part of the coordinate: (blank to quit): ')
    else:
        x = input('Enter the x part of the coordinate: ')
        first_pass = True
    if x == "":break
    
    y = input("Enter the y part of the coordinate: ")
    if y == "":break
    
    x = int(x)
    y = int(y)
    
    # Collecting the coordinates
    coord.append((x, y))
    
i = 0
while i < len(coord)-1:
    perimeter += ((coord[i][0]-coord[i+1][0])**2 + (coord[i][1]-coord[i+1][1])**2)**0.5
    i += 1
    
perimeter += ((coord[i][0]-coord[0][0])**2 + (coord[i][1]-coord[0][1])**2)**0.5
    
print(f'The perimeter of that polygon is {perimeter}')