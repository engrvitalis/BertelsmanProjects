def  format_sort_records(data):

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

from operator import itemgetter

PEOPLE = [
    ('Vladimir', 'Putin', 3.626),
    ('Joe', 'Biden', 7.85), 
    ('Jinping', 'Xi', 10.603)]

# Function to return a sorted list by arguments 
# @param keys
# @return sorted list by arguments 
def format_sort_records(list_tuples, *args):
    sort_list = []
    new_list = sorted(list_tuples, key=itemgetter(*args))
    for info in new_list:
        sort_list.append('{1:10} {0:10} {2:5.2f}'.format(*info))
    return sort_list


# sort by last and first name
print('\n'.join(format_sort_records(PEOPLE,1,0)))