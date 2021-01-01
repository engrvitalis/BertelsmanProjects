"""
This program expresses imperial volume using the largest possible units.
"""

def reduce_measure(num, unit):
    if unit == "teaspoon":
        cup = num//(16*3)
        tablespoon = (num % (16*3)) // 3
        teaspoon = (num % (16*3)) % 3
        return (cup, tablespoon, teaspoon)

    elif unit == "tablespoon":
        cup = num // 16
        tablespoon = num % 16 
        return (cup, tablespoon)
    else:
        return num

def tense(tup):
    """
    This function takes a tuple of numbers and return 
    a tuple of strings.
    """
    v = ('cup', 'tablespoon', 'teaspoon')
    ls = []
    index = 0
    for i in tup:
        if i > 1:
            ls.append(str(v[index]) + 's')
        else:
            ls.append(v[index])
        index += 1
    
    return tuple(ls)

def main():
    x = 59
    y = "teaspoon"
    m = reduce_measure(x, y)
    t = tense(m)

    result = ""
    for i in range(len(m)):
        result += f', {m[i]} {t[i]}'

    print(result[2:])
 
if __name__ == '__main__':
    main()
    