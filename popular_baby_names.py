import os


def popular_names(files):
    """
    This program will read all file in BabyNames directory, identify names 
    that are popular for at least one year and return two lists containing most 
    popular names for boys and girls respectively and each of the list cannot contain
    repeated values.

    @param: List - Names of files.
    @return: Tuple - containing 2 lists, most popular names for boys and girls
        respectively.
    """

    # Initialize variables.
    popular_boys_names = list()
    popular_girls_names = list()

    # Go through the boys files.
    for file in files:

        # Initialize variable.
        name, num = None, None

        # Read each file.
        with open(file, 'r') as f_handle:
            # Go through each line
            if 'Boys' in file:
                for line in f_handle:
                    line = line.split()
                    if num is None or num < int(line[1]):
                        name, num = line[0], int(line[1])

                if name not in popular_boys_names:
                    popular_boys_names.append(name)
                name, num = None, None
            else:
                for line in f_handle:
                    line = line.split()
                    if num is None or num < int(line[1]):
                        name, num = line[0], int(line[1])

                if name not in popular_girls_names:
                    popular_girls_names.append(name)
                name, num = None, None

    print(popular_boys_names)
    print(popular_girls_names)


def main():
    # files = os.listdir('BabyNames')
    files = [os.path.join('BabyNames', file) for file in os.listdir('BabyNames')]
    popular_names(files)


if __name__ == '__main__':
    main()