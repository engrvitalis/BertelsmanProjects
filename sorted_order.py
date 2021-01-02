"""
This project accepts number input from the user, sorts it and display 
the values one line at a time.
"""

def sort_num():
    """
    Collect numbers from user and sort them in ascending order.
    """
    
    try:
        # Request initial input from user.
        num = int(input("Enter a number: "))

        # Initialize state variable.
        ls = list()

        # Continuously ask for input and collect 0 is entered.
        while num != 0:
            ls.append(num)
            num = int(input("Enter a number or '0' to stop: "))

        return sorted(ls)
    except:
        print("Invalid Input!")
        return []

def main():

    # Display the result
    for i in sort_num():
        print(i)

if __name__ == '__main__':
    main()
    