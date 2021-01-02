"""
This project accepts number input from the user, sorts it and display 
the values one line at a time.
"""

def sort_num():
    try:
        # Request initial input from user.
        num = int(input("Enter a number: "))

        # Initialize state variable.
        ls = list()

        # Continuously ask for input and collect 0 is entered.
        while num != 0:
            ls.append(num)
            num = int(input("Enter a number: "))

        return sorted(ls)
    except:
        print("Invalid Input!")
        return []

def display(ls):
    """
    Loop through the list argument and print the content on separate lines.
    """

    for i in ls:
        print(i)

def main():

    # Collect numbers from user and sort them in ascending order.
    ls = sort_num()

    # Display the result
    display(ls)

if __name__ == '__main__':
    main()
    