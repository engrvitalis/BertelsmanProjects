def element_sequence(name, file):
    with open(file) as f:
        for line in f:
            print(line.lower().split(',')[-1], end='')


def main():
    name = "Hydrogen"
    file = "elements.txt"
    
    element_sequence(name, file)


if __name__ == '__main__':
    main()