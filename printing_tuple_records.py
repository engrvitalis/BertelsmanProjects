def  format_sort_records(data):
    """
    This function takes a list of tuples with three 
    fields, first name, last name and duration as argument.
    It will sort the list by last name and print a formatted 
    output.

    @param: list
    @return: str
    """

    import operator

    from operator import itemgetter

    ls = list()
    data = sorted(data, key=itemgetter(1,0))

    for first, last, time in data:
        ls.append("{:10} {:10} {:5.2f}".format(last, first, time))
    
    return '\n'.join(ls)


def main():
    PEOPLE = [('Joe', 'Biden', 7.85), 
	('Vladimir', 'Putin', 3.626),
	('Jinping', 'Xi', 10.603)
    ]

    print( format_sort_records(PEOPLE))


main()