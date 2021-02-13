def share_class(classes, instructors):
    pass


def get_instructors(file):
    ls = list()
    dic = dict()
    s = set()

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            s.add(line)
        print(s)
            # dic[line.strip()] = []
            # # print(dic)
            # ls.append(dic)
            # dic = dict()


def randomize_names(file):
    """
    This function reads file and add lines to 
    set, s.

    @param: str - file
    @return: set
    """

    # 
    s = set()

    with open(file, 'r') as f:
        for line in f:
            s.add(line.strip())
    return s


def main():
    classes = 'classes.txt'
    instructors = 'instructors.txt'

    share_class(classes, instructors)
    # get_instructors(instructors)
    print(randomize_names(instructors))


if __name__ == '__main__':
    main()