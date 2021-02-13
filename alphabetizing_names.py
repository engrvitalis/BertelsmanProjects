def alphabetize_names(obj):
    """
    This function takes list of dictionaries containing 
    lastname, firstname and email and returns same sorted in 
    ascending order by lastname and firstname.

    @param: list - obj
    @return: list - sorted list
    """
    
    from operator import itemgetter
    
    
    print()
    for p in sorted(obj, key=itemgetter('last', 'first')):
        print(f'{p["last"]}, {p["first"]}: {p["email"]}')
    print()

PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'}, 
    {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'}, 
    {'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}
    ]

alphabetize_names(PEOPLE)