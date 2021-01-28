def recurse_sum():
    num = input("Enter a number or blank line to stop: ")
    if num == "":
        return 0.0
    else:
        return float(num) + recurse_sum()


def main():
    try:
        print(f'\nTotal: {recurse_sum()}')
    except:
        print("\nInvalid Input! You must enter a float or an int: ")

if __name__ == '__main__':
    main()
    