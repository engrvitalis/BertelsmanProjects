def element_sequence(name, file):
    with open(file) as f:
        for line in f:
            word = line.lower().split(',')
            if word[-1][0] == name.lower()[-1]:
                return name + word


def get_names(file):
    

def main():
    name = "Hydrogen"
    file = "elements.txt"
    
    element_sequence(name, file)


if __name__ == '__main__':
    main()