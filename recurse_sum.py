def recurse_sum():






def get_nums():
    ls = list()
    while True:
        num = input("Enter a number or blank line to stop: ")
        if num == "":
            break

        ls.append(float(num))
    return ls


def main():
    print(get_nums())


if __name__ == '__main__':
    main()
    