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
    t = ()
    for i in tup:
        if i > 1:
            t.append('')

def main():
    x = 59
    y = "teaspoon"
    m = reduce_measure(x, y)

    if len(m) == 3:
        print(f'{m[0]} cup(s), {m[1]} tablespoon(s), {m[2]} teaspoon(s)')
    elif len(m) == 2:
        print(f'{m[0]} cup(s), {m[1]} tablespoon(s)')
    else:
        print(f'{m[0]} cups(s)')

if __name__ == '__main__':
    main()
    