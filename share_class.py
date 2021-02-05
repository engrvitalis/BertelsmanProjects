def share_class(classes, instructors):
    class_dic = dict()
    instructor_ls = list()
    schedule = dict()

    with open(classes) as f:
        for line in f:
            line = line.split()
            class_dic[line[0]] = int(line[1])
    
    with open(instructors) as f:
        for line in f:
            instructor_ls.append(line.strip())
    instructor_ls = set(instructor_ls)

    items = class_dic.items()
    items_value_sorted = sorted([(item[1], item[0]) for item in items])
    items_sorted = [(item[1], item[0]) for item in items_value_sorted]
    items_sorted = items_sorted[::-1]

    for instructor in instructor_ls:
        schedule[instructor] = []

    i = 0
    ind = 0

    while i < len(items_sorted):
        for name in schedule:
            schedule[name].append(items_sorted[i])
            i += 1
            ind += 1


    print(class_dic)
    print(items_sorted)
    print(schedule)

def main():
    classes = 'classes.txt'
    instructors = 'instructors.txt'

    share_class(classes, instructors)


if __name__ == '__main__':
    main()