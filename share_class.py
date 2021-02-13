def share_class(classes, instructors):
    pass


def get_instructors(file):
    """
    
    """
    ls = list()
    dic = dict()

    for name in randomize_names(file):
        dic[name] = []
        ls.append(dic)
        dic = dict()

    return ls


def randomize_names(file):
    """
    This function reads file and add lines to 
    set, s.

    @param: str - file.
    @return: set - with names in no particular order.
    """

    # Initialize variables.
    s = set()

    # Go through file and add the content to s.
    with open(file, 'r') as f:
        for line in f:
            s.add(line.strip())
    return s


def main():
    classes = 'classes.txt'
    instructors = 'instructors.txt'

    share_class(classes, instructors)
    get_instructors(instructors)
    # print(randomize_names(instructors))


if __name__ == '__main__':
    main()