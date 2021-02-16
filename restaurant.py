def restaurant():
    """
    This function takes orders from customer and displays the 
    running total.

    @param: None
    @return int - total
    """

    # Initialize variables.
    menu = {'egusi': 150, 
    'akpu': 150, 
    'onugbu': 200, 
    'okro': 150, 
    'garri': 150, 
    'nsala': 300, 
    'rice': 150, 
    'stew': 150, 
    'isiewu': 1000
    }
    total = 0

    print()
    # Request input from user. Exit program if blank line is entered.
    while True:
        order = input("Order: ").strip().lower()
        if not order:
            break
        
        # Check if customer order is available in the menu. Increment total
        # if order is available and display appropriate message.
        if order in menu:
            total += menu[order]
            print(f'{order} cost {menu[order]}, total is {total}')
        else:
            print(f'Sorry, we are fresh out of {order} today.')

    print(f'Your total is {total}')

    return total


def main():
    # Ask user for the order and display approriate message.
    restaurant()

    print()

# Driver function.
main()