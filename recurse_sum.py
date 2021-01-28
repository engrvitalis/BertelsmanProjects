def recurse_sum():
    ls = list()
    while True:
        num = input("Enter a number or blank line to stop: ")
        if num == "":
            break

        ls.append(float(num))

