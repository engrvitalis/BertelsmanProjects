def recurse_sum():
    num = input("Enter a number or blank line to stop: ")
    if num == "":
        return 0.0

    else:
        return float(num) + recurse_sum()


def main():
    print(recurse_sum())


if __name__ == '__main__':
    main()
    