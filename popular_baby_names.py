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
                extract_names(name, num, popular_boys_names, f_handle)
            else:
                extract_names(name, num, popular_girls_names, f_handle)

    return tuple([popular_boys_names, popular_girls_names])

    # print(popular_boys_names)
    # print(popular_girls_names)
# 


def extract_names(name, num, ls, f_handle):

    # Go through each line in the file.
    for line in f_handle:
        line = line.split()
        # Update baby name if the number use is the number of use 
        # is higher than previous value.
        if num is None or num < int(line[1]):
            name, num = line[0], int(line[1])

    # Update ls with new popular name
    if name not in ls:
        ls.append(name)


def main():
    # Get file path from directory.
    files = [os.path.join('BabyNames', file) for file in os.listdir('BabyNames')]

    try:
        # Extract popular names from files.
        boys, girl = popular_names(files)
    except:
        print("Invalid file name!")
        quit()

    # Display name list
    print('\nThe most popular baby names:')
    print(f'Boys: {", ".join(boys)}.')
    print(f'Girls: {", ".join(girl)}.')


if __name__ == '__main__':
    main()