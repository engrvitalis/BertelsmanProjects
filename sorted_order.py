"""
This project accepts number input from the user, sorts it and display 
the values one line at a time.
"""

def sort_num():

    # Request input from user.
    num = int(input("Enter a number: "))

    ls = list()

    while num != 0:
        ls.append(num)
        num = int(input("Enter a number: "))

    return sorted(ls)

def display(ls):
    for i in ls:
        print(i)

def main():

    # Collect and sort the numbers.
    ls = sort_num()

    # Display the result
    display(ls)

if __name__ == '__main__':
    main()
    