def alphabetize_names(obj, key=(key1, key2)):
    from operator import itemgetter
    
    
    # Multi sort obj with key1 and key2
    s = sorted(obj, key=itemgetter(key1, key2)) 
    print()
    for p in sorted(obj, key=itemgetter('last', 'first')):
        print(f'{p["last"]}, {p["first"]}: {p["email"]}')
    print()

PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'}, 
    {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'}, 
    {'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}
    ]

alphabetize_names(PEOPLE)