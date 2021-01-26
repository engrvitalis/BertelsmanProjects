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
    pass


def separate_files(files):
    # Separate male from female names.
    boys_files = [name for name in files if 'Boys' in name]
    girls_files = [name for name in files if 'Girls' in name]
    # print(boys_files)
    # print(girls_files)
    return tuple([boys_files, girls_files])
    




def main():
    files = os.listdir('BabyNames')
    # print(ls)
    popular_names(files)
    print(separate_files(files))


if __name__ == '__main__':
    main()