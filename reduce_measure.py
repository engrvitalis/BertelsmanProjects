"""
This program expresses imperial volume using the largest possible units.
"""

def reduce_measure(num, unit):
    if unit == "teaspoon":
        cup = num // (16*3)
        tablespoon = (num % (16*3)) // 3
        teaspoon = (num % (16*3)) % 3
        return (cup, tablespoon, teaspoon)

    else:
        cup = num // 16
        tablespoon = num % 16 
        return (cup, tablespoon)

def tense(tup):
    """
    This function takes a tuple of numbers and return 
    a tuple of strings. It makes sure that unit of measures are 
    displayed as either singular or plural words.
    """
    # Initialize variables.
    u = ('cup', 'tablespoon', 'teaspoon')
    ls = []
    index = 0

    # Go through the units of measure and append 's' if value is more than one.
    for i in tup:
        if i > 1:
            ls.append(str(u[index]) + 's')
        else:
            ls.append(u[index])
        index += 1
    
    return tuple(ls)

def main():
    # Request users input.
    x = int(input("Enter number: "))
    y = input("Enter unit of measure (tablespoon or teaspoon): ")

    # Check for invalid input.
    if y == 'tablespoon' or y == 'teaspoon':
        m = reduce_measure(x, y)
        t = tense(m)
        result = ""

        # Format output.
        for i in range(len(m)):
            if m[i] == 0:
                continue
            result += f', {m[i]} {t[i]}'

        print(result[2:])

    else:
        print("invalid Entry!")
 
if __name__ == '__main__':
    main()
    