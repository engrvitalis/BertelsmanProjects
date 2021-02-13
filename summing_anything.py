def mySum(*items):
    # Return empty tuple if no argument was provided.
    if not items:
        return items 

    # Initialize output with the first 
    output = items[0]
    for item in items[1:]:
        output += item
    return output


print(mySum([1,2,3], [4,5,6,[2,4]]))
print(mySum(1,2,3))
print(mySum('1', 's', 't'))
print(mySum())