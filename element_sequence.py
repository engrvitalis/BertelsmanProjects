def element_sequence(name, ls):
    if name not in ls:
        return ""
    elif 
        return name + element_sequence(name, ls[:-1])


def get_names(file):
    names = list()

    with open(file, 'r') as f:
        for line in f:
            # 
            names.append(line.lower().split(',')[-1].strip())
    
    return names


def main():
    name = "Hydrogen"
    file = "elements.txt"
    
    element_sequence(name)


if __name__ == '__main__':
    main()