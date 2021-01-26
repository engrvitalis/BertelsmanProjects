import os


def popular_names(ls):
    """
    This program will read all file in BabyNames directory, identify names 
    that are popular for at least one year and return two lists containing most 
    popular names for boys and girls respectively and each of the list cannot contain
    repeated values.

    @param: List - Names of files.
    @return: Tuple - containing 2 lists, most popular names for boys and girls
        respectively.
    """

    # Separate male from female names.
    boys_files = [name for name in ls if 'Boys' in name]
    girls_files = [name for name in ls if 'Girls' in name]
    # print(boys_files)
    # print(girls_files)

    # for file in 




def main():
    ls = os.listdir('BabyNames')
    # print(ls)
    popular_names(ls)


if __name__ == '__main__':
    main()