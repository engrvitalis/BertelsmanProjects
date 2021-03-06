def get_rainfall():
    """
    This program continuously prompts the user for name of city
    and quantity of rainfall in mm. When the user enters blank space, 
    the program is terminated and a dict is returned with city names 
    and total rainfall for each city.

    @param: None
    @return: dict
    """

    # Initialize variable.
    rainfall = dict()

    while True:
        # Request city name. Exit if blank line is entered.
        city = input("Enter city name: ")
        if not city:
            break
        
        # Make sure to process only numbers
        try:
            rain_qty = float(input("Enter rain quantity in mm: ").lower())
        except ValueError:
            print("Quantity of rain must be either int or float!")
            continue

        # Update rainfall with city and rain_qty.
        if city in rainfall:
            rainfall[city] += rain_qty
        else:
            rainfall[city] = rain_qty

    return rainfall


def main():
    # Call get_rainfall, format and display returned value.
    data = get_rainfall()
    # Don't print header if there is nothing to print.
    if not data:
        quit()

    print(f'\nCity\t\tRainfall(mm)')
    for key, value in data.items():
        print(f'{key.capitalize()}\t\t{value}')
    print()

# Driver function.
main()