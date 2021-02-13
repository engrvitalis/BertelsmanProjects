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
    s = set()
    
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            s.add(line)
        return s

    print(ls)


def main():
    classes = 'classes.txt'
    instructors = 'instructors.txt'

    share_class(classes, instructors)
    get_instructors(instructors)


if __name__ == '__main__':
    main()