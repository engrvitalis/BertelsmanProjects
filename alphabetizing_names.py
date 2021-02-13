def alphabetize_names(obj, key1, key2):
    """
    This is a multi key sorting function.

    It takes three arguments: obj, key1 and key2. 
    obj is a list or tuple of dictionaries containing first, 
    last and email keys. key1 and key2 are sorting keys which can 
    be either first, last or email. When called with obj and the 
    keys, it returns same obj sorted by key1 and then key2.

    eg:
        alphabetize_names(PEOPLE, 'first', 'second')
        --> return PEOPLE sorted by first, and then second key.

    @param: list - obj; any immutable object type for keys - key1 and key2
    @return: list - sorted list
    """

    import operator as op
    
    
    # Sort obj dicts by last and first name keys.
    s = sorted(obj, key=op.itemgetter(key1, key2))

    print()
    # Print the sorted list content.
    for p in s:
        print(f'{p["last"]}, {p["first"]}: {p["email"]}')
    print()

PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'}, 
    {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'}, 
    {'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}
    ]

# Sort PEOPLE in ascending order by last and first name.
alphabetize_names(PEOPLE, 'last', 'first')